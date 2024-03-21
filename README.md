# Python-Design-Patterns

# Gang of Four: Principles <br>
The Composition Over Inheritance Principle
Problem: the subclass explosion
Solution #1: The Adapter Pattern
Solution #2: The Bridge Pattern
Solution #3: The Decorator Pattern
Solution #4: Beyond the Gang of Four patterns
Dodge: “if” statements
Dodge: Multiple Inheritance
Dodge: Mixins
Dodge: Building classes dynamically

# Python-Specific Patterns
The Global Object Pattern
The Constant Pattern
Import-time computation
Dunder Constants
The Global Object Pattern
Global Objects that are mutable
Import-time I/O
The Prebound Method Pattern
Alternatives
The pattern
The Sentinel Object Pattern
Sentinel Value
The Null Pointer Pattern
The Null Object Pattern
Sentinel Objects

# Gang of Four: Creational Patterns
The Abstract Factory Pattern
The Pythonic approach: callable factories
Restriction: outlaw passing callables
Restriction: outlaw passing classes
Generalizing: the complete Abstract Factory
The Builder Pattern
The Builder as convenience
Nuance
Dueling builders
A degenerate case: simulating optional arguments
The Factory Method Pattern
Dodge: use Dependency Injection
Instead: use a Class Attribute Factory
Instead: use an Instance Attribute Factory
Instance attributes override class attributes
Any callables accepted
Implementing
The Prototype Pattern
The problem
Pythonic solutions
Implementing
The Singleton Pattern
Disambiguation
The Gang of Four’s implementation
A more Pythonic implementation
Verdict

# Gang of Four: Structural Patterns
The Composite Pattern
Example: the UNIX file system
On hierarchies
Example: GUI programming with Tkinter
Implementation: to inherit, or not?
The Decorator Pattern
Definition
Implementing: Static wrapper
Implementing: Tactical wrapper
Implementing: Dynamic wrapper
Caveat: Wrapping doesn’t actually work
Hack: Monkey-patch each object
Hack: Monkey-patch the class
Further Reading
The Flyweight Pattern
Factory or Constructor
Implementing

# Gang of Four: Behavioral Patterns
The Iterator Pattern
Iterating with the “for” loop
The pattern: the iterable and its iterator
A twist: objects which are their own iterator
Implementing an Iterable and Iterator
Python’s extra level of indirection