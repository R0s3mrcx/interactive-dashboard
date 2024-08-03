import reflex as rx
from reflex.style import toggle_color_mode
import pandas as pd
import plotly.graph_objects as go

df = pd.read_csv('STOCK_US_XNAS_AMD.csv')

class State(rx.State):
    month: list[str] = df['Month'].unique().tolist()
    selected_month: str
    plot: go.Figure = go.Figure(data=[
        go.Candlestick(
            x=df['Month'],
            open=df['Open'],
            low=df['High'],
            high=df['Low'],
            close=df['Close']
        )
    ])
    subtitle: str = "For the month of January(1/2/2024) To April(23/04/2024)"

    def set_month(self, value):
        self.selected_month = value
        filtered_df = df[df['Month'] == self.selected_month]
        self.subtitle = f"For the month of {self.selected_month}"
        self.plot = go.Figure(data=[
            go.Candlestick(
                x=filtered_df['Month'],
                open=filtered_df['Open'],
                low=filtered_df['Low'],
                high=filtered_df['High'],
                close=filtered_df['Close']
            )
        ])

    def reset_data(self):
        self.subtitle = "For the month of January(1/2/2024) To December(31/12/2024)"
        self.selected_month = ""
        self.plot = go.Figure(data=[
            go.Candlestick(
                x=df['Month'],
                open=df['Open'],
                low=df['Low'],
                high=df['High'],
                close=df['Close']
            )
        ])

def index():
    return rx.container(
        rx.center(rx.text("AMD Stock Data", font_size="3em")),
        rx.center(rx.text(State.subtitle, font_size="1em", font_style="italic")),
        rx.button(rx.color_mode.icon(), on_click=toggle_color_mode, margin_right="5px", color_scheme="cyan", margin_top="30px"),
        rx.button("Reset", on_click=State.reset_data, margin_right="5px", color_scheme="red", margin_top="30px"),
        rx.select.root(
            rx.select.trigger(placeholder="Select a Month", margin_top="30px"),
            rx.select.content(
                rx.select.group(
                    rx.foreach(
                        State.month,
                        lambda value: rx.select.item(value, value=value)
                    )
                )
            ),
            on_change=State.set_month,
            value=State.selected_month
        ),
        rx.plotly(data=State.plot, height='550px', width='60rem'),
    )

app = rx.App()
app.add_page(index)
app._compile()