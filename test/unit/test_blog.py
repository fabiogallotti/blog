"""Tests for the blog class."""

from blog import Blog

def test_create_blog():
    """Test the creation of a blog."""
    blog = Blog("Test", "Test Author")

    assert blog.title == "Test"
    assert blog.author == "Test Author"
    assert blog.posts == []

def test_repr():
    """Test the __repr__ function."""
    blog = Blog("Test", "Test Author")
    blog2 = Blog("My Day", "Fabio")

    assert blog.__repr__() == "Test by Test Author (0 posts)"
    assert blog2.__repr__() == "My Day by Fabio (0 posts)"

def test_repr_multiple_posts():
    """Test the __repr__ function with multiple posts."""
    blog = Blog("Test", "Test Author")
    blog.posts = ["test"]
    blog2 = Blog("My Day", "Fabio")
    blog2.posts = ["test", "another"]

    assert blog.__repr__() == "Test by Test Author (1 post)"
    assert blog2.__repr__() == "My Day by Fabio (2 posts)"

def test_json():
    """Test the json representation of a blog."""
    blog = Blog("Test", "Test Author")
    blog.create_post("Test", "Test Content")
    expected = {
        "title": "Test",
        "author": "Test Author",
        "posts": [{"title": "Test", "content": "Test Content"}],
    }

    assert blog.json() == expected
