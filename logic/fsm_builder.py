from machine_model import MachineModel
from automata.fa.dfa import DFA
from graph_items.edge_item import EdgeItem
from graph_items.node_item import NodeItem

class FSMBuilder(MachineModel):
    # Self will now contain a MachineModel object within it (type of inheritence)
    def build(self):
        # Get the transitions and edges to create a dictionary in the form
        # 'start state' : {'symbol': 'end state', 'symbol': 'end state'}
        # Basically you're building the transitions dictionary
        
        dfa_transitions = {}
        for node in self.nodes:
            curr_state_transitions = {}
            for edge in node.edges:
                curr_state_transitions[edge.symbol] =  edge.node2.name
            dfa_transitions[node.name] = curr_state_transitions
        
        dfa = DFA(
            states = self.states,
            input_symbols = self.input_symbols,
            transitions = dfa_transitions,
            initial_state = self.initial_state,
            final_states = self.final_states
            )
        return dfa
        
