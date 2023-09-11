from flask import Flask, request, jsonify
from flask_cors import CORS
from geopy.distance import geodesic

app = Flask(__name__)
CORS(app)

students = [
    {
        'id': 1,
        'name': 'John Doe',
        'latitude': 37.7749,
        'longitude': -122.4194
    },
    {
        'id': 2,
        'name': 'Jane Smith',
        'latitude': 37.3382,
        'longitude': -121.8863
    },
    # Add more students here...
]

@app.route('/attendance', methods=['POST'])
def mark_attendance():
    data = request.get_json()
    student_id = data['student_id']
    latitude = data['latitude']
    longitude = data['longitude']

    student = next((s for s in students if s['id'] == student_id), None)
    if not student:
        return jsonify({'message': 'Student not found'}), 404

    distance = calculate_distance(latitude, longitude, student['latitude'], student['longitude'])
    if distance <= 100:  # Adjust the range as needed
        # Mark attendance for the student
        # You can add your own logic here
        return jsonify({'message': 'Attendance marked'})
    else:
        return jsonify({'message': 'Out of range'}), 400

def calculate_distance(lat1, lon1, lat2, lon2):
    coords_1 = (lat1, lon1)
    coords_2 = (lat2, lon2)
    return geodesic(coords_1, coords_2).meters

if __name__ == '__main__':
    app.run(debug=True)
