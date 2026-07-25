# dash imports
from dash import html
import dash_bootstrap_components as dbc


def chatbot_content():
    layout = html.Div(
        [
            html.Div([html.H3("🧐 Development")]),
            html.P(
                "The general idea of the virtual assistant is that the LLM will learn "
                "the provided apartment rental dataset to understand the context of the "
                "application. Through conversation with the user, the LLM will predict "
                "the features of the preferred apartment (such as number of bedrooms, "
                "bathrooms, etc.) to filter and recommend the top apartments to the user."
            ),
        ]
    )
    return layout


def chatbot_layout():
    return html.Div(
        [
            dbc.Container(
                [
                    dbc.Row(
                        dbc.Col(html.H3("🤗🦙💬 Meta's LLaMA", className="text-center"))
                    ),
                    html.Br(),
                    dbc.Alert(
                        "This feature is no longer supported.",
                        color="secondary",
                        className="text-center",
                    ),
                ],
                fluid=True,
            )
        ]
    )


def chatbot_info():
    return (chatbot_content(), chatbot_layout())
