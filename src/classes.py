from dataclasses import dataclass


@dataclass
class User:
    username: str
    user_id: str
    alliance_id: str

    # Add other metrics here

    def get_dummy(self):
        return self.dummy

    def get_user_id(self):
        return self.user_id

@dataclass
class UserMetrics:
    user_id: str
    dummy: str  # For testing


@dataclass
class Summary:
    messages: list[str]
    sentiment_score: int
    sentiment_comment: str


@dataclass
class Conversation:
    session_id: str
    users: list[User]
    messages: list[str]

    def get_messages(self):
        return self.messages

    def get_users(self):
        return self.users


@dataclass
class Prompt:
    players: list[str]
    conversation: list[str]


@dataclass
class Chat:
    messages: list[str]
    timestamp: list[str]

