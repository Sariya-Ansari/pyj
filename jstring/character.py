"""
This module provides a `Character` class inspired by the Java `Character` class,
including utility methods for checking character properties and converting case.

The class also defines constants for various character categories, surrogate
pairs, and Unicode ranges. The nested classes `Subset`, `UnicodeBlock`, and
`UnicodeScript` are used to represent different subsets of characters.
"""


class Character:
    """
    A class representing a single character, with utility methods for character
    manipulation and checking properties.

    The `Character` class provides constants for various character categories
    such as uppercase letters, decimal digits, and punctuation. It also includes
    methods to compare characters, convert them to lowercase or uppercase, and
    check if a character belongs to certain categories like letters, digits, or
    whitespace.

    Attributes:
        BYTES (int): The number of bytes used by the character.
        SIZE (int): The size of the character in bits.
        MAX_RADIX (int): The maximum radix value for character conversions.
        MIN_RADIX (int): The minimum radix value for character conversions.
        MAX_CODE_POINT (int): The maximum Unicode code point.
        MIN_CODE_POINT (int): The minimum Unicode code point.
        MAX_VALUE (str): The maximum value of a character.
        MIN_VALUE (str): The minimum value of a character.
        MAX_HIGH_SURROGATE (str): The maximum value of a high surrogate.
        MIN_HIGH_SURROGATE (str): The minimum value of a high surrogate.
        MAX_LOW_SURROGATE (str): The maximum value of a low surrogate.
        MIN_LOW_SURROGATE (str): The minimum value of a low surrogate.
        MIN_SUPPLEMENTARY_CODE_POINT (int): The minimum supplementary code point.

    Field Constants:
        Defines character categories like `COMBINING_SPACING_MARK`, `LOWERCASE_LETTER`, etc.
    """

    # Field Constants
    BYTES = 2
    SIZE = 16
    MAX_RADIX = 36
    MIN_RADIX = 2
    MAX_CODE_POINT = 0x10FFFF
    MIN_CODE_POINT = 0x0000
    MAX_VALUE = '\uFFFF'
    MIN_VALUE = '\u0000'
    MAX_HIGH_SURROGATE = '\uDBFF'
    MIN_HIGH_SURROGATE = '\uD800'
    MAX_LOW_SURROGATE = '\uDFFF'
    MIN_LOW_SURROGATE = '\uDC00'
    MIN_SUPPLEMENTARY_CODE_POINT = 0x10000

    # Character Categories
    COMBINING_SPACING_MARK = 'Mc'
    CONNECTOR_PUNCTUATION = 'Pc'
    CONTROL = 'Cc'
    CURRENCY_SYMBOL = 'Sc'
    DASH_PUNCTUATION = 'Pd'
    DECIMAL_DIGIT_NUMBER = 'Nd'
    DIRECTIONALITY_ARABIC_NUMBER = 'AN'
    DIRECTIONALITY_BOUNDARY_NEUTRAL = 'BN'
    DIRECTIONALITY_COMMON_NUMBER_SEPARATOR = 'CS'
    DIRECTIONALITY_EUROPEAN_NUMBER = 'EN'
    DIRECTIONALITY_EUROPEAN_NUMBER_SEPARATOR = 'ES'
    DIRECTIONALITY_EUROPEAN_NUMBER_TERMINATOR = 'ET'
    DIRECTIONALITY_LEFT_TO_RIGHT = 'L'
    DIRECTIONALITY_LEFT_TO_RIGHT_EMBEDDING = 'LRE'
    DIRECTIONALITY_LEFT_TO_RIGHT_OVERRIDE = 'LRO'
    DIRECTIONALITY_NONSPACING_MARK = 'NSM'
    DIRECTIONALITY_OTHER_NEUTRALS = 'ON'
    DIRECTIONALITY_PARAGRAPH_SEPARATOR = 'B'
    DIRECTIONALITY_POP_DIRECTIONAL_FORMAT = 'PDF'
    DIRECTIONALITY_RIGHT_TO_LEFT = 'R'
    DIRECTIONALITY_RIGHT_TO_LEFT_ARABIC = 'AL'
    DIRECTIONALITY_RIGHT_TO_LEFT_EMBEDDING = 'RLE'
    DIRECTIONALITY_RIGHT_TO_LEFT_OVERRIDE = 'RLO'
    DIRECTIONALITY_SEGMENT_SEPARATOR = 'S'
    DIRECTIONALITY_UNDEFINED = None
    DIRECTIONALITY_WHITESPACE = 'WS'
    ENCLOSING_MARK = 'Me'
    END_PUNCTUATION = 'Pe'
    FINAL_QUOTE_PUNCTUATION = 'Pf'
    FORMAT = 'Cf'
    INITIAL_QUOTE_PUNCTUATION = 'Pi'
    LETTER_NUMBER = 'Nl'
    LINE_SEPARATOR = 'Zl'
    LOWERCASE_LETTER = 'Ll'
    MATH_SYMBOL = 'Sm'
    MODIFIER_LETTER = 'Lm'
    MODIFIER_SYMBOL = 'Sk'
    NON_SPACING_MARK = 'Mn'
    OTHER_LETTER = 'Lo'
    OTHER_NUMBER = 'No'
    OTHER_PUNCTUATION = 'Po'
    OTHER_SYMBOL = 'So'
    PARAGRAPH_SEPARATOR = 'Zp'
    PRIVATE_USE = 'Co'
    SPACE_SEPARATOR = 'Zs'
    START_PUNCTUATION = 'Ps'
    SURROGATE = 'Cs'
    TITLECASE_LETTER = 'Lt'
    UNASSIGNED = 'Cn'
    UPPERCASE_LETTER = 'Lu'

    # Additional constants for other categories...

    def __init__(self, value):
        """
        Initializes a Character instance with a given value.

        :param value: A single character string.
        :raises ValueError: If the input value is not a single character.
        """
        if len(value) != 1:
            raise ValueError("value must be a single character")
        self.value = value

    def charValue(self):
        """
        Returns the character value of this Character instance.

        :return: The character value as a string.
        """
        return self.value

    def __str__(self):
        """
        Returns a string representation of the Character instance.

        :return: The character value as a string.
        """
        return self.value

    def compareTo(self, anotherCharacter):
        """
        Compares this Character to another Character.

        :param anotherCharacter: The Character to compare with.
        :return: A negative integer, zero, or a positive integer as this Character
                 is less than, equal to, or greater than the specified Character.
        :raises TypeError: If the provided argument is not of type Character.
        """
        if not isinstance(anotherCharacter, Character):
            raise TypeError("Argument must be of type Character")
        return ord(self.value) - ord(anotherCharacter.value)

    def hashCode(self):
        """
        Returns a hash code for this Character instance.

        :return: The hash code of the character value.
        """
        return ord(self.value)

    def equals(self, obj):
        """
        Compares this Character to another object for equality.

        :param obj: The object to compare with.
        :return: True if the objects are equal, otherwise False.
        """
        return isinstance(obj, Character) and self.value == obj.value

    @staticmethod
    def isLetter(ch):
        """
        Determines if the specified character is a letter.

        :param ch: The character to check.
        :return: True if the character is a letter, otherwise False.
        """
        return ch.isalpha()

    @staticmethod
    def isDigit(ch):
        """
        Determines if the specified character is a digit.

        :param ch: The character to check.
        :return: True if the character is a digit, otherwise False.
        """
        return ch.isdigit()

    @staticmethod
    def isWhitespace(ch):
        """
        Determines if the specified character is a whitespace character.

        :param ch: The character to check.
        :return: True if the character is a whitespace, otherwise False.
        """
        return ch.isspace()

    @staticmethod
    def isLowerCase(ch):
        """
        Determines if the specified character is a lowercase letter.

        :param ch: The character to check.
        :return: True if the character is lowercase, otherwise False.
        """
        return ch.islower()

    @staticmethod
    def isUpperCase(ch):
        """
        Determines if the specified character is an uppercase letter.

        :param ch: The character to check.
        :return: True if the character is uppercase, otherwise False.
        """
        return ch.isupper()

    @staticmethod
    def isTitleCase(ch):
        """
        Determines if the specified character is a title case letter.

        :param ch: The character to check.
        :return: True if the character is title case, otherwise False.
        """
        return ch.istitle()

    @staticmethod
    def toLowerCase(ch):
        """
        Converts the specified character to lowercase.

        :param ch: The character to convert.
        :return: The lowercase representation of the character.
        """
        return ch.lower()

    @staticmethod
    def toUpperCase(ch):
        """
        Converts the specified character to uppercase.

        :param ch: The character to convert.
        :return: The uppercase representation of the character.
        """
        return ch.upper()

    @staticmethod
    def codePointAt(a, index):
        """
        Returns the code point value of the character at the specified index in the string.

        :param a: The string containing the character.
        :param index: The index of the character.
        :return: The code point of the character.
        """
        return ord(a[index])

    @staticmethod
    def codePointBefore(a, index):
        """
        Returns the code point value of the character before the specified index in the string.

        :param a: The string containing the character.
        :param index: The index of the character.
        :return: The code point of the character before the specified index.
        """
        return ord(a[index - 1])

    @staticmethod
    def charCount(codePoint):
        """
        Returns the number of char values needed to represent the specified code point.

        :param codePoint: The code point value.
        :return: 2 if the code point is greater than or equal to 0x10000, otherwise 1.
        """
        return 2 if codePoint >= 0x10000 else 1

    @staticmethod
    def digit(ch, radix):
        """
        Converts a character to a digit in the specified radix.

        :param ch: The character to convert.
        :param radix: The radix to use for conversion.
        :return: The integer value of the character in the specified radix.
        """
        return int(ch, radix)

    @staticmethod
    def forDigit(digit, radix):
        """
        Converts an integer digit in the specified radix to a character.

        :param digit: The integer digit.
        :param radix: The radix to use for conversion.
        :return: The character representing the digit in the specified radix, or '\0' if invalid.
        """
        if 0 <= digit < radix <= 36:
            return chr(digit + ord('0')) if digit < 10 else chr(digit - 10 + ord('a'))
        return '\0'

    @staticmethod
    def isSurrogate(ch):
        """
        Determines if the specified character is a surrogate character.

        :param ch: The character to check.
        :return: True if the character is a surrogate, otherwise False.
        """
        return Character.MIN_HIGH_SURROGATE <= ch <= Character.MAX_LOW_SURROGATE

    @staticmethod
    def highSurrogate(codePoint):
        """
        Returns the high surrogate for the specified code point.

        :param codePoint: The code point value.
        :return: The high surrogate character.
        """
        return chr((codePoint >> 10) + 0xD7C0)

    @staticmethod
    def lowSurrogate(codePoint):
        """
        Returns the low surrogate for the specified code point.

        :param codePoint: The code point value.
        :return: The low surrogate character.
        """
        return chr((codePoint & 0x3FF) + 0xDC00)

    # Nested Classes
    class Subset:
        """
        A class representing a subset of Unicode characters.
        """

        def __init__(self, name):
            """
            Initializes a Subset instance with a given name.

            :param name: The name of the subset.
            """
            self.name = name

    class UnicodeBlock:
        """
        A class representing a block of Unicode characters.
        """

        def __init__(self, name):
            """
            Initializes a UnicodeBlock instance with a given name.

            :param name: The name of the Unicode block.
            """
            self.name = name

    class UnicodeScript:
        """
        A class representing a Unicode script.
        """

        def __init__(self, name):
            """
            Initializes a UnicodeScript instance with a given name.

            :param name: The name of the Unicode script.
            """
            self.name = name
