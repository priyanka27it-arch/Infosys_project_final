import reflex as rx


def hero_section():
    return rx.box(
        rx.vstack(
            rx.heading("RAG Application (Reflex + LangChain)" , size="2xl", fontWeight="extrabold"),
            rx.text("Upload your files, ask questions, and get grounded answers based only on your documents.", fontSize="lg", color="gray.300"),
            rx.hstack(
                rx.link(rx.button("Get Started", colorScheme="brand"), href="/upload"),
                rx.link(rx.button("Start Chat", variant="outline"), href="/chat"),
                spacing="12px",
            ),
            spacing="20px",
            alignItems="flex-start",
        ),
        p="24px",
        bg="blue.900",
        borderRadius="lg",
        color="white",
        shadow="xl",
        width="100%",
        maxW="container.xl",
    )
