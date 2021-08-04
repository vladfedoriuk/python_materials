class Printer:
    def log(self, *values):
        print(*values)


class FormattedPrinter(Printer):
    def __init__(
        self,
    ):
        super().__init__()

    def log(self, *values):
        print("".join(["*"] * 10))
        super().log(*values)
        print("".join(["*"] * 10))


FormattedPrinter().log([1, 2, 3])
