class Aircraft:
    """
    abstract Aircarft class
    """

    def __init__(self, registration):
        self.registration = registration

    def num_seats(self):
        """
        calculate total number of seats
        :return: number of seats
        """
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)

    def model(self):
        """
        :return: aircraft model name
        """
        raise NotImplementedError("Subclass must implement abstract method")

    def seating_plan(self):
        """
        :return: aircraft seating plan
        """
        raise NotImplementedError("Subclass must implement abstract method")

    def __str__(self):
        return f"Reg: {self.registration} Model: {self.model()} has {self.num_seats()} seats: {self.seating_plan()}"
