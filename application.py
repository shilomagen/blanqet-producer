from flask import Flask

application = Flask(__name__)


def say_hello(username="World"):
    return '<p>Hello %s!</p>\n' % username


header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service Shalom! Append a username
    to the URL (for example: <code>/Thelonious</code>) to say hello to
    someone specific.</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

@application.route('/')
def index_route():
    return header_text + say_hello() + instructions + footer_text


@application.route('/<username>')
def hello_route(username):
    return header_text + say_hello(username) + home_link + footer_text


if __name__ == '__main__':
    application.run()
