from skimage import io
import numpy as np

def average(array):
    rows = len(array)
    columns = len(array[0])
    s = 0
    total = rows*columns
    
    for i in range(rows):
        for j in range(columns):
            s += array[i][j]
    
    average = s/total
    return average

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
        if ttt_gray[i][270]<0.45:
            hor_line_pos.append(i)
            
    for i in range(len(ttt_gray[0])):
        if ttt_gray[300][i]<0.45:
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
a = 20 #safety margin

def initialise_zones(hor_line_lim,ver_line_lim):
    zone11 = np.zeros((hor_line_lim[1]-a,ver_line_lim[1]-a))
    zone12 = np.zeros((hor_line_lim[1]-a,ver_line_lim[3]-ver_line_lim[2]-a))
    zone13 = np.zeros((hor_line_lim[1]-a,len(ttt_gray[0])-ver_line_lim[4]-a))
    zone21 = np.zeros((hor_line_lim[3]-hor_line_lim[2]-a,ver_line_lim[1]-a))
    zone22 = np.zeros((hor_line_lim[3]-hor_line_lim[2]-a,ver_line_lim[3]-ver_line_lim[2]-a))
    zone23 = np.zeros((hor_line_lim[3]-hor_line_lim[2]-a,len(ttt_gray[0])-ver_line_lim[4]-a))
    zone31 = np.zeros((len(ttt_gray)-hor_line_lim[4]-a,ver_line_lim[1]-a))
    zone32 = np.zeros((len(ttt_gray)-hor_line_lim[4]-a,ver_line_lim[3]-ver_line_lim[2]-a))
    zone33 = np.zeros((len(ttt_gray)-hor_line_lim[4]-a,len(ttt_gray[0])-ver_line_lim[4]-a))
    return zone11,zone12,zone13,zone21,zone22,zone23,zone31,zone32,zone33

def set_zone(zone,x,y,ttt_gray,hor_line_lim,ver_line_lim):
    for i in range(len(zone)-a):
        for j in range(len(zone[0])-a):
            zone[i][j] = ttt_gray[i+hor_line_lim[(x-1)*2]][j+ver_line_lim[(y-1)*2]]
    return zone

def write_position(average,text):
    #filter out previously written values (so you dont check them twice)
    average_filtered = np.ones((3,3))
    for i in range(3):
        for j in range(3):
            if text[i][j] != 1:
                average_filtered[i][j] = average[i][j]
    
    #search in the array where the minimum is and return index            
    minlist = []
    min_index = np.zeros(3)
    
    for i in range(3):
        min_index[i] = np.argmin(average)
        minlist.append(np.amin(average,axis=i)) 
        
    x = np.argmin(minlist)
    y = min_index[x]
    print "The opponent put an x on position",x+1,y+1
    
    pos = text
    pos[x][y] = 1
    
    return pos
            
         
#---------------------------------MAIN PROGRAM---------------------------    

#get greyscale array of picture
image_name = 'Test0_v2'
ttt_gray = load_image(image_name)

#get positions of the grid
hor_line_lim,ver_line_lim = grid_pos(ttt_gray)

#define the zones for furhter calculation
zone11,zone12,zone13,zone21,zone22,zone23,zone31,zone32,zone33 = initialise_zones(hor_line_lim,ver_line_lim)

zone11 = set_zone(zone11,1,1,ttt_gray,hor_line_lim,ver_line_lim)
zone12 = set_zone(zone12,1,2,ttt_gray,hor_line_lim,ver_line_lim)
zone13 = set_zone(zone13,1,3,ttt_gray,hor_line_lim,ver_line_lim)
zone21 = set_zone(zone21,2,1,ttt_gray,hor_line_lim,ver_line_lim)
zone22 = set_zone(zone22,2,2,ttt_gray,hor_line_lim,ver_line_lim)
zone23 = set_zone(zone23,2,3,ttt_gray,hor_line_lim,ver_line_lim)
zone31 = set_zone(zone31,3,1,ttt_gray,hor_line_lim,ver_line_lim)
zone32 = set_zone(zone32,3,2,ttt_gray,hor_line_lim,ver_line_lim)
zone33 = set_zone(zone33,3,3,ttt_gray,hor_line_lim,ver_line_lim)


#get the greyscale averages of the different zones
zone_average = np.empty((3,3))

zone_average[0][0] = average(zone11)
zone_average[0][1] = average(zone12)
zone_average[0][2] = average(zone13)
zone_average[1][0] = average(zone21)
zone_average[1][1] = average(zone22)
zone_average[1][2] = average(zone23)
zone_average[2][0] = average(zone31)
zone_average[2][1] = average(zone32)
zone_average[2][2] = average(zone33)

#read the previous move
text = np.genfromtxt("positions.txt",dtype = int,delimiter = ",")

#convert averages into written or empty entries
pos = np.empty((3,3),dtype = int)
pos = write_position(zone_average,text)

#save the present move to a textfile
np.savetxt("positions.txt",pos,delimiter = ",")

