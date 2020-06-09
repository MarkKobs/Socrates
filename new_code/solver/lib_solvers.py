import autograd.numpy as np

from scipy.optimize import minimize
from scipy.optimize import Bounds

class Optimize():
    def __init__(self):
        return

    def __solve_syntactic_sugar(self, model, assertion):
        return

    def __obj_func(x, model, assertion):
        vars_dict = {}
        size = np.prod(model.shape)

        for i in len(assertion.vars):
            var = assertion.vars[i]
            vars_dict[var.name] = x[i * size : (i + 1) * size]

        vars_dict.update(assertion.init_dict)

        return assertion.neg_num_value(vars_dict)

    def solve(self, model, assertion):
        if isinstance(assertion, dict):
            return self.__solve_syntactic_sugar(model, assertion)

        x = np.zeros(np.prod(model.shape) * len(assertion.vars))
        args = (model, assertion)
        bounds = Bounds(model.lower, model.upper)
        jac = grad(self.__obj_func)

        res = minimize(self.__obj_func, x, args=args, bounds=bounds, jac=jac)



class SPRT():
    def __init__(self, threshold, alpha, beta, delta):
        self.threshold = threshold
        self.alpha = alpha
        self.beta = beta
        self.delta = delta

    def __generate_x(self, shape, lower, upper):
        size = np.prod(shape)
        x = np.random.rand(size)

        x = (upper - lower) * x + lower

        return x

    def __solve_syntactic_sugar(self, model, spec):
        return

    def solve(self, model, assertion):
        if isinstance(assertion, dict):
            return self.__solve_syntactic_sugar(model, assertion)

        p0 = self.threshold + self.delta
        p1 = self.threshold - self.delta

        h0 = self.beta / (1 - self.alpha)
        h1 = (1 - self.beta) / self.alpha

        pr = 1

        while True:
            vars_dict = {}

            for var in assertion.vars:
                x = self.__generate_x(model.shape, model.lower, model.upper)
                vars_dict[var.name] = x

            vars_dict.update(assertion.init_dict)

            if assertion.get_pre_value(vars_dict):
                if assertion.get_post_value(vars_dict):
                    pr = pr * p1 / p0
                else:
                    pr = pr * (1 - p1) / (1 - p0)

            if pr <= h0:
                print('Accept H0. The assertion is satisfied with p >= {} after {} tests.'.format(p0, no_x))
                break
            elif pr >= h1:
                print('Accept H1. The assertion is satisfied with p <= {} after {} tests.'.format(p1, no_x))
                break