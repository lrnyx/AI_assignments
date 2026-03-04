import random

ai_responses = [
    "I enjoy reading books and learning new things.",
    "Yesterday I spent time thinking about interesting problems.",
    "I like talking to people and sharing ideas.",
    "That is an interesting question.",
    "I am not sure, but I think it depends on the situation."
]

print("---- Turing Test Simulation ----")
print("Judge will ask questions to two participants.")
print("One is human, one is AI.\n")

questions = [
    "What did you do yesterday?",
    "What is your favorite hobby?",
    "Do you like music?",
    "What do you think about technology?"
]

for q in questions:
    print("\nJudge Question:", q)

    human_response = input("Human response: ")

    ai_response = random.choice(ai_responses)

    responses = [human_response, ai_response]
    random.shuffle(responses)

    print("\nParticipant A:", responses[0])
    print("Participant B:", responses[1])

    guess = input("\nJudge: Which one is AI? (A/B): ")

    if (guess.upper() == "A" and responses[0] == ai_response) or \
       (guess.upper() == "B" and responses[1] == ai_response):
        print("Correct! You identified the AI.")
    else:
        print("Wrong! That was the human.")

print("\nTuring Test Simulation Complete.")