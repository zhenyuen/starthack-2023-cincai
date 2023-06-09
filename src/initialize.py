import json
from classes import User, Chat, MLFeatures, UserMetrics
from itertools import count
import csv
import os
from dotenv import load_dotenv


load_dotenv()

c = count()


def create_session(chat: Chat, users: list[User], mlfeats: list[MLFeatures], details: list[UserMetrics]):
    session_id = next(c)
    try:
        with open("../db/chats.json", "r") as f:
            chats_data = json.load(f)
    except:
        chats_data = dict()

    try:
        with open("../db/users.json", "r") as f:
            users_data = json.load(f)
    except:
        users_data = dict()

    try:
        with open("../db/mlfeats.json", "r") as f:
            mlfeats_data = json.load(f)
    except:
        mlfeats_data = dict()

    try:
        with open("../db/details.json", "r") as f:
            details_data = json.load(f)
    except:
        details_data = dict()

    chats_data[session_id] = {"session_id": session_id, "chat": chat}

    users_data[session_id] = {
        "session_id": session_id,
        "users": [u.__dict__ for u in users],
    }

    mlfeats_data[session_id] = {
        "session_id": session_id,
        "mlfs": [mlf.__dict__ for mlf in mlfeats],
    }

    details_data[session_id] = {
        "session_id": session_id,
        "details": [det.__dict__ for det in details],
    }

    with open("../db/chats.json", "w") as f:
        json.dump(chats_data, f, indent=4)

    with open("../db/users.json", "w") as f:
        json.dump(users_data, f, indent=4)

    with open("../db/mlfeats.json", "w") as f:
        json.dump(mlfeats_data, f, indent=4)

    with open("../db/details.json", "w") as f:
        json.dump(details_data, f, indent=4)


def read_demo(f) -> list[Chat, list[User]]:
    max_sentences = int(os.getenv("MAX_SENTENCES"))
    unique_users = dict()
    messages = []
    users = []
    timestamps = []
    risks = []
    cc = count()
    lines = 0
    with open(f, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            lines += 1
            risk = row['risk']
            user_id = row["account_id"]
            alliance_id = row["alliance_id"]
            if user_id in unique_users:
                username = unique_users[user_id]
            else:
                username = "user{}".format(next(cc))
                unique_users[user_id] = username
                users.append(User(username, user_id, alliance_id))

            timestamp = row["timestamp"]
            message = {"username": username, "message": row["raw_message"]}
            messages.append(message)
            timestamps.append(timestamp)
            risks.append(risk)
            if lines == max_sentences: break
    chat = Chat(messages, timestamps, risks).__dict__
    
    return chat, users


def read_mlfeats(f) -> list[MLFeatures]:
    mlf = []
    with open(f, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            del row['']
            del row['chat_id']

            temp = MLFeatures(**row)
            mlf.append(temp)
    
    return mlf

def read_details(f) -> list[UserMetrics]:
    unique_users = dict()
    users = []
    lines = 0
    cc = count()
    with open(f, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            lines += 1
            risk_5 = row['past_risk_5']
            risk_6 = row['past_risk_6']
            risk_7 = row['past_risk_7']
            kick_out = row['past_kicked_out']
            user_id = row['account_id']
            if user_id not in unique_users:
                username = "user{}".format(next(cc))
                unique_users[user_id] = username
                users.append(UserMetrics(username, user_id, risk_5, risk_6, risk_7, kick_out))
    return users




if __name__ == "__main__":
    # messages = [
    #     "player1: why no dragon",
    #     "player2: screw you i use ground troop",
    #     "player3: relax guys",
    #     "player1: do you even know how to play",
    #     "player2: i am better than you",
    # ]
    # user1 = User("player1", 1, 1)
    # user2 = User("player2", 1, 1)
    # user3 = User("player3", 1, 1)
    # players = [user1, user2, user3]
    with open("../db/chats.json", "w") as f:
            json.dump({}, f, indent=4)

    with open("../db/users.json", "w") as f:
            json.dump({}, f, indent=4)

    with open("../db/details.json", "w") as f:
            json.dump({}, f, indent=4)

    # chat, users = read_demo('../db/demo1.csv')
    # create_session(chat, users)

    # chat, users = read_demo('../db/toxic2.csv')
    # create_session(chat, users)

    """
    chat, users = read_demo('../db/incident1_chathistory.csv')
    mlfeats = read_mlfeats('../db/incident1_accounts.csv')
    create_session(chat, users, mlfeats)
    """

    chat, users = read_demo('../db/incident2_chathistory.csv')
    mlfeats = read_mlfeats('../db/incident2_accounts.csv')
    details = read_details('../db/incident2_profile.csv')
    create_session(chat, users, mlfeats, details)

    
