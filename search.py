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

import util
from game import Directions
from typing import List
from util import Stack #esto sera util para la funcion de exploracion
from util import PriorityQueue #esto sera util para la funcion de exploracion


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




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    celdas_Visitadas = set()
    pila = Stack()
    #la pila tendra info sobre el estado actual y una lista con todos los movimientos que hace
    comienzo = problem.getStartState()
    pila.push((comienzo,[]))

    while not pila.isEmpty():
         estado, acciones = pila.pop()
         if estado not in celdas_Visitadas:
            celdas_Visitadas.add(estado)
            if problem.isGoalState(estado):
                return acciones
            sucesores = problem.getSuccessors(estado)
            indice = 0
            while indice < len(sucesores):
                estado_sig,accion,coste = sucesores[indice]
                if estado_sig not in celdas_Visitadas:
                    pila.push((estado_sig,acciones + [accion]))
                indice+=1
    return []

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def distanciaEuclidea(state, problem=None):
    x1, y1 = state
    x2, y2 = problem.goal

    distancia = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return distancia



def aStarSearch(problem: SearchProblem, heuristic=distanciaEuclidea) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    celdas_Visitadas = set()

    cola = PriorityQueue()

    comienzo = problem.getStartState()

    prioridad_inicial = 0 + heuristic(comienzo, problem)

    cola.push((comienzo, [], 0), prioridad_inicial)

    while not cola.isEmpty():
        estado, acciones, coste_acumulado = cola.pop()

        if estado not in celdas_Visitadas:
            celdas_Visitadas.add(estado)

            if problem.isGoalState(estado):
                return acciones

            sucesores = problem.getSuccessors(estado)

            for estado_sig, accion, coste_paso in sucesores:
                if estado_sig not in celdas_Visitadas:

                    nuevo_coste = coste_acumulado + coste_paso

                    valor_heuristica = heuristic(estado_sig, problem)
                    f_n = nuevo_coste + valor_heuristica

                    cola.push((estado_sig, acciones + [accion], nuevo_coste), f_n)

    return []



def exploration(problem):
    # utilizamos la funcion de ufs
    celdas_Visitadas = set()
    cola = PriorityQueue()
    # ahora almacenamos el estado, las acciones y el coste acumulado
    comienzo = problem.getStartState()
    cola.push((comienzo,[],0),0)

    while not cola.isEmpty():
        estado, acciones, coste  = cola.pop()
        if estado not in celdas_Visitadas:
            celdas_Visitadas.add(estado)
            if problem.isGoalState(estado):
                return acciones
            sucesores = problem.getSuccessors(estado)
            i = 0
            while i < len(sucesores):
                estado_sig, accion, coste_sig = sucesores[i]
                if estado_sig not in celdas_Visitadas:
                    nuevo_coste = coste + coste_sig
                    cola.push((estado_sig,acciones + [accion], nuevo_coste), nuevo_coste)
                i+=1
    return []

def dfs(problem):
     # Stack for DFS traversal: usamos una pila para el dfs
    celdas_Visitadas = set()
    pila = Stack()
    #la pila tendra info sobre el estado actual y una lista con todos los movimientos que hace
    comienzo = problem.getStartState()
    pila.push((comienzo,[]))

    while not pila.isEmpty():
         estado, acciones = pila.pop()
         if estado not in celdas_Visitadas:
            celdas_Visitadas.add(estado)
            if problem.isGoalState(estado):
                return acciones
            sucesores = problem.getSuccessors(estado)
            indice = 0
            while indice < len(sucesores):
                estado_sig,accion,coste = sucesores[indice]
                if estado_sig not in celdas_Visitadas:
                    pila.push((estado_sig,acciones + [accion]))
                indice+=1
    return []



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
exp = exploration
