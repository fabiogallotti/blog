"""Tests for the app."""

from unittest.mock import patch
import pytest
import src.app
from src.blog import Blog
from src.post import Post


@pytest.fixture(autouse=True)
def setup_blog():
    """Initialize a blog for all tests."""
    blog = Blog("Test", "Test Author")
    src.app.blogs = {"Test": blog}

def test_menu_prints_blogs():
    """Tests if the menu prints the blogs."""
    with patch("src.app.print_blogs") as mocked_print_blogs:
        with patch("builtins.input", return_value="q"):
            src.app.menu()
            mocked_print_blogs.assert_called()

def test_menu_prints_prompt():
    """Tests if the menu prints the menu prompt."""
    with patch("builtins.input", return_value="q") as mocked_input:
        src.app.menu()
        mocked_input.assert_called_with(src.app.MENU_PROMPT)

def test_menu_calls_ask_create_blog():
    """Tests if the menu calls the ask create blog function."""
    with patch("builtins.input") as mocked_input:
        mocked_input.side_effect = ("c", "Test Blog Title", "Test Author", "q")
        src.app.menu()

        assert src.app.blogs["Test Blog Title"] is not None

def test_menu_calls_print_blogs():
    """Tests if the menu calls the print blog function."""
    with patch("builtins.input") as mocked_input:
        with patch("src.app.print_blogs") as mocked_print_blogs:
            mocked_input.side_effect = ("l", "q")
            src.app.menu()

            mocked_print_blogs.assert_called()

def test_menu_calls_ask_read_blog():
    """Tests if the menu calls the ask read blog function."""
    with patch("builtins.input") as mocked_input:
        with patch("src.app.ask_read_blog") as mocked_ask_read_blog:
            mocked_input.side_effect = ("r", "q")
            src.app.menu()

            mocked_ask_read_blog.assert_called()

def test_menu_calls_ask_create_post():
    """Tests if the menu calls the ask create post function."""
    with patch("builtins.input") as mocked_input:
        with patch("src.app.ask_create_post") as mocked_ask_create_post:
            mocked_input.side_effect = ("p", "q")
            src.app.menu()

            mocked_ask_create_post.assert_called()

def test_print_blogs():
    """Tests the print blogs function."""
    with patch("builtins.print") as mocked_print:
        src.app.print_blogs()
        mocked_print.assert_called_with("- Test by Test Author (0 posts)")

def test_ask_create_blog():
    """Tests the ask create blog function."""
    with patch("builtins.input") as mocked_input:
        mocked_input.side_effect = ("Test", "Test Author")
        src.app.ask_create_blog()
        assert src.app.blogs.get("Test") is not None

def test_ask_read_blog():
    """Tests the ask read blog function."""
    with patch("builtins.input", return_value="Test"):
        with patch("src.app.print_posts") as mocked_print_posts:
            src.app.ask_read_blog()
            mocked_print_posts.assert_called_with(src.app.blogs["Test"])

def test_print_posts():
    """Tests the print posts function."""
    src.app.blogs["Test"].create_post("Test Post", "Test Content")
    with patch("src.app.print_post") as mocked_print_post:
        src.app.print_posts(src.app.blogs["Test"])
        mocked_print_post.assert_called_with(src.app.blogs["Test"].posts[0])

def test_print_post():
    """Tests the print post function."""
    post = Post("Test Post", "Test Content")
    expected_print = """
--- Test Post ---

Test Content

"""
    with patch("builtins.print") as mocked_print:
        src.app.print_post(post)
        mocked_print.assert_called_with(expected_print)

def test_ask_create_post():
    """Tests the ask create post function."""
    with patch("builtins.input") as mocked_input:
        mocked_input.side_effect = ("Test", "Test Post", "Test Content")
        src.app.ask_create_post()

        assert src.app.blogs["Test"].posts[0].title == "Test Post"
        assert src.app.blogs["Test"].posts[0].content == "Test Content"
