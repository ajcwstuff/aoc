import time




def parse_data(file):
    with open(file, 'r') as f:
        data = f.readlines()
    a,b = [],[]
    for i,line in enumerate(data):
        if (i+1)%3 == 1:
            a.append(eval(line))
        elif (i+1)%3 == 2:
            b.append(eval(line))
    return a,b





def quickSort(array, low, high):
    def partition(array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if compare(array[j],pivot) != 'Good':
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])
        (array[i + 1], array[high]) = (array[high], array[i + 1])
        return i + 1
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


def compare(leftItem,rightItem):
    if type(leftItem) == int:
        leftItem = [leftItem]
    if type(rightItem) == int:
        rightItem = [rightItem]

    for i in range(len(rightItem)):
        if i > len(leftItem) - 1:
            return 'Good'
        if type(rightItem[i]) == list:
            res =  compare(leftItem[i],rightItem[i])
            if res == 'Good':
                return 'Good'
            elif res == 'Bad':
                return 'Bad'
            else:
                continue
        if type(leftItem[i]) == list:
            res = compare(leftItem[i],rightItem[i])
            if res == 'Bad':
                return 'Bad'
            elif res == 'Good':
                return 'Good'
            else:
                continue
        if leftItem[i] > rightItem[i]:
            return 'Bad'
        if leftItem[i] < rightItem[i]:
            return 'Good'
    if len(leftItem) > len(rightItem):
        return 'Bad'
    return 'continue'


def part1(left,right):
    return sum(i + 1 for i in range(len(left)) if compare(left[i],right[i]) == 'Good')

def part2(packets):
    packets += [[2],[6]]
    size = len(packets)
    quickSort(packets, 0, size - 1)
    return (size - packets.index([2]))*(size - packets.index([6]))




left,right = parse_data('advent13.txt')
t0 = time.time()
print("Part 1:", part1(left,right),time.time() - t0)

print("Part 2:",part2(left+right),time.time() - t0)

