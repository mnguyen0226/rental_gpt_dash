# dash imports
import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from hugchat import hugchat
from hugchat.login import Login
import time

# this is not recommended, usually, the account will be stored in .env file
HARDCODED_EMAIL = "mnguyen0226.swetest@gmail.com"
HARDCODED_PASSWORD = "Rentalgpt123!"

# file imports
from maindash import my_app
from utils.file_operation import read_file_as_str


def chatbot_content():
    layout = html.Div(
        [
            html.Div([html.H3("🧐 Development")]),
            dcc.Markdown(
                children=read_file_as_str("./utils/markdown/virtual_assistant/va.md"),
                mathjax=True,
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
                    dbc.Row(
                        dbc.Col(
                            html.Div(
                                id="chat_bot_chat_area",
                                # className="chat-area",
                                style={
                                    "overflow-y": "auto",
                                    "max-height": "calc(70vh - 120px)",
                                    "margin-bottom": "60px",
                                },
                            ),
                            # width=12
                        )
                    ),
                    dcc.Loading(
                        # id="chat_bot_loading",
                        type="default",
                        children=html.Div(id="chat_bot_loading_output"),
                    ),
                    html.Br(),
                    html.Br(),
                    dbc.Row(
                        [
                            dbc.InputGroup(
                                [
                                    dbc.Input(
                                        id="chat_bot_message_input",
                                        placeholder="Message RentalGPT...",
                                        type="text",
                                        className="me-2",
                                    ),
                                    dbc.Button(
                                        "Send",
                                        id="chat_bot_send_button",
                                        n_clicks=0,
                                        color="success",
                                        className="me-2",
                                    ),
                                    dbc.Button(
                                        "Reset",
                                        id="chat_bot_reset_button",
                                        n_clicks=0,
                                        color="warning",
                                    ),
                                ],
                                className="mb-3",
                            ),
                        ],
                        # className="fixed-bottom",
                    ),
                ],
                fluid=True,
                # style={"height": "100vh"},
            )
        ]
    )


@my_app.callback(
    [
        Output("chat_bot_chat_area", "children"),
        Output("chat_bot_message_input", "value"),
        Output("chat_bot_loading_output", "children"),
    ],
    [
        Input("chat_bot_send_button", "n_clicks"),
        Input("chat_bot_reset_button", "n_clicks"),
    ],
    [State("chat_bot_message_input", "value"), State("chat_bot_chat_area", "children")],
    prevent_initial_call=True,
)
def update_chat(send_n_clicks, reset_n_clicks, message, chat_history):
    # reference: https://github.com/Soulter/hugging-chat-api
    ctx = dash.callback_context
    if not ctx.triggered:
        button_id = "No clicks yet"
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    # clear message and chat area
    if button_id == "chat_bot_reset_button":
        return [], "", None

    if message:
        # simulate loading time
        time.sleep(1)

        # call the function to handle HugChat logic
        response = handle_hugchat_logic(HARDCODED_EMAIL, HARDCODED_PASSWORD, message)

        # prepare chat messages for display
        new_message = create_message_div(f"You: {message}", sender="user")
        response_message = create_message_div(f"RentalGPT: {response}", sender="bot")

        # update chat history
        updated_history = chat_history or []
        updated_history.extend([new_message, response_message])

        # clear message input after sending
        return updated_history, "", None
    return chat_history, "", None


def create_message_div(message, sender="user"):
    """Create a styled message div."""
    return dbc.Card(
        dbc.CardBody(message),
        className=f"mb-2 {'text-light' if sender=='user' else 'text-dark'} {'bg-primary' if sender=='user' else 'bg-secondary'}",
        style={"width": "75%", "margin-left": "auto" if sender == "user" else "0"},
    )


def handle_hugchat_logic(email, password, user_message):
    # reference: https://github.com/Soulter/hugging-chat-api
    try:
        # perform login to HugChat
        login = Login(email, password)
        cookies = login.login()

        # create a chatbot instance with the obtained cookies
        chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

        # prepare the prompt for the chatbot
        prompt = f"User: {user_message}\n"

        # get the response from the chatbot
        response = chatbot.chat(prompt)

        return response

    # handle exceptions (like login failure, API errors, etc.)
    except Exception as e:
        # print("Error in HugChat logic:", e)
        return "Sorry, I couldn't process your request. Probably because Minh's credential is temporarily expired or wrong! Please let him know via mnguyen0226@vt.edu"


def chatbot_info():
    return (chatbot_content(), chatbot_layout())
