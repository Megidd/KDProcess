# coding: utf-8
from __future__ import unicode_literals

import random
import uno

doc = XSCRIPTCONTEXT.getDocument()

def KDProcess(arg):
    print(f"arg: {arg}")
    activeSheet = doc.getCurrentController().getActiveSheet()
    x = random.randint(1,10)
    y = random.randint(1,10)
    cell = activeSheet[x,y]
    cell.setString(f"random:{x},{y}")
    return
