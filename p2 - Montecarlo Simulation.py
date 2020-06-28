# nama file p2.py 
# Isikan email anda dan copy semua cell code yang dengan komentar #Graded

# untuk revisi dan resubmisi sebelum deadline
# silakan di resubmit dengan nilai variable priority yang lebih besar dari
# nilai priority submisi sebelumnya
# JIKA TIDAK ADA VARIABLE priority DIANGGAP priority=0
priority = 0

#netacad email cth: 'abcd@gmail.com'
email='apriliaerlitalisna@gmail.com'
 
# copy-paste semua #Graded cells YANG SUDAH ANDA KERJAKAN di bawah ini

#Graded 1

def isPointInCircle(x,y,r,center=(0,0)):
    if a = ((x - center[0])**2 + (y - center[1])**2)**0.5 <= r:
        print(1>0)
    else:
        print(1<0)

#print(isPointInCircle(1,1,1,center=(0,0)),isPointInCircle(1,0,1,center=(0,0)),isPointInCircle(1,1,1,center=(1,0)),isPointInCircle(0,0,1,center=(1,1)))

#Graded 2

import random

def generateRandomSquarePoints(n,length,center=(0,0)):
    minx = center[0] - length/2
    miny = center[1] - length/2
    maxx = minx + length
    maxy = miny + length
    x = random.uniform(minx,maxx)
    y = random.uniform(miny,maxy)
    
    points = [[x,y] for i in range(n)]
    return points

#CEK OUTPUT KODE ANDA
random.seed(0)

# generate 100 point di dalam persegi dengan panjang sisi 1 dan berpusat di (0,0)
points = generateRandomSquarePoints(100,1)
print(points[10:15])

#Graded 3

def MCCircleArea(r,n=100,center=(0,0)):
  # MULAI KODEMU DI SINI
  pass

#CEK OUTPUT KODE ANDA

random.seed(0)
print(MCCircleArea(1,100),MCCircleArea(1,10,center=(10,10)))