import dash_bootstrap_components as dbc
from dash import html

_nav_dashboard = dbc.Nav(
    [
        html.A(
            html.I(className="fa fa-pie-chart fa-2xl py-3 me-4"),
            href="/dashbord",
        ),
        dbc.NavItem(
            dbc.NavLink(
                "Dashboard",
                href="/dashboard",
                active=True,
                class_name="py-1 px-4 me-2 rounded-pill",
            )
        ),
        dbc.NavItem(
            dbc.NavLink(
                "Upload Files",
                href="/dashboard/upload",
                class_name="py-1 px-4 rounded-pill",
            )
        ),
    ],
    pills=True,
)

_nav_upload_files = dbc.Nav(
    [
        html.A(
            html.I(className="fa fa-pie-chart fa-2xl py-3 me-4"),
            href="/dashbord",
        ),
        dbc.NavItem(
            dbc.NavLink(
                "Dashboard",
                href="/dashboard",
                class_name="py-1 px-4 me-2 rounded-pill",
            )
        ),
        dbc.NavItem(
            dbc.NavLink(
                "Upload Files",
                href="/dashboard/upload",
                active=True,
                class_name="py-1 px-4 rounded-pill",
            )
        ),
    ],
    pills=True,
)

top_dashboard = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(_nav_dashboard, width=6),
            ],
            justify="between",
            align="center",
        ),
    ],
    fluid=True,
    class_name="py-2",
    id="navbar",
)

top_upload_files = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(_nav_upload_files, width=6),
            ],
            justify="between",
            align="center",
        ),
    ],
    fluid=True,
    class_name="py-2",
    id="navbar",
)
