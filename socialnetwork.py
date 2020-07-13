
from datetime import datetime
from utils import calculateElapsedTime

POST_PATTERN = '\s->\s'
FOLLOW_PATTERN = '\sfollows\s'
WALL_PATTERN = '\swall$'

"""Posts repository

post hash is the key
"""
timeline = dict()



"""Users repository

username is the key
"""
users = dict()

class User:
    """Social network user"""

    def __init__(self, name):
        self.name = name

        """Set of user followed
        
        Each entry is the followee's name
        """
        self.following = set()

        """List of user's posts
        
        Each entry is a post's key
        """
        self.timeline = []



class Post:
    """Social network post"""
    def __init__(self, username, content):

        """Creation date"""
        self.dt = datetime.now()

        """Username"""
        self.username = username

        """Post content"""
        self.content = content
    
    def __hash__(self):
        return hash((datetime.timestamp(self.dt), self.username))



def post(username, content):
    """Create a new post

    Keyword arguments:
    username -- user who create the post
    content -- post's content
    """

    if username not in users:
        create_user(username)

    # create post
    post = Post(username, content)

    # use post's hash as key
    post_key = hash(post)

    # insert post in timeline
    timeline[post_key] = post

    # add post reference in user's timeline
    users[username].timeline.append(post_key)

def follow(username, followee):
    """Create a following relation between users
    
    Keyword arguments:
    username -- user that follows
    followee -- the user is going to be followed
    """

    if username not in users:
        create_user(username)

    if followee not in users:
        create_user(followee)

    users[username].following.add(followee)

def show_wall(username):
    """Display a user wall
        
    Keyword arguments:
    username -- wall owner
    """

    if username not in users:
        create_user(username)

    T = set()
    T = T.union(users[username].timeline)
    for following_user_key in users[username].following:
        T = T.union(users[following_user_key].timeline)
    
    wall = set()
    for entry in T:
        wall.add(timeline[entry])

    for post in sorted(wall, reverse=True, key=lambda post: (datetime.now(), post.dt)):
        elapsed, unit = calculateElapsedTime(post.dt)
        # unit = "minutes"
        print("%s - %s (%d %s ago)" % (post.username, post.content, elapsed, unit))

def read_timeline(username):
    """Read user timeline
        
    Keyword arguments:
    username -- timeline owner
    """
    if username not in users:
        create_user(username)

    for timeline_entry in reversed(users[username].timeline):
        post = timeline[timeline_entry]
        elapsed, unit = calculateElapsedTime(post.dt)

        print("%s (%d %s ago)" % (post.content, elapsed, unit))

def create_user(username):
    """Add a new user

    Keyword arguments:
    username -- :)
    """

    new_user = User(username)
    users[username] = new_user
