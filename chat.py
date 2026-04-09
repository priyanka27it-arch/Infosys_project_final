import reflex as rx
from components.navbar import navbar
from components.footer import footer
from state.chat_state import ChatState


def chat():
    return rx.vstack(
        navbar(),
        rx.container(
            rx.heading("Document Chat", size="2xl", mt="8"),
            rx.text("Ask a question and receive answers grounded in uploaded documents.", color="gray.600", mb="4"),
            rx.hstack(
                rx.input(
                    placeholder="Type your question here...",
                    value=ChatState.question,
                    on_change=ChatState.set_question,
                    flex=1,
                    minWidth="60%",
                ),
                rx.button(
                    "Ask",
                    color_scheme="blue",
                    on_click=ChatState.ask,
                    is_loading=ChatState.is_loading,
                ),
                spacing="10px",
            ),
            rx.box(
                rx.heading("Conversation History", size="lg", mt="6"),
                rx.vstack(
                    *[
                        rx.box(
                            rx.text(f"Q: {entry['question']}", fontWeight="bold"),
                            rx.text(f"A: {entry['answer']}", mt="2"),
                            rx.text("Sources: " + ", ".join(entry["sources"]), mt="2", fontSize="sm", color="gray.500"),
                            p="16px",
                            bg="gray.100",
                            borderRadius="md",
                            boxShadow="sm",
                            width="100%",
                        )
                        for entry in ChatState.history[::-1]
                    ]
                ) if ChatState.history else rx.text("No questions asked yet."),
                mt="4",
            ),
            maxW="container.lg",
            p="24px",
        ),
        footer(),
        spacing="0",
        width="100%",
    )
