"""Tests for the post class."""

from src.post import Post

def test_create_post():
    """Test the creation of a post."""
    post = Post("Test", "Test Content")

    assert post.title == "Test"
    assert post.content == "Test Content"

def test_json():
    """Test the json representation of a post."""
    post = Post("Test", "Test Content")
    expected = {"title": "Test", "content": "Test Content"}

    assert expected == post.json()
