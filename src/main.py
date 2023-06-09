import datetime
from classes import User, Conversation, Summary, UserMetrics
from flask import Flask, render_template, request, jsonify
from chatgpt import query
import json
from ml import compute_cluster


app = Flask(__name__)


@app.route("/")
def root():
    # For the sake of example, use static information to inflate the template.
    # This will be replaced with real information in later steps.
    dummy_times = [
        datetime.datetime(2018, 1, 1, 10, 0, 0),
        datetime.datetime(2018, 1, 2, 10, 30, 0),
        datetime.datetime(2018, 1, 3, 11, 0, 0),
    ]

    return render_template("index.html", times=dummy_times)


@app.route("/moderate", methods=["GET"])
def moderate():
    # For the sake of example, use static information to inflate the template.
    # This will be replaced with real information in later steps.
    return render_template("chat.html")


@app.route("/chat", methods=["GET"])  # Front end
def get_chat() -> list[str]:
    session_id = request.args.get("session_id")

    with open("../db/chats.json", "r") as f:
        chat_data = json.load(f)
    return chat_data[session_id]["chat"]


@app.route("/users", methods=["GET"])  # Front end
def get_users() -> list[User]:
    session_id = request.args.get("session_id")

    with open("../db/users.json", "r") as f:
        user_data = json.load(f)
    return user_data[session_id]["users"]


@app.route("/summary", methods=["POST"])  # Front end
def get_summary() -> Summary:
    data = request.get_json()
    messages: list[int] = data["messages"]
    users: list[str] = data["users"]
    req = query(messages, [User(**u) for u in users])
    return req.json()


@app.route("/mlfeats", methods=["GET"])  # Front end
def get_mlfeats() -> list[User]:
    session_id = request.args.get("session_id")

    with open("../db/mlfeats.json", "r") as f:
        mlfs_data = json.load(f)
    return mlfs_data[session_id]['mlfs']


@app.route("/mlcluster", methods=["POST"])  # Front end
def get_mlcluster() -> list[User]:
    mlfs = request.get_json()["mlfs"]
    res = compute_cluster(mlfs)
    return {'cluster': res }


@app.route("/user_metrics", methods=["GET"])  # Front end
def get_user_metrics() -> list[UserMetrics]:
    session_id: int = request.args.get("session_id")
    
    with open("../db/details.json", "r") as f:
        user_detail = json.load(f)
    return user_detail[session_id]["details"]


if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host="127.0.0.1", port=8080, debug=True)
