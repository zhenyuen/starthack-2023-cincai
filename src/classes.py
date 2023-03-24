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
    ...


@dataclass
class MLFeatures:
    risk: float
    is_family_friendly: float
    GENERAL_RISK: float
    BULLYING: float
    VIOLENCE: float
    RELATIONSHIP_SEXUAL_CONTENT: float
    VULGARITY: float
    DRUGS_ALCOHOL: float
    IN_APP: float
    ALARM: float
    FRAUD: float
    HATE_SPEECH: float
    RELIGIOUS: float
    WEBSITE: float
    CHILD_GROOMING: float
    PUBLIC_THREAT: float
    EXTREMISM: float
    SUBVERSIVE: float
    SENTIMENT: float
    POLITICS: float
    chat_id: int
    session_count: int
    session_duration: int
    transaction_count: int
    revenue: int
    account_state: int
    level: int
    session_count_today: int
    session_duration_today: int
    transaction_count_today: int
    revenue_today: float




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
    risks: list[float]

