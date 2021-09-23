# Source

The instructions for this exercise can be found on the Exercism website. Please visit their website for more information. The group has done an AMAZING job at creating a resource to learn coding.

## Links

Resource links:

- [Exercism Website](https://exercism.org/)
- [Python Track](https://exercism.org/tracks/python)
- [Numbers Concept](https://exercism.org/tracks/python/concepts/numbers)
- [Exercise link](https://exercism.org/tracks/python/exercises/currency-exchange)

## Requirements

Requirements for this exercise:

1. Estimate value after exchange
2. Calculate currency left after an exchange
3. Calculate value of bills
4. Calculate number of bills
5. Calculate value after exchange
6. Calculate unexchangeable value

## Current Status

2021-09-20:

- Status: In progress
- Notes: After running the checks, the final two requirements are failing. Will need to circle back, pseudocode them and try again.

2021-09-21:

- Status: In progress
- Notes:
  - First PR tonight - added pseudocode for the `exchangable_value` function.
  - Second PR tonight - coded solution based on pseudocode
    - Result: Pseudocode is correct, coding followed pseudocode, tests passed. Keeping pseudocode in until all tests pass, then removing all pseudocode for final commit.
  - Third PR tonight - added pseudocode for the `unexchangeable_value` function

2021-09-22:

- Status: Completed
- Notes:
  - Finished updating code to pass all tests. The error that I was running into was that I forgot to **store** the final variable after casting it as an `int`. Once that minor change was made, all tests passed.
  - Creating an `exchange.md` file to capture all the pseudocode for the app so I can move it out of the main app and just have the code and brief comments contained in this version of the app.
