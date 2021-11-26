class State:
    def __init__(self, state_number, lower_state, higher_state, color):
        self.state_number = state_number
        self.lower_state = lower_state
        self.higher_state = higher_state
        self.color = color

    def get_next_state(self, state):
        if state == self.lower_state:
            return self.state_number - 1
        elif state == self.higher_state:
            return self.state_number + 1
        else:
            return self.state_number

    def get_color(self):
        return self.color

    def get_state_name(self):
        return "S" + str(self.state_number)


ALLOWED_STATES = ["0,0", "0,1", "1,0", "1,1"]
HIGHER_STATE = "0,1"
LOWER_STATE = "1,1"


def main():
    S0 = State(0, None, HIGHER_STATE, "zelena")
    S1 = State(1, LOWER_STATE, "1,0", "zelena")
    S2 = State(2, "0,0", HIGHER_STATE, "cervena")
    S3 = State(3, LOWER_STATE, None, "cervena")
    states = [S0, S1, S2, S3]

    current_state = S0
    while True:
        string = input("Zadajte prechod v tvare X,Y (pre ukoncenie zadajte N):")
        if string == "N":
            break
        elif string not in ALLOWED_STATES:
            print("Zadali ste nespravny stav! Skuste znova...")
            continue
        next_state_number = current_state.get_next_state(string)
        current_state = states[next_state_number]
        print("Sucasny stav: {}, farba semaforu: {}".format(current_state.get_state_name(), current_state.get_color()))
    print("Dovidenia")

main()
