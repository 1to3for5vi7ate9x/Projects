#include <QApplication>
#include <QWidget>
#include <QVBoxLayout>
#include <QPushButton>
#include <QTimer>
#include <QSystemTrayIcon>
#include <QMenu>
#include <QDebug>
#include <QProcess>
#include <QNetworkInterface>

class BatteryMonitor : public QWidget {
    Q_OBJECT

public:
    explicit BatteryMonitor(QWidget *parent = nullptr) : QWidget(parent) {
        setupUI();
        setupSystemTrayIcon();
        connect(startButton, &QPushButton::clicked, this, &BatteryMonitor::startMonitoring);
        connect(stopButton, &QPushButton::clicked, this, &BatteryMonitor::stopMonitoring);
        connect(exitAction, &QAction::triggered, qApp, &QApplication::quit);
    }

private slots:
    void startMonitoring() {
        // Find IP address of Android device
        QString ipAddress = findAndroidDeviceIPAddress();
        if (ipAddress.isEmpty()) {
            qDebug() << "Android device not found. Please check the connection.";
            return;
        }

        // Connect to Android device via ADB
        QString adbConnectCommand = "adb connect " + ipAddress + ":5555";
        qDebug() << "Connecting to Android device:" << adbConnectCommand;
        QProcess::execute(adbConnectCommand);

        // Start monitoring battery level
        QTimer::singleShot(0, this, &BatteryMonitor::checkBatteryLevel);
        startButton->setEnabled(false);
        stopButton->setEnabled(true);
    }

    void stopMonitoring() {
        // Disconnect from Android device
        QProcess::execute("adb disconnect");
        startButton->setEnabled(true);
        stopButton->setEnabled(false);
    }

    void checkBatteryLevel() {
        // Retrieve battery information and check level
        QString adbBatteryCommand = "adb shell dumpsys battery";
        QString batteryInfo = QProcess::execute(adbBatteryCommand);

        // Parse battery level
        int levelIndex = batteryInfo.indexOf("level:");
        if (levelIndex != -1) {
            QString levelStr = batteryInfo.mid(levelIndex + 7, 2).trimmed();
            int batteryLevel = levelStr.toInt();
            qDebug() << "Battery Level:" << batteryLevel << "%";

            // Display notification if battery level falls below 10%
            if (batteryLevel <= 10) {
                displayNotification("Battery level is low (" + levelStr + "%). Please charge your device.");
            }
        }

        // Check battery level periodically (every 5 minutes)
        QTimer::singleShot(5 * 60 * 1000, this, &BatteryMonitor::checkBatteryLevel);
    }

    void displayNotification(const QString& message) {
        // Display notification on macOS using AppleScript
        QString script = "display notification \"" + message + "\" with title \"Battery Alert\"";
        QString command = "osascript -e '" + script + "'";
        QProcess::execute(command);
    }

    QString findAndroidDeviceIPAddress() {
        // Find IP address of Android device
        QList<QNetworkInterface> interfaces = QNetworkInterface::allInterfaces();
        for (const QNetworkInterface& iface : interfaces) {
            if (iface.name().startsWith("bridge")) {
                QList<QNetworkAddressEntry> addresses = iface.addressEntries();
                for (const QNetworkAddressEntry& address : addresses) {
                    if (address.ip().protocol() == QAbstractSocket::IPv4Protocol) {
                        QString ipAddress = address.ip().toString();
                        if (ipAddress != "127.0.0.1") {
                            return ipAddress;
                        }
                    }
                }
            }
        }
        return QString();
    }

    void setupSystemTrayIcon() {
        trayIcon = new QSystemTrayIcon(QIcon(":/icon.png"), this);
        trayIcon->show();

        QMenu* trayMenu = new QMenu(this);
        startAction = trayMenu->addAction("Start Monitoring");
        stopAction = trayMenu->addAction("Stop Monitoring");
        trayMenu->addSeparator();
        exitAction = trayMenu->addAction("Exit");

        trayIcon->setContextMenu(trayMenu);
    }

    void setupUI() {
        QVBoxLayout *layout = new QVBoxLayout(this);
        startButton = new QPushButton("Start Monitoring", this);
        stopButton = new QPushButton("Stop Monitoring", this);
        stopButton->setEnabled(false);

        layout->addWidget(startButton);
        layout->addWidget(stopButton);

        setLayout(layout);
    }

    QPushButton *startButton;
    QPushButton *stopButton;
    QSystemTrayIcon *trayIcon;
    QAction *startAction;
    QAction *stopAction;
    QAction *exitAction;
};

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);
    BatteryMonitor monitor;
    monitor.show();

    return app.exec();
}

#include "main.moc"



