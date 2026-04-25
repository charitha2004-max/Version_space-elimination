Version Space Assignment (Candidate Elimination)

 Aim

To implement the Candidate Elimination Algorithm and determine the version space using training data.
Introduction
The Candidate Elimination Algorithm is a concept learning technique in Machine Learning. It finds all possible hypotheses that are consistent with the given training data.

This is done using two boundaries:
Specific Hypothesis (S):** The most specific rule
General Hypothesis (G):** The most general rule
Together, these form the Version Space


 Concept
For positive examples, S is generalized and inconsistent hypotheses are removed from G.
For negative examples, G is specialized and inconsistent hypotheses are removed.


Dataset
A custom dataset is used to predict whether a person will **go on a trip or not** based on attributes:

* Weather
* Budget
* Companion
* Transport
* Stay

Target:
Decision (Go / Not Go)

Files Included
 Python implementation of the algorithm
 →Dataset used for training

How to Run

1. Open the folder in Visual Studio Code
2. Open terminal
3. Run the command:


The program displays:

* Step-by-step updates of S and G
* Final Specific Hypothesis
* Final General Hypothesis


Result

The algorithm successfully computes the hypothesis boundaries based on the dataset and identifies the consistent version space.

Conclusion

Candidate Elimination helps in narrowing down the hypothesis space by eliminating inconsistent rules and retaining only valid ones.


