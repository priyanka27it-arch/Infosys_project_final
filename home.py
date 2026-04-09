import reflex as rx
from components.navbar import navbar
from components.hero import hero_section
from components.footer import footer


def home():
    return rx.vstack(
        navbar(),
        rx.container(
            hero_section(),
            rx.grid(
                rx.box(
                    rx.heading("Why RAG?", size="lg", color="blue.800"),
                    rx.unordered_list(
                        rx.list_item("Ground answers on your documents"),
                        rx.list_item("Avoid hallucinations"),
                        rx.list_item("Scalable architecture"),
                        rx.list_item("Keeping UI and backend cleanly separated"),
                    ),
                    p="20px",
                    bg="gray.50",
                    borderRadius="lg",
                    boxShadow="sm",
                ),
                rx.box(
                    rx.heading("Project Structure", size="lg", color="blue.800"),
                    rx.text("assets, components, pages, backend, state, documents"),
                    rx.text("Upload first, then chat with your data."),
                    p="20px",
                    bg="gray.50",
                    borderRadius="lg",
                    boxShadow="sm",
                ),
                columns="1",
                spacing="20px",
                mt="20px",
            ),
            maxW="container.xl",
            p="24px",
        ),
        footer(),
        spacing="0",
        width="100%",
    )
