class DetectState:
    state = 0
    state3count = 0

    def __init__(self):
        self.state = 1
        self.state3count = 0

    def input(self, value):
        if self.state == 1:
            if value != 0:
                self.state = 2
        elif self.state == 2:
            if value == 0:
                self.state = 3
                self.state3count = 60
        elif self.state == 3:
            if value == 0:
                self.state3count = self.state3count - 1
                if self.state3count == 0:
                    self.state = 1
            else:
                self.state = 4
                return self.state, 1
        else:
            if value == 0:
                self.state = 1
        return self.state, 0

state = DetectState()
s, d = state.input(0)
print s,d
s, d = state.input(1)
print s,d
s, d = state.input(1)
print s,d
s, d = state.input(0)
print s,d
s, d = state.input(0)
print s,d
