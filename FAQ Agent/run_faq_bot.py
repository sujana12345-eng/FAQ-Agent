import re

INTENTS = [
    ("greet", [r"\bhi\b", r"\bhello\b", r"\bhey\b"], "Hello! I can help with internship FAQs. How can I help you today?"),
    ("goodbye", [r"\bbye\b", r"\bgoodbye\b", r"see you"], "Goodbye — feel free to ask more questions anytime!"),
    ("ask_duration", [r"how long", r"duration", r"weeks", r"months"], "Internship durations typically range from 8 to 12 weeks, but this depends on the program."),
    ("ask_stipend", [r"stipend", r"paid", r"compensation", r"how much do interns"], "Many internships offer stipends; amounts vary. Typical monthly stipends are between $500-$2500 depending on location and company."),
    ("ask_requirements", [r"requirements", r"eligible", r"do I need to be a student", r"skills are required"], "Typical requirements: enrolled student (or recent graduate), relevant coursework or projects, resume, and sometimes a cover letter or portfolio."),
    ("ask_deadline", [r"deadline", r"when is the application", r"when should I submit"], "Application deadlines vary by program; common cycles are spring (Jan-Mar) and summer (Feb-May). Check the program page for exact dates."),
    ("ask_remote", [r"remote", r"work from home", r"work remotely", r"remote work"], "Some internships allow remote work while others require on-site presence. The posting will indicate remote, hybrid, or on-site."),
    ("ask_roles", [r"roles", r"positions", r"engineering", r"data science", r"design"], "Intern roles often include software engineering, data science, product, design, and marketing. Which area interests you?"),
    ("thanks", [r"thank", r"thanks", r"appreciate"], "You're welcome — happy to help!"),
]

DEFAULT = "Sorry, I didn't understand. Can you rephrase or ask a different question about internships?"


def predict_intent(message: str):
    text = message.lower()
    for intent, patterns, _ in INTENTS:
        for p in patterns:
            if re.search(p, text):
                return intent
    return None


def get_response(intent: str):
    if not intent:
        return DEFAULT
    for i, _, response in INTENTS:
        if i == intent:
            return response
    return DEFAULT


def run_samples():
    samples = [
        "Hi there",
        "How long is the internship?",
        "Do interns get paid?",
        "What are the requirements to apply?",
        "Is the internship remote?",
        "When is the application deadline?",
        "What roles are available?",
        "Thanks for the help",
        "Bye",
        "Can I bring my pet to work?",
    ]

    print("Running simple FAQ bot simulation.\n")
    for s in samples:
        intent = predict_intent(s)
        resp = get_response(intent)
        print(f"User: {s}")
        print(f"Predicted intent: {intent or 'none'}")
        print(f"Bot: {resp}\n")


def run_interactive():
    print("Interactive FAQ bot. Type 'exit' or 'quit' to stop.")
    while True:
        try:
            user = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break
        if not user:
            continue
        if user.lower() in ("exit", "quit"):
            print("Goodbye — feel free to ask more questions anytime!")
            break
        intent = predict_intent(user)
        resp = get_response(intent)
        print(f"Bot: {resp}\n")


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        run_interactive()
    else:
        run_samples()
