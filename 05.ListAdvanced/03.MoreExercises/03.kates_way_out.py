n=int(input())
maze=[list(input()) for i in range(n)]
flag=False  # Flag to notify if Kate cant get out
spaces=[]   # possible spaces to move to
steps=0     # steps and old_steps will help me keep memory of the routs lenghts and choose the longest
steps_old=-1    # because if K is on the edge of the Maze she is already at possible exit position, and
                # i need invalid value for old steps

for i in range(n):  #find Kate
    if 'k' in maze[i]:
        k_idx=[i,maze[i].index(('k'))]

maze[k_idx[0]][k_idx[1]]=' '    # make the space ocupied by Kate as a free space to move over
                                # in case a closed path was chosen and a new one is needed that passes
                                # through K's initial position

visited=[[k_idx[0], k_idx[1]]]  # all spaces that Kate has visited
def find_space(k,ma):
    s_u=[] # space up .. etc...
    s_r=[]
    s_d=[]
    s_l=[]
    if k[0]!=0 and ma[k[0]-1][k[1]]==' ': s_u+= [k[0]-1,k[1]]
    if k[1]<(len(ma[k[0]])-1) and ma[k[0]][k[1]+1]==' ': s_r+=[k[0],k[1]+1]
    if k[0]<(len(ma)-1) and ma[k[0] + 1][ k[1]] == ' ': s_d+=[k[0] + 1, k[1]]
    if k[1]!=0 and ma[k[0]][ k[1] - 1] == ' ':  s_l+=[k[0], k[1] - 1]
    return [s_u,s_r,s_d,s_l]    # list of available spaces in each direction , busy spaces are empty,
                                # Edge spaces are covered separatly

def move(k,s,v,maze,m):
    for i in range(len(s)): # all available spaces around kate, s is the output from def find_space
        if s[i] not in v and bool(s[i]):    #if the space is not visited and is free
            k=s[i]                         #Kate moves there
            v.append(s[i])
            m+=1
            return k,v,m
        elif all(i in v for i in list(filter(lambda x : bool(x),s))): # if all available spaces are already visited
            maze[k[0]][k[1]]='@'            #Kate marks the space with @ BECAUSE this position doesnt lead to any new spaces or exits
            k = v[-2]                       # Kate moves one step back
            del v[-1]                       # Kate removes the marked with @ space from the visited spaces as
                            # it is clearly a dead end and from now on will be part of the Maze walls
            m-=1            # as Kate moves back, we decrease the steps
            return k,v,m

while k_idx[0]<=(n-1):
    if k_idx[1] == 0 or k_idx[1] == len(maze[0]) - 1 or k_idx[0] == 0 or k_idx[0] == n - 1:
        steps_old = max(steps, steps_old) # if Kate is on the Edge then we have a possible exit
                                            # but will explore other options

    spaces=find_space(k_idx,maze) # check where Kate can go
    #  now check if there are spaces to go
    if not sum((lambda x : bool(x))(x) for x in spaces) and k_idx[0]<(n-1) and steps_old==-1:
        # if we didn't encounter a possible exit in the past (steps_old==-1)
        # and we have ways to go now, then there is no exit
        print("Kate cannot get out")
        flag=True
        break
    elif not sum((lambda x: bool(x))(x) for x in spaces) and steps_old != -1:
        steps=steps_old #if we have no ways to go, and we have a possible exit, then that's the exit
        break
    # then if there are spaces to go, GO
    k_idx, visited, steps = move(k_idx,spaces,visited,maze,steps)
    # print('\n\n')
    # for elem in range(n):  # check your way back building walls in the Maze
    #     print(''.join(maze[elem]))
    # print(k_idx)

if  not flag:
    print(f"Kate got out in {max(steps,steps_old)+1} moves")