import numpy as np

def read_lines_of_text(inputfile, otype='list'):
    f = open("../data/"+inputfile, "r")
    data = f.read().splitlines()

    if otype == 'list':
        return data
    
    if otype == 'numpy':
        return np.array(data)
    
def read_lines_of_ints(inputfile, otype='list'):
    f = open("../data/"+inputfile, "r")
    data = f.read().splitlines()
    data = [int(x) for x in data]

    if otype == 'list':
        return data
    if otype == 'numpy':
        return np.array(data)

def read_2dmap_to_numpy(inputfile):
    f = open("../data/"+inputfile, "r")
    data = f.read().splitlines()

    map2d = []
    for line in data:
        line_steps = list(line)
        map2d.append(line_steps)

    map2d = np.array(map2d)
    return map2d
    
