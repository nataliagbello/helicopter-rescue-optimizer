# helicopter-rescue-optimizer

This project was developed as part of the Algorithms and Data Structures course at Universidade Federal do Rio de Janeiro (UFRJ). The goal was to design an optimization system to maximize the number of lives saved in a helicopter rescue mission given a limited fuel supply. By implementing a Greedy Strategy combined with a custom Merge Sort algorithm ($O(n \log n)$), the system calculates an "Urgency Factor" for each lifeboat to determine the most efficient rescue sequence. The project also features a graphical interface built with Tkinter to visualize the decision-making process and the spatial distribution of the rescue mission.

## Problem Statement: 
### The Helicopter Rescue Scenario: 
Following a maritime accident, several lifeboats are adrift at different distances from a central helipad. A rescue helicopter has been dispatched, but it faces a critical constraint: limited fuel capacity.
Each lifeboat has three specific attributes:
* Number of People: How many passengers are on board.
* Distance: The distance (in km) from the helipad.
* Risk Level: A multiplier representing the urgency of the situation (e.g., medical emergencies or boat stability).
### The Challenge: 
The helicopter must perform round-trips (Helipad → Boat → Helipad) for each rescue. The goal is to develop an algorithm that determines the optimal rescue sequence to maximize the number of lives saved before the fuel runs out.

## Solution Strategy
* Greedy Approach: The algorithm makes the locally optimal choice at each step, prioritizing boats with the highest Urgency Factor.
* Urgency Formula: $$Urgency = \frac{People \times Risk}{Fuel Cost}$$
* Sorting: Uses Merge Sort to order boats by priority. The $O(n \log n)$ complexity ensures the algorithm remains efficient even as the number of boats increases.
* Execution: The system iterates through the prioritized list, rescuing each boat only if the remaining fuel allows for a complete round trip.

