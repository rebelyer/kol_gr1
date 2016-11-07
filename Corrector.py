#!/usr/bin/python2


class Corrector(object):
    def __init__(self, max_correction=7.0):
        self._max_correction = max_correction

    def correct(self, angle):
        if angle > self._max_correction:
            return - self._max_correction
        elif angle < - self._max_correction:
            return self._max_correction
        else:
            return -angle


if __name__ == "__main__":
    from Airplane import Airplane
    airplane = Airplane()
    while True:
        try:
            airplane.fly()
            print airplane
        except KeyboardInterrupt:
            airplane.land()
            break
