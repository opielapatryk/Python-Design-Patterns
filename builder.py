from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):
    """
    The Builder interface specifies methods for creating the different parts of
    the report objects.
    """

    @property
    @abstractmethod
    def report(self) -> None:
        pass

    @abstractmethod
    def add_title(self, title: str) -> None:
        pass

    @abstractmethod
    def add_header(self, header: str) -> None:
        pass

    @abstractmethod
    def add_content(self, content: str) -> None:
        pass

class ConcreteBuilder1(Builder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """

    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank report object, which is
        used in further assembly.
        """
        self.reset()

    def reset(self) -> None:
        self._report = Report1()

    @property
    def report(self) -> Report1:
        """
        Concrete Builders are supposed to provide their own methods for
        retrieving results. That's because various types of builders may create
        entirely different reports that don't follow the same interface.
        Therefore, such methods cannot be declared in the base Builder interface
        (at least in a statically typed programming language).

        Usually, after returning the end result to the client, a builder
        instance is expected to be ready to start producing another report.
        That's why it's a usual practice to call the reset method at the end of
        the `getreport` method body. However, this behavior is not mandatory,
        and you can make your builders wait for an explicit reset call from the
        client code before disposing of the previous result.
        """
        report = self._report
        self.reset()
        return report

    def add_title(self, title: str) -> None:
        self._report.add(f"Title: {title}")

    def add_header(self, header: str) -> None:
        self._report.add(f"Header: {header}")

    def add_content(self, content: str) -> None:
        self._report.add(f"Content: {content}")


class Report1():
    """
    It makes sense to use the Builder pattern only when your reports are quite
    complex and require extensive configuration.

    Unlike in other creational patterns, different concrete builders can produce
    unrelated reports. In other words, results of various builders may not
    always follow the same interface.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def show_report(self) -> None:
        print("Generated Report:")
        for part in self.parts:
            print(part)


class Director:
    """
    The Director is only responsible for executing the building steps in a
    particular sequence. It is helpful when producing reports according to a
    specific order or configuration. Strictly speaking, the Director class is
    optional, since the client can control builders directly.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
        The Director works with any builder instance that the client code passes
        to it. This way, the client code may alter the final type of the newly
        assembled report.
        """
        self._builder = builder

    """
    The Director can construct several report variations using the same
    building steps.
    """

    def build_minimal_viable_report(self, title: str) -> None:
        self.builder.add_title(title)

    def build_full_featured_report(self,title: str, header: str, content: str) -> None:
        self.builder.add_title(title)
        self.builder.add_header(header)
        self.builder.add_content(content)


if __name__ == "__main__":
    """
    The client code creates a builder object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder object.
    """

    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    director.build_full_featured_report("Monthly Sales Report", "Sales Summary", "Total sales: $10000")
    report = builder.report
    report.show_report()