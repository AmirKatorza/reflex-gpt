import reflex as rx
from reflex_gpt import ui
from .form import chat_form
from .state import ChatMessage, ChatState

def message_box(chat_message: ChatMessage):
    return rx.box(rx.text(chat_message.message))


def chat_page():
    return ui.base_layout(
        rx.vstack(
            rx.heading("Chat Here", size="9"),
            rx.box(
                rx.foreach(ChatState.messages, message_box),
                width = '100%'
            ),
            chat_form(),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo()
    )
