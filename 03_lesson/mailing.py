from address import Address


class Mailing:
    def __init__(self, to_address, fromn_address, cost, track):
        self.to_address = Address
        self.from_address = Address
        self.cost = cost
        self.track = track

    def __str__(self):
        return (f"{self.track}, {self.from_address}, "
                f"{self.to_address}, {self.cost}")
