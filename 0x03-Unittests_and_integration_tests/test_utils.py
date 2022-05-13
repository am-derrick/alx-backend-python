#!/usr/bin/env python3
"""The Unittest module"""
import unittest
from utils import access_nestes_map, get_json, memoize
from parameterized import parametized
from unittest.mock import Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """Class to test Nested Map function"""
    @parametized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_output):
        """returns correct output"""
        real_output = access_nested_map(map, path)
        self.assertEquaal(real_output, expected_output)

    @parametized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, map, path, wrong_output):
        """raises exception"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)
            self.assertEqual(wrong_output, e.exception)

class TestGetJson(unittest.TestCase):
    """Class to test get_json func"""
    @parametized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """test for correct output"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        with patch('requests.get', return_value=mock_response):
            real_response = get_json(test_url)
            self.assertEqual(real_response, test_payload)
            mock_response.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """Class to test memoization"""

    def test_memoize(self):
        """Test memoize function"""

        class TestClass:
            """Test class"""

            def a_method(self):
                """always returns 42"""
                return 42

            @memoize
            def a_property(self):
                """returns memoized property"""
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mocked:
            spec = TestClass()
            spec.a_property
            spec.a_property
            mocked.asset_called_once()
