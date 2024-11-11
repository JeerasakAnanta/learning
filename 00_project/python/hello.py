import random

class DemoRandom:
    def generate_numbers(self, count):
        return [random.randint(0, 99) for _ in range(count)]

def main():
    demo = DemoRandom()
    numbers = demo.generate_numbers(100)
    for num in numbers:
        print(num)

main()
