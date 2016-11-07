from Corrector import Corrector
import time
import random


class Airplane(object):
    def __init__(self, corrector=Corrector()):
        self._corrector = corrector
        self._current_angle = 0.0

    def fly(self):
        self._turbulence()
        self._make_correction()
        time.sleep(1)

    def land(self):
        time.sleep(1)
        print 'Plane successfully landed.'

    def __str__(self):
        return "Current position " + str(self._current_angle)

    def _turbulence(self):
        self._current_angle += random.gauss(0, 5)

    def _make_correction(self):
        self._current_angle = self._corrector.correct(self._current_angle)