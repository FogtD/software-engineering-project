class FSMBuilder(MachineModel):
    # Self will now contain a MachineModel object within it (type of inheritence)
    def build(self):
        # Get the transitions and edges to create a dictionary in the form
        # 'start state' : {'symbol': 'end state', 'symbol': 'end state'}
        # Basically you're building the transitions dictionary

        dfa = DFA(
            states = self.states,
            input_symbols = self.input_symbols,
            transitions = transitions,
            initial_state = self.initial_state,
            final_states = self.final_states
            )
        return dfa
    

    