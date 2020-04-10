# Class Notes:

## Section 2 (Intro)
- Python usually uses Interpreter (goes line by line), not compiler (they take entire code and turns to machine code).
- cpython is Interpreter. Creates bytecode (`LOAD_GLOBAL` etc). Uses cypython VM to convert to 0s and 1s.
- Python is slower than C, C#, Java, but good at programmer productivity.

## Section 3 (Basics)
- 4 things to learn any language
    - Terms
    - Data Types
    - Actions (aka functions)
    - Best Practices
- Fundamental Data types: (a value in Python)
    - ` int, float, bool, str, list, tuple, set, dict `
- Classes (custom types)
    - `Supercar`
- Specialized Data Types (Special packages and modules)
- None (i.e. nothing - absence of value)

Operator Precedence - BODMAS - `(), **, */, +- `

### Best practices of naming variables
- <b>snake_case</b> (all small with _ instead of spaces)
- Start with lowercase or underscore (_variable = private variable)
- Case sensitive
- Good practice for constants - Do all caps with underscore (`PI = 3.14`)
- <b>Dunder variables</b>
    - Typically used to store metadata or are built into the system
    - Starts with 2 Underscores - Do not create them! eg: `__init__`
- Python uses `None` instead of `null`
- Refer main.py from Section3 for below:
- <b>String</b>
- <b>List</b>
- <b>Dictionary</b>
- <b>Tuple</b>
- <b>Sets</b>

## Section 4 (Basics II)
- if, else, and elif
- <b>Ternary Operator</b>
- A method is a function that lives inside a class (Unsure)
- == checks value, ```'a' is 'b'``` checks location in memory
- ```break, continue, pass``` (pass does nothing; but good for placeholder inside loops)
- Parameters- When defining a function (Generic) ; Arguments- Values when calling a function
- ```@classmethod```, ```@staticmethod```
- Docstrings (''' This is a docstring ''')

## Section 6 (OOP)
- OOP- A paradigm to structure code. Break down into little objects.
- Class- BluePrint; Objects- Instances (A class can be instantiated i.e. Create an object/an instance)
- 4 Pillars of OOP:
    - <b>Encapsulation</b>
        - Binding of data and functions that manipulate that data (Player- name, age, run())
    - <b>Abstraction</b>
        - Hiding/abstracting information and giving only that's necessary
    - <b>Inheritance</b>
        - Allows new objects to take on the properties of existing objects
    - <b>Polymorphism</b>
        - Many forms
        - Ways in which object classes can share the share method names, but behaves differently based on what object calls them (attack() by Archer different from attack() by Wizard)
- <b>Dunder methods</b>
- <b>MRO- Method Resolution Order</b>

## Section 6 (Functional Programming)
- Functional Programming (separate data and functions)
- Instead of 4 pillars - It's just "Pure functions"
    - Example: [1,2,3] -> f() -> [2,4,6]
- A function should not have a 'side effect'
- Functions- map(), filter(), zip(), reduce()
- Lambda expressions
- Comprehensions (list/set/dictionary comprehensions)

## Section 7 (Decorators)
-  Higher Order Functions - a function that either returns function, or uses func as parameter. Eg: map, reduce