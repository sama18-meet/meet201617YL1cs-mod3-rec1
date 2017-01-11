from branch import Branch
import turtle

max_depth=7 #The maximum number of branches the tree can have
length=256 #The length of the first branch
startx=0
starty=-250
branch1=Branch((startx,starty),(startx,starty+length))
turtle.hideturtle()

"""
turtle.penup()
turtle.goto(branch1.start)
turtle.pendown()
turtle.goto(branch1.stop)

my_branches = branch1.split()

for b in my_branches:
    turtle.penup()
    turtle.goto(b.start)
    turtle.pendown()
    turtle.goto(b.stop)
"""

def draw_tree( this_branch, branch_num ):
    if max_depth > branch_num :
        turtle.penup()
        turtle.goto(this_branch.start)
        turtle.pendown()
        turtle.goto(this_branch.stop)
        my_branches = this_branch.split()
        for b in my_branches:
            draw_tree(b,branch_num+1)

    '''
    Draw a branch in the tree; then, split the branch and
    recursively call draw_tree again.

    :param this_branch: the branch that will be drawn in turtle
    :param branch_num: the number corresponding to how deep in the tree this branch exists
    '''
    #Complete this method

draw_tree(branch1,1)

turtle.mainloop()
