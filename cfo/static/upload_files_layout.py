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
                    "borderRadeus": "5px",
                    "textAlign": "center",
                },
                accept=".csv",
            ),
            justify="center",
            class_name="mx-3 mt-4",
        ),
        fluid=True,
    ),
]
