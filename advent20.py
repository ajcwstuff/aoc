import time

test_data = '''1
2
-3
3
-2
0
4'''.split('\n')


def parse_data(data):
    return [{'prev_pos': i, 'val': int(item.replace('\n', '')), 'new_pos': i} for i, item in enumerate(data)]

def part1(mixed_data):
    (out,_pos) = Shuffle(mixed_data)
    res = 0
    for i in range(1, 4):
        ind = (i * 1000 + _pos) % len(out)
        for item in out:
            if item['new_pos'] == ind:
                res += item['val']
    return res

def Shuffle(mixed_data,decription_key = 0):
    new_list = mixed_data.copy()
    length = len(mixed_data)
    key = decription_key #% (length-1)
    for i,item in enumerate(mixed_data):
        if (i-1) % 1000 == 0:
            print(i)
        val = item['val']
        movement = val % (length - 1)
        item['prev_pos'] = item['new_pos']
        alt_len = length if (movement + item['new_pos']) % (length-1) == 0 else length - 1
        item['new_pos'] = (movement + item['new_pos']) % (alt_len)
        for item2 in mixed_data:
            if item != item2:
                if item['prev_pos'] <= item2['new_pos'] <= item['new_pos']:
                    item2['new_pos'] -= 1
                elif item['prev_pos'] >= item2['new_pos'] >= item['new_pos']:
                    item2['new_pos'] += 1
            if item2['val'] == 0:
                a = item2['new_pos']


    return (mixed_data,a)

def part2(mixed_data,decription_key):
    res = 0
    for item in mixed_data:
        item['val'] *= decription_key
    a = mixed_data
    for _ in range(10):
        a,whatever = Shuffle(a)
    for i in range(1, 4):
        ind = (i * 1000 + whatever) % len(mixed_data)
        for item in a:
            if item['new_pos'] == ind:
                print(item['val'])
                res += item['val']
    return res



file = 'advent20.txt'
with open(file, 'r') as f:
    data = f.readlines()
parsed_data = parse_data(test_data)
t0 = time.time()
#print('Part1:', part1(parsed_data), time.time() - t0)

decription_key = 811589153
print('Part2:', part2(parsed_data,decription_key), time.time() - t0)
