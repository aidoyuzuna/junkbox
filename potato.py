class Potato:
    def __init__(self, weight):
        self.potato = weight


class KitchenScale:
    def __init__(self):
        self.potato_weight = 0.0

    def scale_put_on(self, potato):
        self.potato_weight += potato.potato

    def scale_clear(self):
        self.potato_weight = 0.0

    def scale_weighing(self):
        return self.potato_weight


def main():
    scale = KitchenScale()
    potato1 = Potato(2.0)
    scale.scale_put_on(potato1)
    potato2 = Potato(3.0)
    scale.scale_put_on(potato2)
    print(scale.scale_weighing())
    scale.scale_clear()
    print(scale.scale_weighing())


if __name__ == "__main__":
    main()
