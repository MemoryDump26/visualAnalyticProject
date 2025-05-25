import json
import math

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, Input, Output, callback, dash_table, dcc, html
from plotly.subplots import make_subplots

from create_color_map import create_color_map

df = pd.read_csv("output.csv")
daily_cases_df = pd.read_csv(
    "daily-new-confirmed-covid-19-cases-per-million-people.csv"
)
cumulative_cases_df = pd.read_csv("cumulative-confirmed-covid-19-cases.csv")

line_color_map = create_color_map()
fill_color_map = create_color_map(0.8)

app = Dash()

graph_style = {
    "display": "inline-block",
    "justify-content": "center",
    "align-items": "center",
    "padding": "0 0",
}
# Requires Dash 2.17.0 or later
app.layout = [
    html.H1(
        children="Phân tích tần suất chủng SAR-CoV-2", style={"textAlign": "center"}
    ),
    html.Div(
        [
            dcc.Dropdown(df["Country"].unique(), "Vietnam", id="dropdown-selection"),
            dcc.Checklist(["Hiển thị tổng số ca nhiễm"], [], id="use-cumulative"),
        ],
        style={"width": "40%"},
    ),
    html.Div(
        [
            html.Div(
                [
                    dcc.Graph(id="norm-variant-graph"),
                ],
                style=graph_style | {"width": "60%"},
            ),
            html.Div(
                [
                    dcc.Graph(id="variant-pie-chart"),
                ],
                style=graph_style | {"width": "40%"},
            ),
            # html.Div(
            #     [
            #         dcc.Graph(id="daily-cases-graph"),
            #     ],
            #     style={"width": "60%", "display": "inline-block", "padding": "0 0"},
            # ),
        ],
        style={
            "display": "flex",
            "justify-content": "center",
            "align-items": "center",
            # 'height': '100vh',
        },
    ),
    dcc.Store(id="weekHover"),
]


def get_hover_info(week, data):
    info = data.get(week, {})

    result = ""
    for variant, amount in info.items():
        result += str(variant)
        result += ": "
        result += str(amount)
        result += "<br>"
    return result


# @callback(
#     Output("daily-cases-graph", "figure"),
#     Input("dropdown-selection", "value"),
# )
# def update_daily_case_graph_(value):
#     dff = daily_cases_df[daily_cases_df.Entity == value]
#     fig = go.Figure()
#     fig.add_trace(
#         go.Scatter(
#             x=dff["Day"],
#             y=dff[
#                 "Daily new confirmed cases of COVID-19 per million people (rolling 7-day average, right-aligned)"
#             ],
#             mode="lines",
#             line=dict(width=2, shape="spline", smoothing=1),
#             fill="tozeroy",
#             connectgaps=False,
#             hoverinfo="none",
#             showlegend=False,
#         )
#     )
#     fig.update_layout(
#         height=400,
#         hovermode="x unified",
#         title=dict(text="Số ca nhiễm mới hàng ngày trên triệu người"),
#         xaxis=dict(title=dict(text="Ngày")),
#         yaxis=dict(title=dict(text="Số ca")),
#     )
#
#     return fig


@callback(
    Output("norm-variant-graph", "figure"),
    Output("weekHover", "data"),
    Input("dropdown-selection", "value"),
    Input("use-cumulative", "value"),
)
def update_graph_2(country, cumulative):
    # fig = go.Figure()
    if cumulative:
        title = "Tổng số ca nhiễm"
    else:
        title = "Số ca nhiễm mới hàng ngày trên triệu người"

    fig = make_subplots(
        rows=2,
        cols=1,
        shared_xaxes=True,
        subplot_titles=(
            "Tần suất các biến thể",
            title,
        ),
        vertical_spacing=0.1,
    )
    dff = df[df["Country"] == country]
    dff = dff.dropna(axis="columns", how="all")

    weekHover = {}

    for idx, row in dff.iterrows():
        sortedRow = row[4:].sort_values(ascending=False)
        sortedRow = sortedRow.dropna(how="all")
        weekHover.update({row["Week"]: sortedRow.to_dict()})

    columns = dff.columns[4:]
    for variant in columns:
        fig.add_trace(
            go.Scatter(
                x=dff["Week"],
                y=dff[variant],
                mode="lines",
                line=dict(
                    width=1, shape="linear", smoothing=1, color=line_color_map[variant]
                ),
                # fillcolor=color_map[variant],
                # fill='tozeroy',
                name=variant,
                connectgaps=False,
                stackgroup="one",
                groupnorm="percent",
                hoverinfo="none",
                showlegend=False,
            ),
            row=1,
            col=1,
        )

    if cumulative:
        dff = cumulative_cases_df[cumulative_cases_df.Entity == country]
        y_name = "Total confirmed cases of COVID-19"
    else:
        dff = daily_cases_df[daily_cases_df.Entity == country]
        y_name = "Daily new confirmed cases of COVID-19 per million people (rolling 7-day average, right-aligned)"
    fig.add_trace(
        go.Scatter(
            name="Số ca",
            x=dff["Day"],
            y=dff[y_name],
            mode="lines",
            line=dict(width=2, shape="spline", smoothing=1),
            fill="tozeroy",
            connectgaps=False,
            # hoverinfo="none",
            showlegend=False,
        ),
        row=2,
        col=1,
    )

    fig.update_layout(
        height=900,
        hovermode="x unified",
        title=dict(text=""),
        xaxis=dict(title=dict(text="")),
        yaxis=dict(title=dict(text=""), range=[0, 100]),
    )

    return fig, weekHover


@callback(
    Output("variant-pie-chart", "figure"),
    Input("norm-variant-graph", "hoverData"),
    Input("weekHover", "data"),
    Input("dropdown-selection", "value"),
)
def display_hover_data(hoverData, weekHover, value):
    if hoverData is None:
        return
    dff = df[df["Country"] == value]
    dff = dff.dropna(axis="columns", how="all")
    fig = go.Figure()
    currentWeek = hoverData["points"][0]["x"]
    if weekHover.get(currentWeek) is None:
        currentWeek = min(
            dff["Week"],
            key=lambda x: abs(pd.to_datetime(x) - pd.to_datetime(currentWeek)),
        )

    labels = (*weekHover[currentWeek].keys(),)
    values = (*weekHover[currentWeek].values(),)
    colors = []
    for l in labels:
        colors.append(fill_color_map[l])

    fig.add_trace(
        go.Pie(
            labels=labels,
            values=values,
            marker=dict(colors=colors),
            textinfo="label+percent",
            pull=0.1,
            # showlegend=False,
            textposition="inside",
        )
    )
    fig.update_layout(
        height=700,
        title=dict(text=currentWeek, font=dict(size=30)),
        title_x=0.5,
        title_y=0.95,
        # margin=dict(t=300, b=0, l=0, r=0),  # Adjust margins (t=top margin)
        uniformtext_minsize=12,
        uniformtext_mode="hide",
    )

    return fig
    # return json.dumps(weekHover[currentWeek])


if __name__ == "__main__":
    app.run(debug=False)
