from board import Board
import math
import random
class MonteCarloNode(object):

    def __init__(self, board, parent):
        self.number_of_visits = 0.
        self.results = defaultdict(int)
        self.untried_actions = None
        self.board = board
        self.parent = parent

    def is_fully_expanded(self):
        return len(self.untried_actions) == 0

    def best_child(self, c_param=1.4):
        choices_weights = [
            (c.q / c.n) + c_param * sqrt((2 * math.log(self.n) / c.n))
            for c in self.children
        ]
        return self.children[np.argmax(choices_weights)]

    def rollout_policy(self, possible_moves):        
        return possible_moves[random.randint(0, len(possible_moves))]

    def untried_actions(self):
        if self.untried_actions = None:
            self.untried_actions = self.board.getAllValidMoves()
        return self.untried_actions

    def q(self):
        wins = self.results[self.parent.board.current_player]
        loses = self.results[-1 * self.parent.board.current_player]#redo
        return wins - loses

    def n(self):
        return self.number_of_visits

    def expand(self):
        action = self.untried_actions.pop()
        next_board = self.board.makeMove
        child = MonteCarloNode(board=next_board, parent=self)
        self.children.append(child)
        return child

    def is_terminal(self):
        return self.board.isTerminal()

    def rollout(self):
        current_rollout_state = self.board
        while not current_rollout_state.isTerminal():
            possible_moves = current_rollout_state.getAllValidMoves()
            action = self.rollout_policy(possible_moves)
            current_rollout_state = current_rollout_state.move(action)
        return current_rollout_state.result           

    #"repopulates" up the chain of parents
   def backpropagate(self, result):
       self.number_of_visits += 1
       self.results[result] += 1
       if self.parent: # if parent is not None
           self.parent.backpropagate(result)



class MonteCarloSearch(object):
    def __init__(self, node):
        self.root = node

    def best_action(self, num_sims=10):
        for _ in range(0, simulations_number):            
            v = self.tree_policy()
            reward = v.rollout()
            v.backpropagate(reward)
        # to select best child go for exploitation only
        return self.root.best_child(c_param=0.)


    def tree_policy(self):
        current = self.root
        while not current.is_terminal():
            if not current.is_fully_expanded():
                return current.expand()
            else:
                current = current.best_child()
        return current                
