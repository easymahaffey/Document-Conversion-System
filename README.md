# Document Conversion System

## Overview

This project implements a real-world document conversion system using **Abstract Factory** and **Decorator** design patterns. It performs actual file format conversions:

- **PDF → DOCX** using `pdf2docx`
- **DOCX → TXT** using `python-docx`

---

## Design Patterns Used

### Abstract Factory
The Abstract Factory pattern is employed to encapsulate the creation of related document converters. This allows the system to support multiple conversion types (e.g., PDF to DOCX, DOCX to TXT) with a consistent interface and promotes scalability without tightly coupling the client code to specific classes.

- Provides a family of document converters (e.g., PDF to DOCX, DOCX to TXT).
- Enables extension without modifying client code.
- Promotes encapsulation and scalability.

### Decorator
The Decorator pattern adds dynamic behavior (like logging, compression, or encryption) to a converter without modifying its structure. This approach follows the Open/Closed Principle, enabling behavior extension without altering existing code.

- Adds dynamic behaviors like logging without changing converter logic.
- Follows the Open/Closed Principle for flexible enhancement.

---

## How the Implementation Follows SOLID Principles

- **S: Single Responsibility** – Each class has a dedicated function (conversion, decoration, factory creation).
- **O: Open/Closed** – New formats or behaviors can be added via subclasses or decorators.
- **L: Liskov Substitution** – All converters inherit from `DocumentConverter` and can be used interchangeably.
- **I: Interface Segregation** – Only necessary methods are exposed through the `DocumentConverter` interface.
- **D: Dependency Inversion** – Client code uses the abstract `DocumentConverter`, not concrete types.

---

## Installation

```bash
pip install pdf2docx python-docx

## Trade-offs and Alternatives

###Considered:
- **Strategy Pattern** Could support dynamic selection of conversion strategies at runtime.Could support dynamic selection of conversion strategies at runtime.
- **Chain of Responsibility** Could allow chaining conversions (e.g., PDF → DOCX → TXT).
- Using **Observer Pattern** Could notify UI/logging modules of progress, but not required yet.

###Not Used:
- **Singleton** Avoided for converters to keep instances stateless and reusable.
---

## Extensibility

###The architecture allows:

- Adding new converters like DOCX to HTML or TXT to PDF.
- Applying multiple decorators (e.g., logging + encryption).
- Plug-and-play behavior modifications without altering core logic.

---

## Future Enhancements

- Add a GUI or CLI to dynamically choose conversion formats.

---

## Running the Code

```bash
python main.py
