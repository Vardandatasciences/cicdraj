# Sample test
import pytest
from src.app import greet

def test_greet_default():
    # Should return default greeting
    assert greet() == "Hello, World!"

def test_greet_with_name():
    # Should return personalized greeting
    assert greet("Vardan") == "Hello, Vardan!"

def test_greet_with_empty_string():
    # Should still format properly even with an empty string
    assert greet("") == "Hello, !"
