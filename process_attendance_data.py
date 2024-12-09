import plotly.graph_objs as go
import plotly.io as pio

def percent_bar_chart(data):
    sports = []
    attendance_percentages = []
    sorted_data = sorted(data, key=lambda x: x["Attendance"], reverse=True)
    for item in sorted_data:
        sports.append(item["Sport"])
        attendance_percentages.append(item["Attendance"])

    min_attendance = min(attendance_percentages)
    y_axis_start = max(0, min_attendance - 10)  # Ensure it doesn't go below 0

    # https://plotly.com/python/bar-charts/#basic-bar-charts-with-plotlygraphobjects
    # https://plotly.com/python-api-reference/generated/plotly.graph_objects.Figure.html
    bar_chart = go.Figure(
        data=[go.Bar(x=sports, y=attendance_percentages, name="Attendance Percentage")]
    )
    bar_chart.update_layout(
        title="Sports Attendance",
        title_x=0.5,
        title_font_size=30,
        title_font_family="Arial",
        xaxis_title="Sport",
        yaxis_title="Attendance (%)",
        yaxis = dict(range=[y_axis_start, 100]),
        clickmode="event+select"
    )

    return pio.to_json(bar_chart)