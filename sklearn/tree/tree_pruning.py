from sklearn.utils import check_random_state

class Desision:

    def __init__(self, random_state=None, propability=0.1):
        self.random_state = check_random_state(random_state)
        self.propability = propability

    def flip(self, proba=None):
        if proba is None:
            proba = self.propability
        return self.random_state.rand() < proba
