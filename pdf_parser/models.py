class Section:
    def __init__(self, text, section_id):
        self.text = text
        self.section_id = section_id
        self.tests = []
        self.question_str = ""

    def __str__(self):
        return f"{self.section_id} - {self.text}"


class Test:
    def __init__(self, question, test_id: int):
        self.section_text = ""
        self.question = question
        self.test_id = test_id
        self.correct_answer: int = None
        self.reference_number: str = None
        self.versions = []

    def __str__(self):
        return f"{self.test_id} - {self.question}"

    def to_dict(self):
        return {
            "question": f"{self.question}",
            "questionType": "text",
            "answerSelectionType": "single",
            "answers": [str(n) for n in self.versions],
            "correctAnswer": str(self.correct_answer + 1),
            "messageForCorrectAnswer": "სწორია.",
            "messageForIncorrectAnswer": "შეცდომაა, სცადეთ თავიდან.",
            "explanation": f"გამარტებᲐ, კონსტიტუციის მუხლი: {self.reference_number}",
            "point": "1"
        }


def build_tests(tests):
    return {
        "quizTitle": "აარჩევნო ადმინისტრაციის მოხელეთა სასერტიფიკაციო გამოცდის ტესტები",
        "quizSynopsis": """ცესკოს 2024 წლის 27 თებერვლის N16/2024
                  განკარგულება „საარჩევნო ადმინისტრაციის
                  მოხელეთა სერტიფიცირების საგამოცდო ტესტების
                  დამტკიცების შესახებ“ 2023 წლის 13 ივნისის
                  №136/2023 განკარგულებაში ცვლილებების შეტანის
                  შესახებ""",
        "nrOfQuestions": "25",
        "questions": [test.to_dict() for test in tests]
    }
