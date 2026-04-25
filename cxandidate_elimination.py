import csv

def load_data(filename):
    with open(filename, 'r') as file:
        data = list(csv.reader(file))
    return data[1:]   # skip header


# Check if hypothesis h is consistent with example x
def is_consistent(h, x):
    return all(h[i] == '?' or h[i] == x[i] for i in range(len(h)))


# Check if h1 is more general than or equal to h2
def more_general(h1, h2):
    more = False
    for i in range(len(h1)):
        if h1[i] == '?' and h2[i] != '?':
            more = True
        elif h1[i] != h2[i]:
            return False
    return True


# Remove duplicate and overly specific hypotheses
def prune(G):
    pruned = []
    for g in G:
        if not any((g != h and more_general(h, g)) for h in G):
            if g not in pruned:
                pruned.append(g)
    return pruned


def candidate_elimination(data):
    num_attr = len(data[0]) - 1

    S = ['0'] * num_attr
    G = [['?'] * num_attr]

    print("Initial S:", S)
    print("Initial G:", G)

    for step, row in enumerate(data, start=1):
        x = row[:-1]
        label = row[-1]

        print(f"\nStep {step}: {row}")

        if label == "Go":   # POSITIVE
            # Remove inconsistent hypotheses from G
            G = [g for g in G if is_consistent(g, x)]

            # Generalize S
            for i in range(num_attr):
                if S[i] == '0':
                    S[i] = x[i]
                elif S[i] != x[i]:
                    S[i] = '?'

        else:   # NEGATIVE
            new_G = []
            for g in G:
                if is_consistent(g, x):
                    for i in range(num_attr):
                        if g[i] == '?':
                            if S[i] != x[i]:
                                new_h = g.copy()
                                new_h[i] = S[i]
                                new_G.append(new_h)
                else:
                    new_G.append(g)

            G = prune(new_G)

        print("S:", S)
        print("G:", G)

    return S, G


# Run
data = load_data("data.csv")
S, G = candidate_elimination(data)

print("\nFinal S:", S)
print("Final G:", G)