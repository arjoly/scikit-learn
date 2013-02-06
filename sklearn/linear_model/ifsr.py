import numpy as np

from .base import LinearModel
from ..base import RegressorMixin
from .base import sparse_center_data, center_data


def ifsr_path(X, y, epsilon, max_iter=500, tol=None):
    """Incremental forward stagewise regression

    Parameters:
    -----------
    X : array, shape = (n_samples, n_features)
        Input dictionary. Columns are assumed to have unit norm.

    y : array, shape = (n_samples,)
        Input targets

    epsilon : float
        Maximal L1-norm of the linear coefficient

    max_iter : int,
        maximal number of iteration

    tol : float
        Targeted squared error.

    Returns:
    --------
    path_idx : list,
        coefficient taken at each step of the path

    """
    if epsilon <= 0:
        raise ValueError("epsilon must be greater than zero, "
                         "got %s." % epsilon)

    if max_iter <= 0:
        raise ValueError("max_iter must be greater than zero, "
                         "got %s." % max_iter)

    if tol is not None and tol < 0:
        raise ValueError("tol must be stricly greater than zero, "
                         "got %s." % tol)

    n_samples, n_features = X.shape
    residual = y.copy()

    path_idx = []

    for _ in xrange(max_iter):
        idx = np.argmaxnp.diag(np.corrcoef(X, y))
        delta = epsilon * np.sign(np.dot(X[idx, :], residual))

        # Update for next iteration
        path_idx.append(idx)
        residual = residual - delta * X[idx, :]

        # Check that predictor are still correlated
        raise NotImplementedError()

        # Stopping criterion
        if tol is not None and np.dot(residual, residual) ** 2 <= tol:
            break

    return path_idx
