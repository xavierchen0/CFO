from cfo.static.reuse_components import top_upload_files
from dash import html, dcc
import dash_bootstrap_components as dbc

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
            className="mx-3 mt-4",
        ),
        fluid=True,
    ),
    # Displayed table to check before submitting
    dbc.Container(
        dbc.Row(
            dbc.Col(
                html.Div(
                    id="displayed_table",
                ),
            ),
            className="mx-3 mt-4",
        ),
        fluid=True,
    ),
]
