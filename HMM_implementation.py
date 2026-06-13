import numpy as np

states = ["Rainy", "Sunny"]

start_prob = [0.6, 0.4]

transition = [
    [0.7, 0.3],
    [0.4, 0.6]
]

emission = [
    [0.8, 0.2],
    [0.3, 0.7]
]

n = int(input("Enter number of observations: "))

obs = []
print("Enter observations (0 or 1):")

for i in range(n):
    obs.append(int(input()))

hidden_states = []

for observation in obs:

    max_prob = -1
    best_state = 0

    for state in range(len(states)):
        prob = start_prob[state] * emission[state][observation]

        if prob > max_prob:
            max_prob = prob
            best_state = state

    hidden_states.append(states[best_state])

print("\nPredicted Hidden States:")
for s in hidden_states:
    print(s)