"""Test for the integration Blog - Post. """

from src.blog import Blog


def test_create_post_in_blog():
    """Tests if a post is created in a blog. """
    blog = Blog("Test", "Test Author")
    blog.create_post("Test Post", "Test Content")

    assert len(blog.posts) == 1
    assert blog.posts[0].title == "Test Post"
    assert blog.posts[0].content == "Test Content"


def test_json_no_posts():
    """Tests the json representation without posts. """
    blog = Blog("Test", "Test Author")
    expected = {"title": "Test", "author": "Test Author", "posts": []}

    assert blog.json() == expected


def test_json():
    """Tests the json representation with posts. """
    blog = Blog("Test", "Test Author")
    blog.create_post("Test Post", "Test Content")
    expected = {"title": "Test", "author": "Test Author", "posts": [{"title": "Test Post", "content": "Test Content"}]}
    assert blog.json() == expected
