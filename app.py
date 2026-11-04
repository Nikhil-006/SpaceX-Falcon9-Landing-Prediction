import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
df = pd.read_csv("data/spacex_cleaned.csv")

print("Dataset loaded successfully!")
print(df.shape)
app = Dash(__name__)

app.title = "SpaceX Falcon 9 Dashboard"
app.layout = html.Div([

    html.H1(
        "SpaceX Falcon 9 Launch Dashboard",
        style={"textAlign": "center"}
    ),

    html.H3("Select Launch Site:"),

    dcc.Dropdown(
        id="site-dropdown",
        options=[
            {"label": site, "value": site}
            for site in df["LaunchSite"].unique()
        ],
        value="CCAFS SLC 40",
        clearable=False
    ),

    html.Br(),

    html.Div(id="output-container"),

    dcc.Graph(id="success-pie-chart"),

    dcc.Graph(id="payload-scatter-chart")

])
@app.callback(
    [
        Output("output-container", "children"),
        Output("success-pie-chart", "figure"),
        Output("payload-scatter-chart", "figure")
    ],
    Input("site-dropdown", "value")
)

def update_dashboard(selected_site):

    filtered_df = df[df["LaunchSite"] == selected_site]

    total_launches = len(filtered_df)

    successful_landings = filtered_df["Class"].sum()

    unsuccessful_landings = total_launches - successful_landings

    success_rate = (successful_landings / total_launches) * 100

    summary = html.Div([

        html.H4(f"Total Launches: {total_launches}"),

        html.H4(f"Successful Landings: {successful_landings}"),

        html.H4(f"Unsuccessful Landings: {unsuccessful_landings}"),

        html.H4(f"Success Rate: {success_rate:.2f}%")

    ])

    pie_chart = px.pie(
        names=["Successful", "Unsuccessful"],
        values=[successful_landings, unsuccessful_landings],
        title="Landing Success Distribution"
    )

    scatter_chart = px.scatter(
        filtered_df,
        x="PayloadMass",
        y="Class",
        color="Class",
        title="Payload Mass vs Landing Outcome",
        labels={
            "PayloadMass": "Payload Mass (kg)",
            "Class": "Landing Outcome"
        }
    )

    return summary, pie_chart, scatter_chart
if __name__ == "__main__":
    app.run(debug=True)