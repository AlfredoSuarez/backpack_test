
from ortools.algorithms.python import knapsack_solver
import random


def main():
    
    # Create the solver.
    solver = knapsack_solver.KnapsackSolver(
        knapsack_solver.SolverType.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER,
        "KnapsackExample",
    )

    for i in range(10):
        values = [
            # fmt:off
        random.randint(0, 100) for _ in range(20)
            # fmt:on
        ]
        weights = [
            # fmt: off
        [random.randint(0, 100) for _ in range(20)]
            # fmt: on
        ]
        capacities = [random.randint(15, 100) for _ in range(1)]#capacities = [50]

        solver.init(values, weights, capacities)
        computed_value = solver.solve()

        packed_items = []
        packed_weights = []
        total_weight = 0
        print("--------------------------------------")
        print(f"Iteration {i + 1}:\nTotal value = {computed_value}")
        #print("Total value =", computed_value)
        for i in range(len(values)):
            if solver.best_solution_contains(i):
                packed_items.append(i)
                packed_weights.append(weights[0][i])
                total_weight += weights[0][i]
        print("Capacity of the container:", capacities)
        print("Total weight:", total_weight)
        print("Packed items:", packed_items)
        print("Packed_weights:", packed_weights)


if __name__ == "__main__":
    main()