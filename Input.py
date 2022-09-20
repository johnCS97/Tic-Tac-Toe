
def User_Click(x,y,width,height):
    col=-1
    row=-1
    if(x<width / 3):
        col = 0
     
    elif (x<width / 3 * 2):
        col = 1
     
    elif(x<width):
        col = 2
    else:
        col = None

    if(y<height / 3):
        row = 0
     
    elif (y<height / 3 * 2):
        row = 1
     
    elif(y<height):
        row = 2
     
    else:
        row = None
    
    return row,col