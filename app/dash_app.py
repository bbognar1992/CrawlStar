from dash import Dash, html, dcc, Input, Output, State
import requests
from datetime import datetime
import dash_bootstrap_components as dbc

# Initialize Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    html.H1("Crawler Scheduling Dashboard"),

    html.Div([
        dcc.Input(id="crawler-name", type="text",
                  placeholder="Enter crawler name"),
        dcc.DatePickerSingle(id="run-date", date=datetime.now().date()),
        dcc.Input(id="run-time", type="time", placeholder="Enter time"),
        html.Button("Schedule Crawl", id="schedule-btn"),
        html.Div(id="output-message"),
    ]),
])


@app.callback(
    Output("output-message", "children"),
    Input("schedule-btn", "n_clicks"),
    State("crawler-name", "value"),
    State("run-date", "date"),
    State("run-time", "value"),
)
def schedule_crawl(n_clicks, crawler_name, run_date, run_time):
    if n_clicks:
        if not crawler_name or not run_date or not run_time:
            return "Please provide all fields."

        # Combine date and time for scheduling
        run_at = f"{run_date}T{run_time}"

        # Schedule crawl using FastAPI endpoint
        response = requests.post("http://localhost:8000/schedule_crawl", json={
            "crawler_name": crawler_name,
            "run_at": run_at
        })

        if response.status_code == 200:
            return f"Crawl scheduled for {crawler_name} at {run_at}"
        else:
            return f"Error: {response.json().get('detail', 'Unknown error')}"

    return ""


if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=8050)
