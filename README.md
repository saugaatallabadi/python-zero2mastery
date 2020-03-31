# Class Notes:

## Section 2
- Python usually uses Interpreter (goes line by line), not compiler (they take entire code and turns to machine code).
- cpython is Interpreter. Creates bytecode (`LOAD_GLOBAL` etc). Uses cypython VM to convert to 0s and 1s.
- Python is slower than C, C#, Java, but good at programmer productivity.

## Section 3
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
    - Starts with 2 Underscores - Do not create them!
- Python uses `None` instead of `null`
- Refer main.py from Section3 for below:
- <b>String</b>
- <b>List</b>
- <b>Dictionary</b>
- <b>Tuple</b>
- <b>Sets</b>

## Section 4
- if, else, and elif
- <b>Ternary Operator</b>
- == checks value, ```'a' is 'b'``` checks location in memory
- ```break, continue, pass``` (pass does nothing; but good for placeholder inside loops)
- Parameters- When defining a function (Generic) ; Arguments- Values when calling a function
- Docstrings (''' This is a docstring ''')