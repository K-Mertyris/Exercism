# Source

The instructions for this exercise can be found on the Exercism website. Please visit their website for more information. The group has done an AMAZING job at creating a resource to learn coding.

## Links

Resource links:

- [Exercism Website](https://exercism.org/)
- [Python Track](https://exercism.org/tracks/python)
- [Strings Concept](https://exercism.org/tracks/python/concepts/strings)
- [Exercise link](https://exercism.org/tracks/python/exercises/little-sisters-vocab)

## Requirements

Requirements for this exercise:

1. Add a prefix to a word
2. Add prefixes to word groups
3. Remove a suffix from a word
4. Extract and transform a word

## Current Status

Most recent updates shown first.

### 2021-09-24

- **Status**: In Progress
- **Notes**: Putting the code in the program based on the pseudocode. Had to change a couple things in the pseudocode as it forced me to read the directions again and get clarification.
  - **Results**: 1 test passed, 15 tests failed
  - **Notes**: I'm getting the outputs I expect, but getting errors from Exercism (pasted below in the `Function Results` bullet)
  - **Function Results**:
    - `add_prefix_un`: Passed
    - `make_word_groups`: Failed

    - ```python
      CODE RUN

      input_data = ['auto', 'didactic', 'graph', 'mate', 'chrome', 'centric', 'complete',
                    'echolalia', 'encoder', 'biography']
      
      result_data = ('auto :: autodidactic :: autograph :: automate :: autochrome :: '
                     'autocentric :: autocomplete :: autoecholalia :: autoencoder :: '
                     'autobiography')

      self.assertEqual(make_word_groups(input_data), result_data,msg=f'Expected {result_data} but got something else instead.')
      
      TEST FAILURE

      AttributeError: 'list' object has no attribute 'split'
      ```

    - `remove_suffix_ness`: Failed

    - ```python
      CODE RUN
      
      input_data = ["heaviness", "sadness", "softness", "crabbiness", "lightness", "artiness", "edginess"]
      result_data = ["heavy", "sad", "soft", 'crabby', 'light', 'arty', 'edgy']
      number_of_variants = range(1, len(input_data) + 1)
      
      for variant, word, result in zip(number_of_variants, input_data, result_data):
        with self.subTest(f"variation #{variant}", word=word, result=result):
          self.assertEqual(remove_suffix_ness(word), result,
                           msg=f'Expected: {result} but got a different word instead.')
      
      TEST FAILURE
      
      AssertionError: 'ness' != 'heavy'
      - ness
      + heavy
        : Expected: heavy but got a different word instead.
      ```

    - `noun_to_verb`: Failed

    - ```python
      CODE RUN
      
      input_data = ['Look at the bright sky.',
              'His expression went dark.',
              'The bread got hard after sitting out.',
              'The butter got soft in the sun.',
              'Her face was filled with light.',
              'The morning fog made everything damp with mist.',
              'He cut the fence pickets short by mistake.',
              'Charles made weak crying noises.',
              'The black oil got on the white dog.']
      index_data = [-2, -1, 3, 3, -1, -3, 5, 2, 1]
      result_data = ['brighten', 'darken', 'harden', 'soften',
                     'lighten', 'dampen', 'shorten', 'weaken', 'blacken']
      number_of_variants = range(1, len(input_data) + 1)
      
      for variant, sentence, index, result in zip(number_of_variants, input_data, index_data, result_data):
        with self.subTest(f"variation #{variant}", sentence=sentence, index=index, result=result):
          self.assertEqual(noun_to_verb(sentence, index), result,
                           msg=f'Expected: {result} but got a different word instead.')
      
      TEST FAILURE
      
      AssertionError: 'dark.en' != 'darken'
      - dark.en
      ?     -
      + darken
       : Expected: darken but got a different word instead.
      ```

### 2021-09-23

- **Status**: In Progress
- **Notes**: Updating `.md` files to conform to standards (need to find those standards so I can add linting to my IDE). Created pseudocode in [`strings.md`](strings.md). Added initial docstring to [`strings.py`](strings.py), trying to figure out a standard for myself there too.
- **Misc**: It **seems** like doing it this way (creating setup files -> writing pseudocode -> coding) will take me longer overall, but I feel a lot better about what I will be coding because I have a better understanding of my goal. It may not be necessary later, especially with simpler functions w/in an app, but I'm going to stick with it for a bit to see how it feels overall and also see if it makes it easier for others to follow my thought process. It may also assist with refactoring when I come back and cycle through after I've been at this for a couple months.
- **Music**: Jason Lewis - Mind Amend: [Peak Focus Upbeat Study Music Mix With Isochronic Tones](https://www.youtube.com/watch?v=ZCq1FPGi8lU)

### 2021-09-22

- **Status**: In progress
- **Notes**: Adding basic files - `README.md`, [`strings.md`](strings.md), [`strings.py`](strings.py). Setting up environment for coding:
  - `strings.py`: Copying code from Exercism exercise to IDE
  - `strings.md`: Creating structure for pseudocode
