# py_dutch_numerals

py_dutch_numerals is a Python package that parses and converts Dutch written numbers into their numeric equivalents, supporting numbers up to one million.

## Installation

You can install py_dutch_numerals using pip:

```
pip install py_dutch_numerals
```

## Usage

Here's a basic example of how to use py_dutch_numerals:

```python
from py_dutch_numerals import tel

# Convert a Dutch number to an integer
result = tel("driehonderdvijfenveertig")
print(result)  # Output: 345

# It also handles larger numbers
result = tel("een miljoen tweehonderdduizend")
print(result)  # Output: 1200000
```

## Features

- Parses Dutch written numbers and converts them to integers
- Supports numbers up to one million
- Handles compound numbers (e.g., "eenentwintig" for 21)
- Uses ANTLR4 for robust parsing

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License - see the [LICENSE](LICENSE) file for details.

## Author

Jeroen Bloemscheer

## Acknowledgments

- This project uses ANTLR4 for parsing
- Inspired by the need for processing Dutch numerical text in various applications

## Support

If you encounter any problems or have any questions, please open an issue on the [GitHub repository](https://github.com/grootstebozewolf/py_dutch_numerals/issues).