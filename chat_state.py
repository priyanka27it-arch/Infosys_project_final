import reflex as rx
from backend.rag import generate_answer


class ChatState(rx.State):
    question: str = ""
    is_loading: bool = False
    history: list[dict] = []

    def set_question(self, value: str):
        self.question = value

    def ask(self):
        if self.question.strip() == "":
            return
        self.is_loading = True
        result = generate_answer(self.question.strip())
        self.history.append(
            {
                "question": self.question.strip(),
                "answer": result.get("answer", "No answer available."),
                "sources": result.get("sources", []),
            }
        )
        self.question = ""
        self.is_loading = False
