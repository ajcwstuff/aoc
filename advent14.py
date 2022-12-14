import time
import numpy as np


def parse_data(file):
    wall = []
    with open(file, 'r') as f:
        data = f.readlines()
    for line in data:
        points = [
            np.array((int(bit.split(',')[0]), int(bit.split(',')[1])))
            for bit in line.split()
            if bit != '->'
        ]
        for i in range(len(points)):
            wall.append((points[i][0],points[i][1]))
            if i >= len(points) - 1:
                break
            diff =  points[i+1] - points[i]
            if abs(diff).any() > 0:
                for j in range(1,max(abs(diff))):
                    a = points[i]+ (j*np.sign(diff))
                    wall.append((a[0],a[1]))
    return np.array(wall)



leftdown = [-1,1]
rightdown = [1,1]
class Cave:
    def __init__(self,walls):
        self.walls = walls
        self.settled = np.array(())
        self.blocks = walls
        self.floor = max(walls[:,1]) + 2

    def endlessFall(self,snow,f1,f2):
        return snow[0] not in self.blocks[:, 0] or len(self.blocks[(f1 & f2)]) == 0
    def endlessFall2(self,snow,f1,f2):
        return snow[0] not in self.blocks[:, 0] or len(self.blocks[(f1 & f2)]) == 0
    def fall(self,snow):

        filter1 = (self.blocks[:, 0] == snow[0])
        filter2 = (self.blocks[:, 1] > snow[1])
        if self.endlessFall(snow,filter1,filter2):
            return False
        #if self.endlessFall(snow,filter1,filter2):

        #    self.blocks = np.append(self.blocks, np.array((snow[0],self.floor -1 ))).reshape(-1, 2)
        #    return True


        lowval_y = min(self.blocks[(filter1 & filter2)][:,1])
        snow[1] = (lowval_y) - 1
        filter3 = (self.blocks[:, 0] == (snow + leftdown)[0])
        filter4 = (self.blocks[:, 1] == (snow + leftdown)[1])
        filter5 = (self.blocks[:, 0] == (snow + rightdown)[0])
        filter6 = (self.blocks[:, 1] == (snow + rightdown)[1])
        loval_x = snow[0]

        #subset = walls[(filter1 & (walls[:,1] == lowval))]
        if not len(self.blocks[(filter3 & filter4)]):
            snow += leftdown
            return self.fall(snow)
        elif not len(self.blocks[(filter5 & filter6)]):
            snow += rightdown
            return self.fall(snow)
        else:
            self.blocks = np.append(self.blocks,snow).reshape(-1,2)
            return True


def part1(walls,start_point = 500):
    snow = np.array([start_point,0])
    cave = Cave(walls)
    count = 0
    while cave.fall(snow):
        count += 1
        snow = np.array([start_point,0])
    return count

def part2(walls, start_point=500):
    snow = np.array([start_point, 0])
    cave = Cave(walls)
    count = 0
    while cave.fall(snow):
        count += 1
        if count%400 == 0:
            print(count)
        snow = np.array([start_point, 0])
        if len(cave.blocks[((cave.blocks[:, 0] == snow[0]) & (cave.blocks[:, 1] == snow[1]))]):
            return count
    return count



            #check for wall









t0 = time.time()

walls = parse_data('advent14.txt')
print('Part1: ',part1(walls),time.time() - t0)
print('Part2: ',part2(walls),time.time() - t0)
