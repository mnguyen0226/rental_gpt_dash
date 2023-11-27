# dash imports
import dash
from dash import html
from dash import Input
from dash import Output
from dash import dcc
import dash_bootstrap_components as dbc

# file imports
from maindash import my_app


#######################################
# Layout
#######################################
def analysis_layout():
    layout = html.Div(
        [
            # image
            html.Div(
                [
                    html.Div(
                        [
                            html.Img(
                                src="https://images.unsplash.com/photo-1534477675274-cd511de4be22?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
                                style={
                                    "width": "100%",
                                    "height": "auto",
                                    "position": "relative",
                                },
                            ),
                        ],
                        style={
                            "height": "300px",
                            "overflow": "hidden",
                            "position": "relative",
                        },
                    ),
                    html.H1(
                        "RentGPT",
                        style={
                            "position": "absolute",
                            "top": "80%",
                            "left": "50%",
                            "transform": "translate(-45%, -50%)",
                            "color": "white",
                            "text-align": "left",
                            "width": "100%",
                        },
                    ),
                ],
                style={
                    "position": "relative",
                    "text-align": "center",
                    "color": "white",
                },
            ),
            # tab
            html.Div(
                style={"display": "flex"},
                children=[
                    html.Div(
                        [
                            dbc.Tabs(
                                id="analysis_selected_tab",
                                children=[
                                    dbc.Tab(
                                        label="Line Plot",
                                        tab_id="analysis_line",
                                    ),
                                    dbc.Tab(
                                        label="Bar Plot 1",
                                        tab_id="analysis_bar_1",
                                    ),
                                    dbc.Tab(
                                        label="Bar Plot 2",
                                        tab_id="analysis_bar_2",
                                    ),
                                    dbc.Tab(
                                        label="Count Plot 1",
                                        tab_id="analysis_count_1",
                                    ),
                                    dbc.Tab(
                                        label="Count Plot 2",
                                        tab_id="analysis_count_2",
                                    ),
                                    dbc.Tab(
                                        label="Count Plot 3",
                                        tab_id="analysis_count_3",
                                    ),
                                    dbc.Tab(
                                        label="Count Plot 4",
                                        tab_id="analysis_count_4",
                                    ),
                                    dbc.Tab(
                                        label="Count Plot 5",
                                        tab_id="analysis_count_5",
                                    ),
                                    dbc.Tab(
                                        label="Count Plot 6",
                                        tab_id="analysis_count_6",
                                    ),
                                    dbc.Tab(
                                        label="Pie Chart",
                                        tab_id="analysis_pie",
                                    ),
                                    dbc.Tab(
                                        label="Dist Plot",
                                        tab_id="analysis_dist",
                                    ),
                                    dbc.Tab(
                                        label="Pair Plot",
                                        tab_id="analysis_pair",
                                    ),
                                    dbc.Tab(
                                        label="Heatmap",
                                        tab_id="analysis_heatmap",
                                    ),
                                    dbc.Tab(
                                        label="Histogram KDE Plot",
                                        tab_id="analysis_hist_kde",
                                    ),
                                    dbc.Tab(
                                        label="QQ Plot",
                                        tab_id="analysis_qq",
                                    ),
                                    dbc.Tab(
                                        label="KDE Plot",
                                        tab_id="analysis_kde",
                                    ),
                                    dbc.Tab(
                                        label="Reg Plot 1",
                                        tab_id="analysis_reg_1",
                                    ),
                                    dbc.Tab(
                                        label="Reg Plot 2",
                                        tab_id="analysis_reg_2",
                                    ),
                                    dbc.Tab(
                                        label="Reg Plot 3",
                                        tab_id="analysis_reg_3",
                                    ),
                                    dbc.Tab(
                                        label="Area Plot",
                                        tab_id="analysis_area",
                                    ),
                                    dbc.Tab(
                                        label="Violin Plot",
                                        tab_id="analysis_violin",
                                    ),
                                    dbc.Tab(
                                        label="Joint Plot 1",
                                        tab_id="analysis_joint_1",
                                    ),
                                    dbc.Tab(
                                        label="Joint Plot 2",
                                        tab_id="analysis_joint_2",
                                    ),
                                    dbc.Tab(
                                        label="Rug Plot",
                                        tab_id="analysis_rug",
                                    ),
                                    dbc.Tab(
                                        label="3D Plot",
                                        tab_id="analysis_3d",
                                    ),
                                    dbc.Tab(
                                        label="Contour Plot",
                                        tab_id="analysis_contour",
                                    ),
                                    dbc.Tab(
                                        label="3D Contour Plot",
                                        tab_id="analysis_3d_contour",
                                    ),
                                    dbc.Tab(
                                        label="Cluster Plot",
                                        tab_id="analysis_cluster",
                                    ),
                                    dbc.Tab(
                                        label="Hexbin Plot",
                                        tab_id="analysis_hexbin",
                                    ),
                                    dbc.Tab(
                                        label="Strip Plot 1",
                                        tab_id="analysis_strip_1",
                                    ),
                                    dbc.Tab(
                                        label="Strip Plot 2",
                                        tab_id="analysis_strip_2",
                                    ),
                                    dbc.Tab(
                                        label="Strip Plot 3",
                                        tab_id="analysis_strip_3",
                                    ),
                                    dbc.Tab(
                                        label="Swarm Plot",
                                        tab_id="analysis_swarm",
                                    ),
                                    dbc.Tab(
                                        label="Story Plot 1",
                                        tab_id="analysis_story_1",
                                    ),
                                    dbc.Tab(
                                        label="Story Plot 2",
                                        tab_id="analysis_story_2",
                                    ),
                                    dbc.Tab(
                                        label="Story Plot 3",
                                        tab_id="analysis_story_3",
                                    ),
                                    dbc.Tab(
                                        label="Story Plot",
                                        tab_id="analysis_story_4",
                                    ),
                                ],
                                active_tab="analysis_line",
                            ),
                        ]
                    ),
                ],
            ),
            # content: analysis & plot
            html.Div(
                style={"display": "flex"},
                children=[
                    html.Div(
                        style={
                            "width": "50%",
                            "padding": "20px",
                        },
                        children=[
                            html.Div(id="analysis_tab_content_layout"),
                        ],
                    ),
                    html.Div(
                        style={
                            "width": "50%",
                            "padding": "20px",
                        },
                        children=[
                            html.Div(id="analysis_tab_plot_layout"),
                        ],
                    ),
                ],
            ),
        ]
    )

    return layout


#######################################
# Callbacks
#######################################
@my_app.callback(
    [
        Output(component_id="analysis_tab_content_layout", component_property="children"),
        Output(component_id="analysis_tab_plot_layout", component_property="children"),
    ],
    [Input(component_id="analysis_selected_tab", component_property="active_tab")],
)
def render_tab_1(tab_choice):
    """Renders the selected subtab's layout

    Args:
        tab_choice (str): selected subtab

    Returns:
        selected subtab's layout
    """
    if tab_choice == "theory_tab":
        return (html.P("theory_tab"), html.P("theory_tab"))
    if tab_choice == "pg_tab":
        return (html.P("pg_tab"), html.P("pg_tab"))
    if tab_choice == "code_tab":
        return (html.P("code_tab"), html.P("code_tab"))
    if tab_choice == "theory_tab":
        return (html.P("theory_tab"), html.P("theory_tab"))
    if tab_choice == "pg_tab":
        return (html.P("pg_tab"), html.P("pg_tab"))
    if tab_choice == "code_tab":
        return (html.P("code_tab"), html.P("code_tab"))
    if tab_choice == "theory_tab":
        return (html.P("theory_tab"), html.P("theory_tab"))
    if tab_choice == "pg_tab":
        return (html.P("pg_tab"), html.P("pg_tab"))
    if tab_choice == "code_tab":
        return (html.P("code_tab"), html.P("code_tab"))
    if tab_choice == "theory_tab":
        return (html.P("theory_tab"), html.P("theory_tab"))
    if tab_choice == "pg_tab":
        return (html.P("pg_tab"), html.P("pg_tab"))
    if tab_choice == "code_tab":
        return (html.P("code_tab"), html.P("code_tab"))
    if tab_choice == "theory_tab":
        return (html.P("theory_tab"), html.P("theory_tab"))
    if tab_choice == "pg_tab":
        return (html.P("pg_tab"), html.P("pg_tab"))
    if tab_choice == "code_tab":
        return (html.P("code_tab"), html.P("code_tab"))
    if tab_choice == "theory_tab":
        return (html.P("theory_tab"), html.P("theory_tab"))
    if tab_choice == "pg_tab":
        return (html.P("pg_tab"), html.P("pg_tab"))
    if tab_choice == "code_tab":
        return (html.P("code_tab"), html.P("code_tab"))