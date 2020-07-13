
import re
from socialnetwork import *



def main():

    i = 0
    while True:

        command = input("> ")

        match = re.search(POST_PATTERN, command)
        if match:
            username = command[0 : match.start()].strip()
            content = command[match.end():].strip()
            post(username, content)
            continue

        match = re.search(FOLLOW_PATTERN, command)
        if match:
            username = command[0 : match.start()].strip()
            followee = command[match.end():].strip()
            follow(username, followee)
            continue

        match = re.search(WALL_PATTERN, command)
        if match:
            username = command[0 : match.start()].strip()
            show_wall(username)
            continue

        match = re.search("exit", command)
        if match:
            break

        if not match:
            username = command
            read_timeline(username)




if __name__=="__main__":
   main()