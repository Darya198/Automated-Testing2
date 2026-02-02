from adress import Adress


class Mailing:
    def __init__(self, to_adress, fromn_adress, cost, track):
        self.to_adress = Adress
        self.from_adress = Adress
        self.cost = cost
        self.track = track

    def __str__(self):
        return (f"{self.track}, {self.from_adress}, "
                f"{self.to_adress}, {self.cost}")
