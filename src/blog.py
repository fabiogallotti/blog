""" The Blog class. """

from post import Post

class Blog:
    """ The Blog class. """
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        return "{} by {} ({} post{})".format(self.title,
                                             self.author,
                                             len(self.posts),
                                             "s" if len(self.posts) != 1 else "")

    def create_post(self, title, content):
        """ Creates a post in the blog. """
        self.posts.append(Post(title, content))

    def json(self):
        """ Returns the json representation of a blog."""
        return {
            "title": self.title,
            "author": self.author,
            "posts": [post.json() for post in self.posts],
        }
