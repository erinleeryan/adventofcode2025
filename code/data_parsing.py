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
    
def read_a_csv(inputfile, output='string', reduce=True):
    # output means you can force things to be a string
    # reduce means that rather than return a list of lists 
    # where each constituent list represents a line
    # you reduce something that is all smashed together in a single list

    f = open("../data/"+inputfile, "r")
    data = f.read().splitlines()
    output_data = []
    for line in data:
        strings = line.split(',')
        # remove trailing comma ends and any blank entries in the middle that might show up
        strings = [item for item in strings if item != '']
        if output == 'int':
            strings = [int(x) for x in strings]
        output_data.append(strings)

    if reduce == True:
        output_data = sum(output_data, [])


    return output_data

    
