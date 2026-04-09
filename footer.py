import reflex as rx


def footer():
    return rx.box(
        rx.text("© 2026 RAG Project - Build with Reflex + LangChain", fontSize="sm"),
        rx.text("GitHub Copilot generated UI", fontSize="xs", color="gray.400"),
        bg="gray.900",
        color="gray.200",
        textAlign="center",
        px="20px",
        py="16px",
        mt="40px",
        width="100%",
    )
