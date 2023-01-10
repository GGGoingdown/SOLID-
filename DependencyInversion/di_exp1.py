###
#   Bad
###
# class LightBulb:
#     def turn_on(self) -> None:
#         print("Lightbulb::Turn on")

#     def turn_off(self) -> None:
#         print("Lightbulb::Turn off")


# class PowerSwitch:
#     def __init__(self, lightbulb: LightBulb) -> None:
#         self.lightbulb = lightbulb
#         self.on: bool = False

#     def press(self) -> None:
#         if self.on:
#             self.lightbulb.turn_off()
#             self.on = False

#         else:
#             self.lightbulb.turn_on()
#             self.on = True


###
#   Good
###
from abc import ABC, abstractclassmethod


class Switchable(ABC):
    @abstractclassmethod
    def turn_on(self) -> None:
        raise NotImplementedError

    @abstractclassmethod
    def turn_off(self) -> None:
        raise NotImplementedError


class LightBulb(Switchable):
    def turn_on(self) -> None:
        print("Lightbulb::Turn on")

    def turn_off(self) -> None:
        print("Lightbulb::Turn off")


class Fan(Switchable):
    def turn_on(self) -> None:
        print("Fan::Turn on")

    def turn_off(self) -> None:
        print("Fan::Turn off")


class PowerSwitch:
    def __init__(self, device: Switchable) -> None:
        self.device = device
        self.on: bool = False

    def press(self) -> None:
        if self.on:
            self.device.turn_off()
            self.on = False

        else:
            self.device.turn_on()
            self.on = True


if __name__ == "__main__":
    lb = LightBulb()
    fan = Fan()
    ps = PowerSwitch(device=fan)
    ps.press()  # Fan::Turn on
    ps.press()  # Fan::Turn off
