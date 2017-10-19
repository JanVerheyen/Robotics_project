from skimage import io
import numpy as np
    
def contrast(array):
    difference = np.ones((3,3))
    for i in range(3):
        for j in range(3):
            array[i][j] = np.sort(array[i][j],axis=None)
            c = len(array[i][j])/100
            difference[i][j] = sum(array[i][j][-c:-1])-sum(array[i][j][1:c])     
    return difference
    

#load png image and convert into greyscale
def load_image(imagename):
    filename = 'Pictures/'+imagename+'.png'
    ttt_gray = io.imread(filename,True)
    return ttt_gray

def check_whiteness(array):
    s = array[0][0]+array[0][-1]+array[-1][0]+array[-1][-1]
    whiteness = s/4
    return whiteness
    
#calculate the pixel-positions of the grid
def grid_pos(ttt_gray):
    hor_line_pos = []
    ver_line_pos = []
    hor_line_lim = [0,0,0,0,0]
    ver_line_lim = [0,0,0,0,0] 
    
    #Get the location of the more black pixels to have a range of the positions of the lines
    for i in range(len(ttt_gray)):
        if ttt_gray[i][len(ttt_gray[0])/30]<0.45:
            hor_line_pos.append(i)
            
    for i in range(len(ttt_gray[0])):
        if ttt_gray[len(ttt_gray)/30][i]<0.45:
            ver_line_pos.append(i)
    
    #extremes of the hor and ver lines
    hor_line_lim[1] = hor_line_pos[0]
    hor_line_lim[4] = hor_line_pos[-1]
    ver_line_lim[1] = ver_line_pos[0]
    ver_line_lim[4] = ver_line_pos[-1]
    
    for i in range(1,len(hor_line_pos)-1):
        if (hor_line_pos[i+1]-hor_line_pos[i])>5:
            hor_line_lim[2] = hor_line_pos[i] 
            hor_line_lim[3] = hor_line_pos[i+1]
    
    for i in range(1,len(ver_line_pos)-1):
        if (ver_line_pos[i+1]-ver_line_pos[i])>5:
            ver_line_lim[2] = ver_line_pos[i] 
            ver_line_lim[3] = ver_line_pos[i+1] 
    
    return hor_line_lim,ver_line_lim
    
#initialise zones for calculation
    
def initialise_zones(hor_line_lim,ver_line_lim):
    zone = np.zeros((3,3),dtype=object)
    zone[0][0] = np.ones((hor_line_lim[1]-a,ver_line_lim[1]-a))
    zone[0][1] = np.ones((hor_line_lim[1]-a,ver_line_lim[3]-ver_line_lim[2]-a))
    zone[0][2] = np.ones((hor_line_lim[1]-a,len(ttt_gray[0])-ver_line_lim[4]-a))
    zone[1][0] = np.ones((hor_line_lim[3]-hor_line_lim[2]-a,ver_line_lim[1]-a))
    zone[1][1] = np.ones((hor_line_lim[3]-hor_line_lim[2]-a,ver_line_lim[3]-ver_line_lim[2]-a))
    zone[1][2] = np.ones((hor_line_lim[3]-hor_line_lim[2]-a,len(ttt_gray[0])-ver_line_lim[4]-a))
    zone[2][0] = np.ones((len(ttt_gray)-hor_line_lim[4]-a,ver_line_lim[1]-a))
    zone[2][1] = np.ones((len(ttt_gray)-hor_line_lim[4]-a,ver_line_lim[3]-ver_line_lim[2]-a))
    zone[2][2] = np.ones((len(ttt_gray)-hor_line_lim[4]-a,len(ttt_gray[0])-ver_line_lim[4]-a))
    
    for x in range(3):
        for y in range(3):
            dim = np.shape(zone[x][y])
            for i in range(dim[0]-a):
                for j in range(dim[1]-a):
                    zone[x][y][i][j] = ttt_gray[i+hor_line_lim[x*2]][j+ver_line_lim[y*2]]
    return zone      

def write_position(average,text):
    #filter out previously written values (so you dont check them twice)
    average_filtered = np.ones((3,3))
    for i in range(3):
        for j in range(3):
            if text[i][j] != 1:
                average_filtered[i][j] = average[i][j]
        
    #search in the array where the minimum is and return index 
    index = average.argmax()
    x = index/3
    y = index%3  
    
    pos = text
    pos[x][y] = 1
    
    return pos
            
         
#---------------------------------MAIN PROGRAM---------------------------    
#get greyscale array of picture
image_name = 'tic-tac-toe'
ttt_gray = load_image(image_name)
a = len(ttt_gray)/30  #safety margin

#get positions of the grid
hor_line_lim,ver_line_lim = grid_pos(ttt_gray)

#define and get the right vlaues for the zones
zone = initialise_zones(hor_line_lim,ver_line_lim)

#get the contrast of the different zones
zone_contrast = np.ones((3,3))
zone_contrast = contrast(zone)

#read the previous move
text = np.genfromtxt("positions.txt",dtype = int,delimiter = ",")

#convert averages into written or empty entries
pos = np.empty((3,3),dtype = int)
pos = write_position(zone_contrast,text)

#save the present move to a textfile
np.savetxt("positions.txt",pos,delimiter = ",")