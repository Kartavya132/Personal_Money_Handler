from __init__ import *


class mains(ABC):
    @ab
    def add_acc(self):
        pass

    @ab
    def acc_detail(self):
        pass

    @ab
    def add_d(self):
        pass

    @ab
    def predict(self):
        pass

    @ab
    def plots_build(self):
        pass


class Account(mains):
    def add_acc(self):
        pass

    def acc_detail(self):
        pass

    def add_d(self):
        pass

    def predict(self):
        pass

    def plots_build(self):
        pass

    def __del__(self):
        pass


class Normal(Account):
    def __init__(self):
        pass

    def add_acc(self):
        pass

    def make_move(self):
        pass

    def __del__(self):
        pass


class Saving(Account):
    def __init__(self):
        pass

    def add_acc(self):
        pass

    def make_move(self):
        pass

    def __del__(self):
        pass
