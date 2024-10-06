import unittest
from jstring import Character


class TestCharacter(unittest.TestCase):
    """
    Test suite for the Character class.

    This suite tests the methods and functionalities of the Character class,
    including character comparison, equality, case conversion, and Unicode-related functions.
    """

    def test_charValue(self):
        """
        Test that charValue returns the correct character for a Character instance.
        """
        c = Character('a')
        self.assertEqual(c.charValue(), 'a')

    def test_str(self):
        """
        Test that the string representation of a Character instance is correct.
        """
        c = Character('b')
        self.assertEqual(str(c), 'b')

    def test_compareTo(self):
        """
        Test the compareTo method, ensuring it correctly compares Character instances.
        """
        c1 = Character('a')
        c2 = Character('b')
        self.assertTrue(c1.compareTo(c2) < 0)
        self.assertTrue(c2.compareTo(c1) > 0)
        self.assertTrue(c1.compareTo(Character('a')) == 0)

    def test_hashCode(self):
        """
        Test that hashCode returns the correct hash code for the character.
        """
        c = Character('a')
        self.assertEqual(c.hashCode(), ord('a'))

    def test_equals(self):
        """
        Test the equals method to verify equality between Character instances.
        """
        c1 = Character('a')
        c2 = Character('a')
        c3 = Character('b')
        self.assertTrue(c1.equals(c2))
        self.assertFalse(c1.equals(c3))
        self.assertFalse(c1.equals('a'))

    def test_isLetter(self):
        """
        Test the isLetter static method, which checks if a character is a letter.
        """
        self.assertTrue(Character.isLetter('a'))
        self.assertFalse(Character.isLetter('1'))

    def test_isDigit(self):
        """
        Test the isDigit static method, which checks if a character is a digit.
        """
        self.assertTrue(Character.isDigit('1'))
        self.assertFalse(Character.isDigit('a'))

    def test_isWhitespace(self):
        """
        Test the isWhitespace static method, which checks if a character is a whitespace.
        """
        self.assertTrue(Character.isWhitespace(' '))
        self.assertFalse(Character.isWhitespace('a'))

    def test_isLowerCase(self):
        """
        Test the isLowerCase static method, which checks if a character is lowercase.
        """
        self.assertTrue(Character.isLowerCase('a'))
        self.assertFalse(Character.isLowerCase('A'))

    def test_isUpperCase(self):
        """
        Test the isUpperCase static method, which checks if a character is uppercase.
        """
        self.assertTrue(Character.isUpperCase('A'))
        self.assertFalse(Character.isUpperCase('a'))

    def test_isTitleCase(self):
        """
        Test the isTitleCase static method, which checks if a character is title case.
        """
        self.assertTrue(Character.isTitleCase('A'))
        self.assertFalse(Character.isTitleCase('a'))

    def test_toLowerCase(self):
        """
        Test the toLowerCase static method, which converts a character to lowercase.
        """
        self.assertEqual(Character.toLowerCase('A'), 'a')

    def test_toUpperCase(self):
        """
        Test the toUpperCase static method, which converts a character to uppercase.
        """
        self.assertEqual(Character.toUpperCase('a'), 'A')

    def test_codePointAt(self):
        """
        Test the codePointAt static method, which returns the code point of a character.
        """
        self.assertEqual(Character.codePointAt('abc', 1), ord('b'))

    def test_codePointBefore(self):
        """
        Test the codePointBefore static method, which returns the code point before a specified index.
        """
        self.assertEqual(Character.codePointBefore('abc', 2), ord('b'))

    def test_charCount(self):
        """
        Test the charCount static method, which returns the number of char values needed to represent a code point.
        """
        self.assertEqual(Character.charCount(0x10000), 2)
        self.assertEqual(Character.charCount(0xFFFF), 1)

    def test_digit(self):
        """
        Test the digit static method, which converts a character to a digit in a specified radix.
        """
        self.assertEqual(Character.digit('A', 16), 10)
        self.assertEqual(Character.digit('1', 10), 1)

    def test_forDigit(self):
        """
        Test the forDigit static method, which converts a digit to a character in a specified radix.
        """
        self.assertEqual(Character.forDigit(10, 16), 'a')  # 10 in base 16 is 'a'
        self.assertEqual(Character.forDigit(1, 10), '1')  # 1 in base 10 is '1'
        self.assertEqual(Character.forDigit(36, 37), '\0')  # Invalid digit/radix returns '\0'

    def test_isSurrogate(self):
        """
        Test the isSurrogate static method, which checks if a character is a surrogate.
        """
        self.assertTrue(Character.isSurrogate('\uD800'))
        self.assertFalse(Character.isSurrogate('a'))

    def test_highSurrogate(self):
        """
        Test the highSurrogate static method, which returns the high surrogate for a code point.
        """
        self.assertEqual(Character.highSurrogate(0x10400), '\uD801')

    def test_lowSurrogate(self):
        """
        Test the lowSurrogate static method, which returns the low surrogate for a code point.
        """
        self.assertEqual(Character.lowSurrogate(0x10400), '\uDC00')

    def test_Subset(self):
        """
        Test the Subset nested class.
        """
        subset = Character.Subset('example')
        self.assertEqual(subset.name, 'example')

    def test_UnicodeBlock(self):
        """
        Test the UnicodeBlock nested class.
        """
        block = Character.UnicodeBlock('exampleBlock')
        self.assertEqual(block.name, 'exampleBlock')

    def test_UnicodeScript(self):
        """
        Test the UnicodeScript nested class.
        """
        script = Character.UnicodeScript('exampleScript')
        self.assertEqual(script.name, 'exampleScript')


if __name__ == '__main__':
    unittest.main()
