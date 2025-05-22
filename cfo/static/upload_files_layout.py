import dash_bootstrap_components as dbc
from dash import dcc, html

from cfo.static.reuse_components import top_upload_files

upload_files_layout = [
    # Top of page
    top_upload_files,
    # Upload
    dbc.Container(
        dbc.Row(
            # Only accept one .csv file at a time
            dbc.Col(
                dcc.Upload(
                    id="upload_data",
                    children=html.Div(
                        ["Drag and Drop, or ", html.A("Select Files")]
                    ),
                    style={
                        "height": "300px",
                        "lineHeight": "300px",
                        "borderWidth": "1px",
                        "borderStyle": "dashed",
                        "borderRadius": "15px",
                        "textAlign": "center",
                    },
                    accept=".csv",
                ),
            ),
            className="mx-3 my-4",
        ),
        fluid=True,
    ),
    # Displayed table to check before submitting
    dbc.Container(
        [
            dbc.Row(
                dbc.Alert(
                    [
                        html.H4("Error"),
                        html.P(id="alert_date_error_msg"),
                    ],
                    id="alert_date",
                    is_open=False,
                    color="#eb6f92",
                    dismissable=True,
                    fade=True,
                ),
                className="mx-3 my-4",
            ),
            dbc.Row(
                dbc.Alert(
                    [
                        html.H4("Error"),
                        html.P(id="alert_income_error_msg"),
                    ],
                    id="alert_income",
                    is_open=False,
                    color="#eb6f92",
                    dismissable=True,
                    fade=True,
                ),
                className="mx-3 my-4",
            ),
            dbc.Row(
                dbc.Alert(
                    [
                        html.H4("Error"),
                        html.P(id="alert_amount_error_msg"),
                    ],
                    id="alert_amount",
                    is_open=False,
                    color="#eb6f92",
                    dismissable=True,
                    fade=True,
                ),
                className="mx-3 my-4",
            ),
            dbc.Row(
                dbc.Col(
                    html.Div(
                        id="displayed_table",
                    ),
                ),
                className="mx-3 my-4",
            ),
        ],
        fluid=True,
    ),
]
