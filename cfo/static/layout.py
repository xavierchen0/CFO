from dash import html
import dash_bootstrap_components as dbc

nav = dbc.Nav(
    [
        html.A(html.I(className="fa fa-pie-chart fa-2xl py-3 me-4"), href=""),
        dbc.NavItem(
            dbc.NavLink(
                "Dashboard",
                href="",
                active=True,
                class_name="py-1 px-4 me-2 rounded-pill",
            )
        ),
        dbc.NavItem(
            dbc.NavLink(
                "Upload Files",
                href="",
                class_name="py-1 px-4 rounded-pill",
            )
        ),
    ],
    pills=True,
)

layout = [
    # Top of page
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(nav, width=6),
                ],
                justify="between",
                align="center",
            ),
        ],
        # fluid=True,
        fluid=True,
        class_name="py-2",
        id="navbar",
    )
]
