AUTHOR = 'Richard Henderson'
SITENAME = "From the mind of Ricard Henderson..."
SITEURL = 'http://RichardHenderson.dev'
SITETITLE = "Richard Henderson"
SITESUBTITLE = "Data Analyst"
SITEDESCRIPTION = "From the mind of Richard Henderson..."

#BROWSER_COLOR =
PYGMENTS_STYLE = "monokai"

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

# Blogroll

#LINKS = (('Pelican', 'https://getpelican.com/'),
#('Python.org', 'https://www.python.org/'),
#('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'https://github.com/RichardHendersonCR8s'),
          ('twitter', 'https://twitter.com/richsUsername_'),
          ('linkedin','https://www.linkedin.com/in/richard-henderson-716010207/'))

DEFAULT_PAGINATION = 10

THEME = "themes/Flex-master"


FIRST_NAME = "Richard"

TWITTER_USERNAME = "@RichsUsername_"

SITEDESCRIPTION = "Blog by Richard Henderson. Theme provided by David Bryant Copeland\'s https://brutalist-web.design/"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

COPYRIGHT_YEAR = datetime.now().year

USE_LESS = True
