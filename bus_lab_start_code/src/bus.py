class Bus:
    def __init__ (self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []
    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self, new_passenger):
        self.passengers.append(new_passenger)

    def drop_off(self, passenger):
        self.passengers.remove(passenger)

    def empty(self):
        self.passengers = []

    def pick_up_from_stop(self, bus_stop):
        while len(bus_stop.queue) != 0:
            self.pick_up(bus_stop.queue)
            bus_stop.remove_from_queue()