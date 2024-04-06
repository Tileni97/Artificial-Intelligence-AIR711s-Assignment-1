def compare_with_optimal(tsp, solution, optimal_distance):
    """
    Compare the solution obtained with the optimal distance (if available).
    """
    final_route, total_distance = solution

    print("Places visited by the trace:")
    for place in final_route:
        print(place)

    print("\nDistance found by Hill Climbing:", total_distance)
    print("Optimal Distance:", optimal_distance)
    if optimal_distance:
        percentage_difference = ((total_distance - optimal_distance) / optimal_distance) * 100
        print("Percentage Difference:", percentage_difference, "%")
