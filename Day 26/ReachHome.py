# https://www.youtube.com/watch?v=zg8Y1oE4qYQ&list=PLDzeHZWIZsTqBmRGnsCOGNDG5FY0G04Td&index=2

def reach_home(src,dest):
    print(f"source {src} destnation {dest}")
    if src == dest:
        print("Reached")
        return

    reach_home(src+1,dest)


src = 0
dest = 10
reach_home(src,dest)