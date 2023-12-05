import dash
from dash import html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
from hugchat import hugchat
from hugchat.login import Login
import time

# hardcoded credentials (not recommended for production)
HARDCODED_EMAIL = "mnguyen0226@vt.edu"
HARDCODED_PASSWORD = "Minh123456!!!"

# initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# define the layout of the app
app.layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(html.H1("🤗🦙💬 Meta's LLaMA", className="text-center"), width=12)
        ),
        html.Br(),
        dbc.Row(
            dbc.Col(
                html.Div(
                    id="chat-area",
                    className="chat-area",
                    style={
                        "overflow-y": "auto",
                        "max-height": "calc(100vh - 120px)",
                        "margin-bottom": "60px",
                    },
                ),
                width=12,
            )
        ),
        dbc.Row(
            [
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("Enter message:"),
                        dbc.Input(
                            id="message-input",
                            placeholder="Write LlaMA...",
                            type="text",
                        ),
                        dbc.InputGroupText(
                            dbc.Button("Send", id="send-button", n_clicks=0)
                        ),
                        dbc.InputGroupText(
                            dbc.Button("Reset", id="reset-button", n_clicks=0)
                        ),
                    ],
                    className="mb-3",
                ),
            ],
            className="fixed-bottom",
        ),
        dcc.Loading(
            id="loading", type="default", children=html.Div(id="loading-output")
        ),
    ],
    fluid=True,
    style={"height": "100vh"},
)


@app.callback(
    [
        Output("chat-area", "children"),
        Output("message-input", "value"),
        Output("loading-output", "children"),
    ],
    [Input("send-button", "n_clicks"), Input("reset-button", "n_clicks")],
    [State("message-input", "value"), State("chat-area", "children")],
    prevent_initial_call=True,
)
def update_chat(send_n_clicks, reset_n_clicks, message, chat_history):
    ctx = dash.callback_context
    if not ctx.triggered:
        button_id = "No clicks yet"
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    # clear chat area and message input
    if button_id == "reset-button":
        return [], "", None

    if message:
        # simulate loading time (not needed)
        time.sleep(1)

        # call the function to handle HugChat logic
        response = handle_hugchat_logic(HARDCODED_EMAIL, HARDCODED_PASSWORD, message)

        # prepare chat messages for display
        new_message = create_message_div(f"You: {message}", sender="user")
        response_message = create_message_div(f"Assistant: {response}", sender="bot")

        # update chat history
        updated_history = chat_history or []
        updated_history.extend([new_message, response_message])

        return updated_history, "", None  # Clear message input after sending
    return chat_history, "", None


def create_message_div(message, sender="user"):
    return dbc.Card(
        dbc.CardBody(message),
        className=f"mb-2 text-white {'bg-primary' if sender=='user' else 'bg-secondary'}",
        style={"width": "75%", "margin-left": "auto" if sender == "user" else "0"},
    )


def handle_hugchat_logic(email, password, user_message):
    try:
        # perform login to HugChat
        login = Login(email, password)
        cookies = login.login()

        # create a chatbot instance with the obtained cookies
        chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

        # prepare the prompt for the chatbot
        prompt = f"User: {user_message}\nAssistant:"

        # get the response from the chatbot
        response = chatbot.chat(prompt)

        return response

    # handle exceptions (like login failure, API errors, etc.)
    except Exception as e:
        print("Error in HugChat logic:", e)
        return "Sorry, I couldn't process your request. Probably because the author's credential is expired or wrong!"


# run the app
if __name__ == "__main__":
    app.run_server(debug=True)
