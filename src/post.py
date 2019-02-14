""" The Post class. """


class Post:
    """ The Post class. """

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def json(self):
        """ Returns the json representation of a post. """
        return {"title": self.title, "content": self.content}
