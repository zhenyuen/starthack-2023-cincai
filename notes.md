

Details:

1. Voting
	1. For yes-no scenarios, follow victim decision (no majority vote), or ignore if no response from victim.
	2. If required, use majority vote calculated by $$\begin{split}N&=\sum_i{R_i}\\score&=\frac{\sum_i\delta_i}{N}\end{split}$$such that $R_i$ is the rating of user $i$, and $\delta_i = 1$ is user $i$ votes yes, else $\delta_i=0$
2. We prioritise both users (A and B) engaged in the conversation. If both sides okay with profanity, then we only check if other users in the same chat is okay with it.
3. Use a rolling average to update risk tolerance
4. Rating system use a simple increment/decrement, alll users start with $R_i = 80$ out of 100.
	1. Set threshold for temporary/permanent bans.
	2. If user has no engaged in any in inappropriate behaviour for $100 - R_i$ days, then increment rating daily until the next inappropriate behavious.
5. If user does not respond to prompt, skip the next time the user is engaged in another argument/ being bullied. If user still does not respond on the following situation, then skip twice (multiples of two basically, hence exponential backoff)


Demo.

1. Demonstrate 2 cases:
	1. Abusive
	2. Arguing

2. Assume:
	1. 5 users - A, B, C, D, E
		1. Users A,B engaged
		2. Users C,D,E are participants
	2. To simplify situation,
		1. Only A and B actively sending messages, other participants do not send messages (they do not start conversations of a different context in the same chat box)
		2. Participants can be online or offline.

3. Case 1, Abusive:
	1. A bullies B. Prompt B. B says yes. Deduct A's rating. Adjust B's risk tolerance.
	2. A bullies B. Prompt B. B says no.
		1. If no ONLINE participants, do nothing.
		2. Else, ask majority vote.
			1. If yes, deduct A rating. Adjust participants risk tolerance
4. Case 2, Arguing:
	1. A and B using profanity. Prompt A and B. Both says no.
		1. If no ONLINE participants, do nothing.
		2. Else, ask majority vote.
			1. If yes, warn A and B.
				1. If situation escalates, deduct A and B's rating. Adjust participants risk tolerance.
	2. A and B using profanity. Prompt A and B. Both says yes.
		1. If yes, warn A and B.
		2. If situation escalates, deduct A and B's rating. Adjust A and B's risk tolerance.
	3. A and B using profanity. Prompt A and B. One yes and one no.
		1. If yes, warn A and B.
		2. If situation escalates, deduct A and B's rating. Adjust A/B's (the one who voted yes) risk tolerance.

5. Implementation, assume all local
	1. Start the main client to run the server
	2. Adjust the rating/risk preference of the users manually via the local db file
	3. Start 5 other clients representing the other users.