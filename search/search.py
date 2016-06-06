# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util,copy

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    -> Start: (5, 5)
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    -> Is the start a goal? False
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    -> Start's successors: [((5, 4), 'South', 1), ((4, 5), 'West', 1)]
     """
    "*** YOUR CODE HERE ***"
    current = problem.getStartState()
    visited = [current]
    for next in problem.getSuccessors(current):
        result = dfs_rec(problem, visited, [], next)
        if result != -1:
            return result
    return []


def dfs_rec(problem, visited, path, node):
    if node[0] not in visited:
        path = copy.copy(path)
        visited.append(node[0])
        path.append(node[1])
        if problem.isGoalState(node[0]):
            return path
        else:
            for childNode in problem.getSuccessors(node[0]):
                result = dfs_rec(problem, visited, path, childNode)
                if result != -1:
                    return result
            return -1
    return -1



def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue = util.Queue()
    visited = [problem.getStartState()]

    queue.push((problem.getStartState(), []))

    while not queue.isEmpty():
        (current, path) = queue.pop()
        for childNode in problem.getSuccessors(current):
            if childNode[0] not in visited:
                visited.append(childNode[0])
                if problem.isGoalState(childNode[0]):
                    return path + [childNode[1]]
                else:
                    queue.push((childNode[0], path + [childNode[1]]))

    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    queue = util.PriorityQueue()
    visited = [problem.getStartState()]

    queue.push((problem.getStartState(), []),0)

    while not queue.isEmpty():
        (current, path) = queue.pop()
        for childNode in problem.getSuccessors(current):
            if childNode[0] not in visited:
                visited.append(childNode[0])
                if problem.isGoalState(childNode[0]):
                    return path + [childNode[1]]
                else:
                    queue.push((childNode[0], path + [childNode[1]]),problem.getCostOfActions(path + [childNode[1]]))

    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
