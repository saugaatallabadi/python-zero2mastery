class Toy:
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False
        }

    def __str__(self):  # Overriding str dunder method
        return f'{self.color}'

    def __len__(self):
        return 5

    def __call__(self):
        return 'yes?'

    def __getitem__(self, index):
        return self.my_dict[index]


action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))  # Even this changes to red
print(len(action_figure))
print(action_figure())
print(action_figure['name'])
