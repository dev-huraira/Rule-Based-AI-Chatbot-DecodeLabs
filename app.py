from flask import Flask, request, jsonify, render_template
from decobot_project1 import (
    KNOWLEDGE_BASE,
    phase_process,
    get_time,
    get_date,
    get_joke,
    get_calc,
    EXIT_CMDS,
)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    clean_input = data["message"].lower().strip()

    if clean_input in EXIT_CMDS:
        return jsonify({"reply": "Goodbye! Session ended. 👋", "type": "exit"})

    session_stats = {"count": 0, "name": "User", "start": "N/A"}
    bot_response = phase_process(clean_input, session_stats)
    return jsonify({"reply": bot_response, "type": "response"})


if __name__ == "__main__":
    app.run(port=5000, debug=True)
