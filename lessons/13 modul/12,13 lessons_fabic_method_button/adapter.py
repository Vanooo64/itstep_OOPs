from math import sqrt

class RoundPeg: #циліндр
    def __init__(self, radius: int):
        self._radius = radius

    def get_radius(self):
        return self._radius


class SquarePeg: #квадратний кілок
    def __init__(self, width: int):
        self._width = width

    def get_width(self):
        return self._width


class SquarePegAdapter(RoundPeg): # переформатовує get_radius для квадрату
    def __init__(self, peg: SquarePeg):
        self._peg = peg

    def get_radius(self):
        return self._peg.get_width() * sqrt(2) / 2


class RoundHole: #круглий отвір
    def __init__(self, radius: int):
        self._radius = radius

    def get_radius(self):
        return self._radius

    def fit(self, pag: RoundPeg):  #порівнюемо отвір з циліндром
        result = self.get_radius() >= pag.get_radius()
        print(f"Fit: {result}")
        return result

hole = RoundHole(5)
rpeg = RoundPeg(4)
hole.fit(rpeg)
print()

small_sqpeg = SquarePeg(5) #намагаемось перевірити квадрат до круглого отвору, помилка
large_sqpeg = SquarePeg(10)

small_sqpeg_adapter = SquarePegAdapter(small_sqpeg) #робимо адаптер для квадрата тоді можна зробити перевірку
large_sqpeg_adapter = SquarePegAdapter(large_sqpeg)

hole.fit(small_sqpeg_adapter)





