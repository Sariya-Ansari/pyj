import unittest
from jstring import String, StringBuilder, StringBuffer

class StringTest(unittest.TestCase):
    """
    Test suite for the String class and its associated functionalities.

    This test suite includes tests for basic string operations such as concatenation, equality,
    case manipulation, searching, and more. It also tests String objects created from StringBuilder
    and StringBuffer.
    """

    def setUp(self):
        """
        Initializes various String instances to be used in the tests.
        """
        self.s0 = String()  # Empty string
        self.s1 = String("hello")  # String from a string literal
        self.s2 = String("world")  # String from a string literal
        self.s3 = String("hello world")  # String from a string literal
        self.s4 = String(["hello", "world"])  # String from a list of strings
        self.s5 = String.from_char_array(['h', 'e', 'l', 'l', 'o'])  # String from character array
        self.s6 = String.from_code_points([104, 101, 108, 108, 111])  # String from code points
        self.sb1 = String(StringBuilder("hello"))  # String from StringBuilder
        self.sb2 = String(StringBuffer("world"))  # String from StringBuffer
        self.sb3 = String(StringBuilder().append("hello").append(" world"))  # Concatenated StringBuilder
        self.sb4 = String(StringBuffer().append("hello").append(" world"))  # Concatenated StringBuffer

    def test_constructor(self):
        """
        Tests the constructor functionality for various initializations.
        """
        self.assertEqual(str(self.s1), "hello")
        self.assertEqual(str(self.s4), "helloworld")
        self.assertEqual(str(self.s5), "hello")
        self.assertEqual(str(self.s6), "hello")

    def test_addition(self):
        """
        Tests string addition (concatenation) with other strings and String objects.
        """
        self.assertEqual(str(self.s1 + self.s2), "helloworld")
        self.assertEqual(str(self.s1 + " world"), "hello world")

    def test_length(self):
        """
        Tests the length method to return the correct string length.
        """
        self.assertEqual(self.s1.length(), 5)

    def test_charAt(self):
        """
        Tests the charAt method for valid and out-of-range indices.
        """
        self.assertEqual(self.s1.charAt(0), 'h')
        with self.assertRaises(IndexError):
            self.s1.charAt(5)

    def test_codePointAt(self):
        """
        Tests the codePointAt method for valid and out-of-range indices.
        """
        self.assertEqual(self.s1.codePointAt(0), ord('h'))
        with self.assertRaises(IndexError):
            self.s1.codePointAt(5)

    def test_compareTo(self):
        """
        Tests string comparison using compareTo.
        """
        self.assertEqual(self.s1.compareTo(self.s2), -1)
        self.assertEqual(self.s1.compareTo(self.s3), -1)
        self.assertEqual(self.s3.compareTo(self.s3), 0)

    def test_contains(self):
        """
        Tests whether a string contains a given substring.
        """
        self.assertTrue(self.s3.contains("hello"))
        self.assertFalse(self.s3.contains("goodbye"))

    def test_equals(self):
        """
        Tests string equality.
        """
        self.assertTrue(self.s1.equals("hello"))
        self.assertFalse(self.s1.equals("world"))

    def test_equalsIgnoreCase(self):
        """
        Tests string equality, ignoring case.
        """
        self.assertTrue(self.s1.equalsIgnoreCase("HELLO"))

    def test_format(self):
        """
        Tests string formatting with placeholders.
        """
        self.assertEqual(str(String.format("Hello, {}!", "world")), "Hello, world!")

    def test_getBytes(self):
        """
        Tests conversion of a string to bytes.
        """
        self.assertEqual(self.s1.getBytes(), b"hello")

    def test_hashCode(self):
        """
        Tests the hashCode method, ensuring it returns the correct hash value.
        """
        self.assertEqual(self.s1.hashCode(), hash("hello"))

    def test_indexOf(self):
        """
        Tests finding the index of a character in the string.
        """
        self.assertEqual(self.s1.indexOf('l'), 2)
        self.assertEqual(self.s1.indexOf('l', 3), 3)

    def test_isEmpty(self):
        """
        Tests if the string is empty.
        """
        self.assertFalse(self.s1.isEmpty())
        self.assertTrue(String().isEmpty())

    def test_lastIndexOf(self):
        """
        Tests finding the last occurrence of a character in the string.
        """
        self.assertEqual(self.s1.lastIndexOf(ord('l')), 3)

    def test_matches(self):
        """
        Tests string matching against a regular expression.
        """
        self.assertTrue(self.s1.matches("hello"))
        self.assertFalse(self.s1.matches("world"))

    def test_replace(self):
        """
        Tests replacing characters in a string.
        """
        self.assertEqual(str(self.s1.replace('l', 'L')), "heLLo")

    def test_split(self):
        """
        Tests splitting the string based on a delimiter.
        """
        self.assertEqual([str(s) for s in self.s3.split(" ")], ["hello", "world"])

    def test_substring(self):
        """
        Tests extracting a substring from the string.
        """
        self.assertEqual(str(self.s1.substring(0, 2)), "he")
        self.assertEqual(str(self.s1.substring(2)), "llo")

    def test_toLowerCase(self):
        """
        Tests converting the string to lowercase.
        """
        self.assertEqual(str(self.s1.toLowerCase()), "hello")

    def test_toUpperCase(self):
        """
        Tests converting the string to uppercase.
        """
        self.assertEqual(str(self.s1.toUpperCase()), "HELLO")

    def test_trim(self):
        """
        Tests trimming leading and trailing whitespace from the string.
        """
        self.assertEqual(str(String("   hello   ").trim()), "hello")

    def test_sb1_type(self):
        """
        Tests that sb1 is an instance of String.
        """
        self.assertIsInstance(self.sb1, String)

    def test_sb2_type(self):
        """
        Tests that sb2 is an instance of String.
        """
        self.assertIsInstance(self.sb2, String)

    def test_sb3_type(self):
        """
        Tests that sb3 is an instance of String.
        """
        self.assertIsInstance(self.sb3, String)

    def test_sb4_type(self):
        """
        Tests that sb4 is an instance of String.
        """
        self.assertIsInstance(self.sb4, String)

    def test_sb1_content(self):
        """
        Tests the content of sb1.
        """
        self.assertEqual(self.sb1, "hello")

    def test_sb2_content(self):
        """
        Tests the content of sb2.
        """
        self.assertEqual(self.sb2, "world")

    def test_sb3_content(self):
        """
        Tests the content of sb3.
        """
        self.assertEqual(self.sb3, "hello world")

    def test_sb4_content(self):
        """
        Tests the content of sb4.
        """
        self.assertEqual(self.sb4, "hello world")

if __name__ == "__main__":
    unittest.main()
