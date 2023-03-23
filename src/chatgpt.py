import openai
import os
from dotenv import load_dotenv
import requests
from classes import Prompt, User

load_dotenv()


def query(messages: list[str], users: list[User]):
    prompt = make_prompt(messages, users)
    print(prompt)
    openai.api_key = os.getenv("OPENAI_API_KEY")
    max_tokens = int(os.getenv("OPENAI_MAX_TOKENS"))

    headers = {
        "content-type": "application/json",
        "Authorization": f"Bearer {openai.api_key}",
    }

    data = {
        "model": "text-davinci-003",
        "prompt": prompt,
        "max_tokens": max_tokens,
        "temperature": 0,
    }

    req = requests.post(
        url="https://api.openai.com/v1/completions",
        json=data,
        headers=headers,
        timeout=10,
    )

    return req


def make_prompt(messages: list[str], users: list[User]) -> Prompt:
    l1 = f"This is conversation between {', '.join([user.username for user in users])} as follows:"
    l2 = "{}".format("\n".join(messages))
    l3 = "Please summarize the above conversation in 100 words or less."
    l4 = "In addition, please give a sentiment score from 0 (negative) to 10 (positive)."
    l5 = "Lastly, for each player, assign a score from 0 to 10 corresponding to his/her level of aggresiveness."
    return "\n\n".join([l1, l2, l3, l4, l5])


if __name__ == "__main__":
    messages = [
        "player1: why no dragon",
        "player2: screw you i use ground troop",
        "player3: relax guys",
        "player1: do you even know how to play",
        "player2: i am better than you",
    ]
    user1 = User("player1", 1, 1)
    user2 = User("player2", 1, 1)
    user3 = User("player3", 1, 1)
    players = [user1, user2, user3]
    prompt = make_prompt(messages, players)
    print(prompt)

    req = query(messages, players)
    print(req.json())
