# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import json
# make the operating system for paths undepending
from pathlib import Path

from matplotlib import cm

filename = Path("Ploten/data.json")

if filename:
    with open(filename, 'r') as loadedData:
        data = loadedData.read()
        datastore = json.loads(data)

x = np.linspace(-40, 40, 49)
y = np.linspace(-40, 40, 49)

cs = plt.contourf(x, y, datastore[2][:][:], levels=100, cmap=cm.jet)

char = plt.colorbar(cs, ticks=[-60, -50, -40, -30, -20, -11])

plt.xlabel('x=direction [$\mu$$m$]')
plt.ylabel('y=direction [$\mu$$m$]')
plt.show()