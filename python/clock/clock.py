class Clock :
    def __init__(self, h, m) :
        self.hours = h
        self.mins = m
        self.correct()

    def correct(self) :
        self.hours += self.mins / 60
        self.mins = self.mins % 60
        self.hours = self.hours % 24

    def displayHours(self) :
        return str(self.hours).zfill(2)

    def displayMins(self) :
        return str(self.mins).zfill(2)

    def add(self, mins) :
        self.mins += mins
        self.correct()
        return self

    def __str__(self) :
        return self.displayHours() + ':' + self.displayMins()

    def __eq__(self, rhs) :
        return self.hours == rhs.hours and self.mins == self.mins

