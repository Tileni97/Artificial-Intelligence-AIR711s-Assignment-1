import random

def randomSolution(tsp): # generate a random solution
    places = list(range(len(tsp)))
    solution = []

    for i in range(len(tsp)): # for each element in the tsp
        randomPlace = places[
            random.randint(0, len(places) - 1)]
        solution.append(randomPlace)
        places.remove(randomPlace)

    return solution

def routeLength(solution, tsp): # calculate the length of the route
    routeLength = 0
    for i in range(len(solution)):
        routeLength += tsp[solution[i - 1]][1][solution[i]]
    return routeLength

def getNeighbours(solution): # get all neighbors by swapping two places in the route
    neighbours = []
    for i in range(len(solution)): # for each element in the solution
        for j in range(i + 1, len(solution)): # swap two places, exclude self
            neighbour = solution.copy() # copy the solution
            neighbour[i] = solution[j] # swap
            neighbour[j] = solution[i] # swap
            neighbours.append(neighbour) # add the neighbor to the neighbors list
    return neighbours
def getBestNeighbour(neighbours, tsp): # get the best neighbour
    bestRouteLength = routeLength(neighbours[0], tsp) # get the route length of the first neighbor
    bestNeighbour = neighbours[0]
    for neighbour in neighbours:
        currentRouteLength = routeLength(neighbour, tsp)
        if currentRouteLength < bestRouteLength:
            bestRouteLength = currentRouteLength
            bestNeighbour = neighbour

    return bestNeighbour, bestRouteLength # return the best neighbor and the route length of the best neighbor
def hillclimbing(tsp):
    currentSolution = randomSolution(tsp)
    currentRouteLength = routeLength(currentSolution, tsp)
    neighbours = getNeighbours(currentSolution)  # get all neighbors
    bestNeighgbours, bestNeighgboursRouteLength = getBestNeighbour(neighbours, tsp)  # get the best neighbor

    while bestNeighgboursRouteLength < currentRouteLength:  # if the best neighbor is better than the current solution
        currentSolution = bestNeighgbours # set the current solution to the best neighbor
        currentRouteLength = bestNeighgboursRouteLength # set the current route length to the best neighbor's route length
        neighbours = getNeighbours(currentSolution) # get all neighbors
        bestNeighgbours, bestNeighgboursRouteLength = getBestNeighbour(neighbours, tsp) # get the best neighbor

    return currentSolution, currentRouteLength

