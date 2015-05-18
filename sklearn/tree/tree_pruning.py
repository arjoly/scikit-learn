from sklearn.utils import check_random_state


class Desision:

    def __init__(self, random_state=None, propability=0.1):
        self.random_state = check_random_state(random_state)
        self.propability = propability

    def flip(self, proba=None):
        if proba is None:
            proba = self.propability
        return self.random_state.rand() < proba

class TreePointer:

    def __init__(self, clf, mean=0.0, std=0.0):
        self.pointed_clf = clf
        self.mean = mean
        self.std = std

    def predict(self, X, x_std=None):
        return self.pointed_clf.predict(X, x_std, self.mean, self.std)

    def predict_proba(self, X, x_std=None):
        return self.pointed_clf.predict_proba(X, x_std, self.mean, self.std)

    def predict_log_proba(self, X, x_std=None):
        return self.pointed_clf.predict_log_proba(X, x_std, self.mean, self.std)

