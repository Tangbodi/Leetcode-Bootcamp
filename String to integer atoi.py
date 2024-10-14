class StateMachine:
    def __init__(self):
        self.State = {"q0": 1, "q1": 2, "q2": 3, "qd": 4}
        self.INT_MAX, self.INT_MIN = pow(2, 31) - 1, -pow(2, 31)

        self.__current_state = self.State["q0"]
        self.__result = 0
        self.__sign = 1

    def to_state_q1(self, ch: chr) -> None:
        self.__sign = -1 if (ch == "-") else 1
        self.__current_state = self.State["q1"]

    def to_state_q2(self, digit: int) -> None:
        self.__current_state = self.State["q2"]
        self.append_digit(digit)

    def to_state_qd(self) -> None:
        self.__current_state = self.State["qd"]

    def append_digit(self, digit: int) -> None:
        if (self.__result > self.INT_MAX // 10) or (
            self.__result == self.INT_MAX // 10 and digit > self.INT_MAX % 10
        ):
            if self.__sign == 1:
                self.__result = self.INT_MAX
            else:
                self.__result = self.INT_MIN
                self.__sign = 1

            self.to_state_qd()
        else:
            self.__result = (self.__result * 10) + digit

    def transition(self, ch: chr) -> None:
        if self.__current_state == self.State["q0"]:
            if ch == " ":
                return
            elif ch == "-" or ch == "+":
                self.to_state_q1(ch)
            elif ch.isdigit():
                self.to_state_q2(int(ch))
            else:
                self.to_state_qd()

        elif (
            self.__current_state == self.State["q1"]
            or self.__current_state == self.State["q2"]
        ):
            if ch.isdigit():
                self.to_state_q2(int(ch))
            else:
                self.to_state_qd()

    def get_integer(self) -> int:
        return self.__sign * self.__result

    def get_state(self) -> int:
        return self.__current_state


class Solution:
    def myAtoi(self, input: str) -> int:
        q = StateMachine()

        for ch in input:
            q.transition(ch)
            if q.get_state() == q.State["qd"]:
                break

        return q.get_integer()