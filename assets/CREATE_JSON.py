from os import listdir
from os.path import isfile, join
import json
folders = ["tile", "objects", "layer", "background"]

for a in folders:
    onlyfiles = [f for f in listdir(a) if isfile(join(a, f))]
    to_save = {}
    i = 0
    for b in onlyfiles:
        print (b[-4:])
        if b[-4:] == ".png":
            to_save[str(i)] = b
            i += 1
    with open(a + '/data.json', 'w') as outfile:
        json.dump(to_save, outfile)

