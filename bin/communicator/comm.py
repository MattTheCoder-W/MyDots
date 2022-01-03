class Types:
    INFO = "!"
    ERROR = "-"
    SUCCESS = "+"
    QUESTION = "?"
    PROCESS = "*"

def show(info_type: str, content: str, end="\n"):
    print(f"[{info_type}] >> {content}", end=end)

