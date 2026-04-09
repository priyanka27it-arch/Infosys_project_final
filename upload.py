import reflex as rx
from components.navbar import navbar
from components.footer import footer
from state.upload_state import UploadState


def upload():
    return rx.vstack(
        navbar(),
        rx.container(
            rx.heading("Upload Documents", size="2xl", mt="8"),
            rx.text("Enter local file paths (comma-separated). This loads PDF/TXT content into RAG context.", color="gray.600", mb="4"),
            rx.textarea(
                placeholder="C:/docs/manual.txt, C:/docs/guide.pdf",
                value=UploadState.file_paths,
                on_change=UploadState.set_file_paths,
                rows=4,
                width="100%",
            ),
            rx.button(
                "Load Documents",
                color_scheme="blue",
                mt="3",
                on_click=UploadState.add_files,
            ),
            rx.text(UploadState.status, mt="3"),
            rx.box(
                rx.heading("Loaded Documents", size="md"),
                rx.unordered_list(*[rx.list_item(doc) for doc in UploadState.files]) if UploadState.files else rx.text("No documents loaded yet."),
                mt="4",
            ),
            maxW="container.lg",
            p="24px",
        ),
        footer(),
        spacing="0",
        width="100%",
    )

