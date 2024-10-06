import unittest
from jstring import StringBuffer


class TestStringBuffer(unittest.TestCase):
    """
    Test suite for the StringBuffer class.

    This test suite includes tests for basic StringBuffer operations such as appending, deleting,
    inserting, and more. It ensures that the StringBuffer behaves correctly as a mutable sequence
    of characters.
    """

    def test_constructor_empty(self):
        """
        Tests the constructor with no arguments, ensuring that the StringBuffer is initialized empty
        with a default capacity of 16.
        """
        sb = StringBuffer()
        self.assertEqual(sb.toString(), "")
        self.assertEqual(sb.capacity(), 16)

    def test_constructor_with_string(self):
        """
        Tests the constructor with an initial string, ensuring that the StringBuffer contains the
        string and has the correct length.
        """
        sb = StringBuffer("Hello")
        self.assertEqual(sb.toString(), "Hello")
        self.assertEqual(sb.length(), 5)

    def test_append(self):
        """
        Tests appending strings to the StringBuffer, ensuring that the content is correctly appended.
        """
        sb = StringBuffer("Hello")
        sb.append(" World")
        self.assertEqual(sb.toString(), "Hello World")

    def test_charAt(self):
        """
        Tests retrieving a character at a specific index using charAt.
        """
        sb = StringBuffer("Hello")
        self.assertEqual(sb.charAt(1), "e")

    def test_ensureCapacity(self):
        """
        Tests the ensureCapacity method, ensuring that the capacity is correctly expanded.
        """
        sb = StringBuffer("Hello")
        sb.ensureCapacity(50)
        self.assertEqual(sb.capacity(), 50)

    def test_trimToSize(self):
        """
        Tests the trimToSize method, ensuring that the capacity is reduced to match the current length.
        """
        sb = StringBuffer("Hello World")
        sb.trimToSize()
        self.assertEqual(sb.capacity(), 11)

    def test_delete(self):
        """
        Tests deleting a range of characters from the StringBuffer.
        """
        sb = StringBuffer("Hello World")
        sb.delete(5, 11)
        self.assertEqual(sb.toString(), "Hello")

    def test_deleteCharAt(self):
        """
        Tests deleting a character at a specific index from the StringBuffer.
        """
        sb = StringBuffer("Hello")
        sb.deleteCharAt(1)
        self.assertEqual(sb.toString(), "Hllo")

    def test_indexOf(self):
        """
        Tests finding the index of the first occurrence of a substring.
        """
        sb = StringBuffer("Hello World")
        self.assertEqual(sb.indexOf("World"), 6)

    def test_lastIndexOf(self):
        """
        Tests finding the index of the last occurrence of a substring.
        """
        sb = StringBuffer("Hello World World")
        self.assertEqual(sb.lastIndexOf("World"), 12)

    def test_insert(self):
        """
        Tests inserting a string at a specific offset in the StringBuffer.
        """
        sb = StringBuffer("Hello World")
        sb.insert(6, "Beautiful ")
        self.assertEqual(sb.toString(), "Hello Beautiful World")

    def test_setCharAt(self):
        """
        Tests setting a character at a specific index in the StringBuffer.
        """
        sb = StringBuffer("Hello")
        sb.setCharAt(1, "a")
        self.assertEqual(sb.toString(), "Hallo")

    def test_setLength(self):
        """
        Tests setting the length of the StringBuffer. If the new length is less than the current length,
        the content is truncated. If the new length is greater, the content is padded with null characters.
        """
        sb = StringBuffer("Hello")
        sb.setLength(3)
        self.assertEqual(sb.toString(), "Hel")
        sb.setLength(5)
        self.assertEqual(sb.toString(), "Hel\0\0")  # or "Hel  " depending on padding character used

    def test_reverse(self):
        """
        Tests reversing the content of the StringBuffer.
        """
        sb = StringBuffer("Hello")
        sb.reverse()
        self.assertEqual(sb.toString(), "olleH")

    def test_replace(self):
        """
        Tests replacing a range of characters in the StringBuffer with a new string.
        """
        sb = StringBuffer("Hello World")
        sb.replace(6, 11, "Python")
        self.assertEqual(sb.toString(), "Hello Python")


if __name__ == "__main__":
    unittest.main()
