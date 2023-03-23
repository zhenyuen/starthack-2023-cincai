Design considerations:

1. GCP Firestore for DB
   1. User account
   2. Ongoing-chats
2. GCP Firebase for hosting
3. GCP Cloud run vs App Engine
   1. If serverless can use cloud run. BUT,
   2. I think the AI model must use App Engine, or even better perphaps vertex AI
   3. Im gonna decouple the AI model as a microservice.
   4. Hence use cloud run for back end only.
4. Public endpoints to communicate with frontend
   1. update_chat(user: int, msg: str, session_id: int) -> None
   2. reply_prompt(user: int, report: bool, timeout: bool) -> None
   3. new_chat(users: list[int]) -> session_id: int
5. Private endpints to communicate with backend
   1. get_risk_tolerance(user:int) -> risk_tolerance: int
   2. update_risk_tolerance(user:int, curr_risk: int) -> None
   3. deduct_rating(user:int) -> None
6. Private endpoints to communicate with AI model microservice
   1. new_chat() -> session_id: int
   2. update_chat(msg:str, session_id: int) -> None
   3. is_behaviour_inappropriate(: session_id: int) -> behaviour_appropriate: bool
7. Need pub/sub to trigger prompts?
   1. Maybe not. Say for now, user sents a new sentence.
      1. `update_chat()` called on backend
      2. `update_chat()` called on model
      3. `is_behaviour_inappropriate` called on model
      4. If true, then we need to promp the user on the front-end.