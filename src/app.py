"""
The main functionality of the app.
"""
from src.blog import Blog

MENU_PROMPT = """Enter:
- 'c' to create a blog
- 'l' to list blogs
- 'r' to read one
- 'p' to create a post
- 'q' to quit
Your choice: """

POST_TEMPLATE = """
--- {} ---

{}

"""

blogs = dict()

def menu():
    """ The menu of the app. """
    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != "q":
        if selection == "c":
            ask_create_blog()
        elif selection == "l":
            print_blogs()
        elif selection == "r":
            ask_read_blog()
        elif selection == "p":
            ask_create_post()
        selection = input(MENU_PROMPT)

def print_blogs():
    """ Print the available blogs. """
    for blog in blogs.values():
        print("- {}".format(blog))

def ask_create_blog():
    """Ask to the user the blog title and the author."""
    title = input("Insert the blog title: ")
    author = input("Insert your name: ")

    blogs[title] = Blog(title, author)

def ask_read_blog():
    """Ask to the user the blog he want to read."""
    title = input("Insert the blog title you want to read: ")

    print_posts(blogs[title])

def print_posts(blog):
    """Print the content of a blog."""
    for post in blog.posts:
        print_post(post)

def print_post(post):
    """Print the content of a post."""
    print(POST_TEMPLATE.format(post.title, post.content))

def ask_create_post():
    """Let the user create a post in a blog."""
    blog_name = input("Insert the blog title where you want to create the post: ")
    title = input("Insert the post title: ")
    content = input("Insert the content of the post: ")

    blogs[blog_name].create_post(title, content)

if __name__ == "__main__":
    menu()
