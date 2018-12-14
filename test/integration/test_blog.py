import pytest
from src.blog import Blog

class TestBlog():
    def test_create_post_in_blog(self):
        blog = Blog("Test", "Test Author")
        blog.create_post("Test Post", "Test Content")

        assert len(blog.posts) == 1
        assert blog.posts[0].title == "Test Post"
        assert blog.posts[0].content == "Test Content"

    def test_json_no_posts(self):
        blog = Blog("Test", "Test Author")
        expected = {
            "title": "Test",
            "author": "Test Author",
            "posts": []
        }

        assert blog.json() == expected

    def test_json(self):
        blog = Blog("Test", "Test Author")
        blog.create_post("Test Post", "Test Content")
        expected = {
            "title": "Test",
            "author": "Test Author",
            "posts": [
                {
                    "title": "Test Post",
                    "content": "Test Content"
                }
            ]
        }

        assert blog.json() == expected
