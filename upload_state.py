import reflex as rx
from backend.rag import load_document


class UploadState(rx.State):
    status: str = ""
    files: list[str] = []
    file_paths: str = ""

    def set_file_paths(self, value: str):
        self.file_paths = value

    def add_files(self):
        raw = self.file_paths.strip()
        if not raw:
            self.status = "No file paths provided."
            return

        paths = [p.strip() for p in raw.split(",") if p.strip()]
        if not paths:
            self.status = "No valid file paths provided."
            return

        for path in paths:
            try:
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    text = f.read()
                name = path.split("/")[-1].split("\\")[-1]
                load_document(name, text)
                if name not in self.files:
                    self.files.append(name)
            except Exception as e:
                self.status = f"Failed loading {path}: {e}"
                return

        self.status = f"{len(paths)} file(s) uploaded successfully."
        self.file_paths = ""
