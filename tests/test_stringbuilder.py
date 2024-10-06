import unittest
from jstring import StringBuilder


class TestStringBuilder(unittest.TestCase):
    """
    Test suite for the StringBuilder class.

    This test suite includes tests for basic StringBuilder operations such as appending, deleting,
    inserting, and more. It ensures that the StringBuilder behaves correctly as a mutable sequence
    of characters.
    """

    def test_initialization(self):
        """
        Tests the initialization of the StringBuilder with a string, an integer capacity, and with no arguments.
        """
        sb = StringBuilder("Hello")
        self.assertEqual(str(sb), "Hello")
        self.assertEqual(sb.capacity(), 16)

        sb = StringBuilder(10)
        self.assertEqual(sb.capacity(), 10)
        self.assertEqual(str(sb), "")

        sb = StringBuilder()
        self.assertEqual(sb.capacity(), 16)
        self.assertEqual(str(sb), "")

    def test_append(self):
        """
        Tests appending various types (string, integer, boolean) to the StringBuilder.
        """
        sb = StringBuilder("Hello")
        sb.append(" World")
        self.assertEqual(str(sb), "Hello World")

        sb.append(123)
        self.assertEqual(str(sb), "Hello World123")

        sb.append(True)
        self.assertEqual(str(sb), "Hello World123true")

    def test_charAt(self):
        """
        Tests retrieving a character at a specific index using charAt.
        """
        sb = StringBuilder("Hello")
        self.assertEqual(sb.charAt(1), "e")

    def test_codePointAt(self):
        """
        Tests retrieving the Unicode code point of the character at a specific index.
        """
        sb = StringBuilder("Hello")
        self.assertEqual(sb.codePointAt(1), ord("e"))

    def test_codePointBefore(self):
        """
        Tests retrieving the Unicode code point of the character before a specific index.
        """
        sb = StringBuilder("Hello")
        self.assertEqual(sb.codePointBefore(1), ord("H"))

    def test_codePointCount(self):
        """
        Tests counting the number of Unicode code points in a specified text range.
        """
        sb = StringBuilder("Hello")
        self.assertEqual(sb.codePointCount(1, 4), 3)

    def test_delete(self):
        """
        Tests deleting a range of characters from the StringBuilder.
        """
        sb = StringBuilder("Hello World")
        sb.delete(5, 11)
        self.assertEqual(str(sb), "Hello")

    def test_deleteCharAt(self):
        """
        Tests deleting a character at a specific index from the StringBuilder.
        """
        sb = StringBuilder("Hello")
        sb.deleteCharAt(1)
        self.assertEqual(str(sb), "Hllo")

    def test_ensureCapacity(self):
        """
        Tests ensuring the capacity of the StringBuilder.
        """
        sb = StringBuilder("Hello")
        sb.ensureCapacity(50)
        self.assertEqual(sb.capacity(), 50)

    def test_getChars(self):
        """
        Tests copying characters from the StringBuilder into a specified destination list.
        """
        sb = StringBuilder("Hello World")
        dst = [' '] * 5
        sb.getChars(6, 11, dst, 0)
        self.assertEqual(''.join(dst), "World")

    def test_indexOf(self):
        """
        Tests finding the index of the first occurrence of a specified substring.
        """
        sb = StringBuilder("Hello World")
        self.assertEqual(sb.indexOf("World"), 6)
        self.assertEqual(sb.indexOf("world"), -1)

    def test_insert(self):
        """
        Tests inserting a string at a specific offset in the StringBuilder.
        """
        sb = StringBuilder("Hello World")
        sb.insert(6, "Beautiful ")
        self.assertEqual(str(sb), "Hello Beautiful World")

    def test_lastIndexOf(self):
        """
        Tests finding the index of the last occurrence of a specified substring.
        """
        sb = StringBuilder("Hello Hello Hello")
        self.assertEqual(sb.lastIndexOf("Hello"), 12)
        self.assertEqual(sb.lastIndexOf("Hello", 10), 6)

    def test_length(self):
        """
        Tests retrieving the length of the StringBuilder content.
        """
        sb = StringBuilder("Hello")
        self.assertEqual(sb.length(), 5)

    def test_offsetByCodePoints(self):
        """
        Tests calculating the offset of a position by a specified number of code points.
        """
        sb = StringBuilder("Hello")
        self.assertEqual(sb.offsetByCodePoints(1, 2), 3)

    def test_replace(self):
        """
        Tests replacing a range of characters in the StringBuilder with a new string.
        """
        sb = StringBuilder("Hello World")
        sb.replace(6, 11, "Python")
        self.assertEqual(str(sb), "Hello Python")

    def test_reverse(self):
        """
        Tests reversing the content of the StringBuilder.
        """
        sb = StringBuilder("Hello")
        sb.reverse()
        self.assertEqual(str(sb), "olleH")

    def test_setCharAt(self):
        """
        Tests setting a character at a specific index in the StringBuilder.
        """
        sb = StringBuilder("Hello")
        sb.setCharAt(1, 'a')
        self.assertEqual(str(sb), "Hallo")

    def test_setLength(self):
        """
        Tests setting the length of the StringBuilder. If the new length is less than the current length,
        the content is truncated. If the new length is greater, the content is padded with null characters.
        """
        sb = StringBuilder("Hello")
        sb.setLength(3)
        self.assertEqual(str(sb), "Hel")
        sb.setLength(5)
        self.assertEqual(str(sb), "Hel\0\0")

    def test_subSequence(self):
        """
        Tests retrieving a subsequence from the StringBuilder.
        """
        sb = StringBuilder("Hello World")
        self.assertEqual(sb.subSequence(6, 11), "World")

    def test_substring(self):
        """
        Tests retrieving a substring from the StringBuilder.
        """
        sb = StringBuilder("Hello World")
        self.assertEqual(sb.substring(6, 11), "World")

    def test_trimToSize(self):
        """
        Tests adjusting the capacity of the StringBuilder to match its current size.
        """
        sb = StringBuilder("Hello World")
        sb.trimToSize()
        self.assertEqual(sb.capacity(), 11)


if __name__ == "__main__":
    unittest.main()
