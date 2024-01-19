class Potato():
    def __init__(self, weight):
        self.weight = weight


class Kitchenscale():
    def __init__(self):
        self.scale = 0

    def put_potato(self, potato):
        self.scale += potato.weight

    def clear(self):
        self.scale = 0

    def get_potato(self):
        return self.scale


def main():
    potato1 = Potato(2.0)
    scale = Kitchenscale()
    scale.put_potato(potato1)
    potato2 = Potato(3.0)
    scale.put_potato(potato2)
    print(scale.get_potato())
    scale.clear()
    print(scale.get_potato())


if __name__ == '__main__':
    main()
