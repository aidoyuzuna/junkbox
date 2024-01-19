class Potato:
    def __init__(self, weight):
        self.weight = weight


class KitchenScale:
    def __init__(self):
        self.total_weight = 0.0

    def scale_put_on(self, potato):
        self.total_weight += potato.weight

    def clear(self):
        self.total_weight = 0.0

    def get_total_weight(self):
        return self.total_weight


def main():
    scale = KitchenScale()
    potato1 = Potato(2.0)
    scale.scale_put_on(potato1)
    potato2 = Potato(3.0)
    scale.scale_put_on(potato2)
    print(scale.get_total_weight())
    scale.clear()
    print(scale.get_total_weight())


if __name__ == "__main__":
    main()
