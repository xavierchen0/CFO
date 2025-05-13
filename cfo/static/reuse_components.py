from dash import html
import dash_bootstrap_components as dbc

_nav = dbc.Nav(
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

top = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(_nav, width=6),
            ],
            justify="between",
            align="center",
        ),
    ],
    fluid=True,
    class_name="py-2",
    id="navbar",
)
