from collections import defaultdict

def find_town_chief(n, trust):
    # Create a directed graph using adjacency lists
    graph = defaultdict(list)
    
    # Build the graph based on the trust relationships
    for a, b in trust:
        graph[a].append(b)

    # Check if there is a town chief
    for person in range(1, n + 1):
        # Property 1: The town chief trusts nobody, so there should be no outgoing edges from the town chief
        if not graph[person]:
            # Property 2: Everybody (except the town chief) trusts the town chief, so everyone else should have an edge to the town chief
            if all(person in graph[other_person] for other_person in range(1, n + 1) if other_person != person):
                return person

    # No town chief found
    return -1

# Example usage
n = 4  # Number of people in the town
trust = [[1, 3], [2, 3], [3, 4], [4, 1], [4, 2]]  # Trust relationships

town_chief = find_town_chief(n, trust)

if town_chief != -1:
    print(f"The town chief is person {town_chief}.")
else:
    print("There is no town chief.")
