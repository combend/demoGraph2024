from flask import Flask, render_template
import process_attendance_data

app = Flask(__name__)

attendance_data = [
    {"Sport": "Rowing", "Attendance": 90},
    {"Sport": "Basketball", "Attendance": 85},
    {"Sport": "Cricket", "Attendance": 92},
    {"Sport": "Rifle Shooting", "Attendance": 88},
    {"Sport": "Water Polo", "Attendance": 80},
    {"Sport": "Sailing", "Attendance": 95},
    {"Sport": "Swimming", "Attendance": 91},
    {"Sport": "Tennis", "Attendance": 87},
    {"Sport": "Table Tennis", "Attendance": 89},
]


@app.route('/')
def index():
    chart_json = process_attendance_data.percent_bar_chart(attendance_data)
    sports_alphabetical = sorted_data = sorted(attendance_data, key=lambda x: x["Sport"])
    return render_template('index.html', data=sports_alphabetical, chart_json=chart_json)


@app.route('/sport/<sport_name>')
def sport_stub(sport_name):
    return f"<h1>Information about {sport_name}</h1><p>This page is under construction.</p>"


if __name__ == '__main__':
    app.run(debug=True)
