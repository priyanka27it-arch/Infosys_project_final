import reflex as rx


def navbar():
    return rx.box(
        rx.hstack(
            rx.link(rx.heading("RAG Document AI"), href="/", _hover={"textDecoration": "none"}),
            rx.spacer(),
            rx.link("Home", href="/", px="4", py="2", _hover={"textDecoration":"underline"}),
            rx.link("Upload", href="/upload", px="4", py="2", _hover={"textDecoration":"underline"}),
            rx.link("Chat", href="/chat", px="4", py="2", _hover={"textDecoration":"underline"}),
        ),
        bg="gray.800",
        color="white",
        px="20px",
        py="12px",
        width="100%",
        boxShadow="md",
        position="sticky",
        top="0",
        zIndex="overlay",
    )
