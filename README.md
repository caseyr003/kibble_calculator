# Kibble Calculator

## Overview

The Kibble Calculator is a Python 3 project that helps you determine the amount of dog food to order for the next month based on the number of dogs you have and the leftover kibble from the previous month.

## Requirements

Python 3: This project is developed in Python 3.

## Getting Started

Follow these steps to use the Kibble Calculator in your Python project:

Clone the Repository:

```
bash
git clone https://github.com/caseyr003/kibble_calculator.git
cd kibble_calculator
```

Usage Example:

You can use the kibble_amount function in your Python code to calculate the amount of dog food to order. Here's an example of how to use it:

```python
from kibble_calculator import kibble_amount

dogs = {'small': 2, 'medium': 3, 'large': 1}
leftover = 5.0

recommended_order = kibble_amount(dogs, leftover)
print(f"Recommended order amount: {recommended_order} lbs")
```

## Running Tests

The tests are ran using Github Actions after changes are pushed to the repository. They can also be ran locally with the following command:

```bash
python -m unittest
```
