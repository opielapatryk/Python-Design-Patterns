# Python-Design-Patterns

## Python-Specific Patterns
### Global Object Pattern
Providing a centralized point of access for certain functionalities or resources, used in conjunction with Singleton ensures that only one instance of the object exists throughout the program lifecycles<br>
### Prebound Method Pattern
A powerful technique for offering callables at the top level of your module that share state through a common object<br>
### Sentinel Object Pattern
We use -1 instead of null i.e. if a.find(x) is -1: return <br>

## Creational Patterns
### Abstract Factory
solves the problem of creating entire product families without specifying their concrete classes.<br>

### Singleton
better use Global Object Pattern

### Prototype
can be easily recognized by copy methods

### Builder 
useful when you need to create an object with lots of possible configuration options i.e. "reports generator"

## Structural Patterns
### Adapter
can be used to adopt some classes to work with different foreign objects

### Bridge
especially useful when dealing with cross-platform apps, supporting multiple types of database servers or working with several API providers

### Composite 
used for building tree structure i.e. interface components/graphs, each object of a tree is a part of the same class hierarchy

