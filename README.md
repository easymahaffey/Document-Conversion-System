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

- While designing the system, I explored a few other patterns that could have added value in certain scenarios. The Strategy Pattern seemed like a good fit if I needed to let users choose conversion methods dynamically at runtime. I also considered the Chain of Responsibility, which would be helpful for automatically chaining multiple conversions—like going from PDF to DOCX and then to TXT. The Observer Pattern was another option, useful for notifying a UI or logging system during conversion progress, but it felt unnecessary at this stage. As for the Singleton Pattern, I decided not to use it for converters. Keeping them stateless and reusable just made more sense—it keeps things flexible and avoids complications if I want to run multiple conversions in parallel later on.

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
