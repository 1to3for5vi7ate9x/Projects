let lorenzX, lorenzY, lorenzZ;
let rosslerX, rosslerY, rosslerZ;
let lorenzA = 10, lorenzB = 28, lorenzC = 8 / 3;
let rosslerA = 0.2, rosslerB = 0.2, rosslerC = 5.7;
let dt = 0.01;
let lorenzBall, rosslerBall;

function setup() {
  createCanvas(1440, 800);
  background(0);
  
  // Initialize the variables
  lorenzX = random(-20, 20);
  lorenzY = random(-20, 20);
  lorenzZ = random(0, 40);

  rosslerX = random(-30, 30);
  rosslerY = random(-30, 30);
  rosslerZ = random(-30, 30);

  // Initialize the balls
  lorenzBall = new Ball(255, 0, 0); // Red ball for Lorenz attractor
  rosslerBall = new Ball(0, 0, 255); // Blue ball for Rössler system
}

function draw() {
  // Update the Lorenz system
  let lorenzDX = lorenzA * (lorenzY - lorenzX);
  let lorenzDY = lorenzX * (lorenzB - lorenzZ) - lorenzY;
  let lorenzDZ = lorenzX * lorenzY - lorenzC * lorenzZ;
  lorenzX += lorenzDX * dt;
  lorenzY += lorenzDY * dt;
  lorenzZ += lorenzDZ * dt;

  // Update the Rössler system
  let rosslerDX = -rosslerY - rosslerZ;
  let rosslerDY = rosslerX + rosslerA * rosslerY;
  let rosslerDZ = rosslerB + rosslerZ * (rosslerX - rosslerC);
  rosslerX += rosslerDX * dt;
  rosslerY += rosslerDY * dt;
  rosslerZ += rosslerDZ * dt;

  // Map the system variables to the canvas
  let lorenzPX = map(lorenzX, -30, 30, 0, width);
  let lorenzPY = map(lorenzY, -30, 30, height, 0);
  
  let rosslerPX = map(rosslerX, -30, 30, 0, width);
  let rosslerPY = map(rosslerY, -30, 30, height, 0);

  // Update the balls' positions
  lorenzBall.update(lorenzPX, lorenzPY);
  rosslerBall.update(rosslerPX, rosslerPY);

  // Clear the canvas
  background(0);

  // Display the balls
  lorenzBall.display();
  rosslerBall.display();
}

class Ball {
  constructor(r, g, b) {
    this.posX = 0;
    this.posY = 0;
    this.radius = 6;
    this.color = color(r, g, b);
  }

  update(x, y) {
    this.posX = x;
    this.posY = y;
  }

  display() {
    fill(this.color);
    noStroke();
    ellipse(this.posX, this.posY, this.radius * 1.5, this.radius * 1.5);
  }
}
