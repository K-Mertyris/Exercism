# Purpose

The purpose of this doc is to hold all the pseudocode for the [`meltdown.py`](meltdown.py) app. This file helps me to create a habit of thinking about the challenge before doing any coding.

Placing the pseudocode in this document will also allow me to keep the codebase clean, ensuring it only has comments for the specific functions called and steps taken.

## Concepts

Concepts highlighted in the introduction:

- `if`, `elif`, and `else` are used to control the flow of execution and make decisions in a program
  - Python 3.9 and below does not offer a case-switch statement
  - Python 3.10 and above does via a variant case-switch statement called `pattern matching`
- Conditional statements must resolve to `True` or `False`
- When paired with an `if`, an **optional** `else` code block will be evaluated when `if` returns `False`
  - Using linters, the linter may suggest removing the `else` as it is unecessary **unless** program execution needs to continue regardless of the outcome of the `if` statement
  - Example: if using `if` as a logic gate to return a value, when `if` evaluates as true and returns the value to the calling program, there is no need for an `else`, you can just call the `false` case `return` outside of the `if` statement because if it was true, the function would have exited.
- Boolean operations (`or`, `and`, `not`) can be combined with conditionals for more complex testing

## Pseudocode

Goal: pass all tests without errors

```Python
def is_criticality_balanced(temperature, neutrons_emitted):
    # Pseudocode
    # Read incoming variables
    # Store 'constants'
    #   temp_check = temperature to check against
    #   neutron_check = neutron emissions to check against
    #   product_check = product of temp * neutrons emitted to check against
    # Check if temperature is less than 800
    # Check if neutrons_emitted is greater than 500
    # Check if teperature * neutrons_emitted < 500,000
    # If all above conditions are true, return True
    # Else return False

def reactor_efficiency(voltage, current, theoretical_max_power):
    # Pseudocode
    # Read incoming variables
    # Store variables:
    #   efficiency = (generated_power/theoretical_max_power)*100
    #   generated_power = voltage * current
    # Check percentage_value against different cases and return a value based on calculated efficiency
    #   efficiency >= .8, return green
    #   efficiency >= .6 and efficiency < .8, return orange
    #   efficiency >= .3 and efficiency < .6, return red
    #   efficiency < .3, return black

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    # Pseudocode
    # Read incoming variables
    # Test:
    #   If temperature * neutrons_produced_per_second < 90% of threshold, return `LOW`
    #   If temperature * neutrons_produced_per_second > 90% of threshold and < 100% of threshold, return `NORMAL`
    #   If neither of the cases above are true, return `DANGER`

```
