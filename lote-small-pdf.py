#!/usr/bin/python
# untested
# está sin probar
# ghostscript must be installed -> sudo apt-get install ghostscript
# ghostscript debe estar instalado -> sudo apt-get install ghostscript

import os, time, glob, subprocess

files = glob.glob('*.png')

workers = []
while files or workers:
    while len(workers) < 4 and files:
        f = files[0]
        files = files[1:]
# aquí ocurre la magia
        w = subprocess.Popen(['ps2pdf', f,
            os.path.splitext(f)[0]+'_XS.pdf'])
# aquí ocurre la magia
        workers.append(w)
    for w in list(workers):
        if w.poll() is not None:
            workers.remove(w)
    time.sleep(0.1)
