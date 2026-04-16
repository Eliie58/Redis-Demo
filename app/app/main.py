from flask import Flask, request, jsonify, Response, render_template
import json
import time
import threading

import redis_api as api

app = Flask(__name__)

# Connect once
api.connect()

# ─────────────────────────────────────────────
# SPEAKERS
# ─────────────────────────────────────────────

@app.route("/speakers", methods=["POST"])
def create_speaker():
    data = request.json
    api.register_speaker(
        data["id"],
        data["name"],
        data["topic"],
        data["bio"],
        data["handle"]
    )
    return jsonify({"status": "ok"})


@app.route("/speakers/<id>", methods=["GET"])
def get_speaker(id):
    speaker = api.get_speaker(id)
    if not speaker:
        return jsonify({"error": "not found"}), 404
    return jsonify(speaker)

@app.route("/speakers/topic/<topic>", methods=["GET"])
def get_speakers(topic):
    speakers = api.get_speakers(topic)
    if not speakers:
        return jsonify({"error": "not found"}), 404
    return jsonify(speakers)


# ─────────────────────────────────────────────
# SESSIONS
# ─────────────────────────────────────────────

@app.route("/sessions", methods=["POST"])
def add_session():
    data = request.json
    api.add_session(
        data["session_id"],
        data["title"],
        data["speaker_id"],
        data["start_ts"],
        data["room"]
    )
    return jsonify({"status": "ok"})


@app.route("/sessions/upcoming")
def upcoming_sessions():
    return jsonify(api.get_upcoming_sessions())


# ─────────────────────────────────────────────
# QUESTIONS
# ─────────────────────────────────────────────

@app.route("/questions", methods=["POST"])
def submit_question():
    data = request.json
    api.submit_question(
        data["session_id"],
        data["attendee"],
        data["question"]
    )
    return jsonify({"status": "queued"})


@app.route("/questions/<session_id>/next")
def next_question(session_id):
    q = api.pop_next_question(session_id)
    return jsonify(q)


# ─────────────────────────────────────────────
# LEADERBOARD
# ─────────────────────────────────────────────

@app.route("/leaderboard/award", methods=["POST"])
def award():
    data = request.json
    score = api.award_points(data["attendee"], data["points"])
    return jsonify({"score": score})


@app.route("/leaderboard")
def leaderboard():
    return jsonify(api.get_leaderboard())


# ─────────────────────────────────────────────
# ANNOUNCEMENTS (PUB/SUB)
# ─────────────────────────────────────────────

@app.route("/announce", methods=["POST"])
def announce():
    data = request.json
    count = api.publish_announcement(data["channel"], data["message"])
    return jsonify({"delivered": count})


@app.route("/announcements")
def history():
    return jsonify(api.get_recent_announcements())


# 🔴 SSE STREAM (REAL-TIME)
@app.route("/stream/<channel>")
def stream(channel):

    def event_stream():
        for message in api.listen_to_channel(channel):
            if message["type"] == "message":
                yield f"data: {message['data']}\n\n"

    return Response(event_stream(), mimetype="text/event-stream")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/speakers")
def speakers():
    return render_template("speakers.html")

@app.route("/sessions")
def sessions():
    return render_template("sessions.html")

@app.route("/questions")
def questions():
    return render_template("questions.html")

@app.route("/leaderboard-page")
def leaderboard_page():
    return render_template("leaderboard.html")

@app.route("/announcements-page")
def announcements_page():
    return render_template("announcements.html")
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("Starting")
    app.run(debug=True, threaded=True, host="0.0.0.0")