#!/usr/bin/python
# untested
# sin probar
# ghostscript must be installed -> sudo apt-get install ghostscript
# ghostscript debe estar instalado -> sudo apt-get install ghostscript

import os, time, glob, subprocess

files = glob.glob('*.pdf')

workers = []
while files or workers:
    while len(workers) < 4 and files:
        f = files[0]
        files = files[1:]
# aqui ocurre la magia
        w = subprocess.Popen(['ps2pdf', '-dCompatibilityLevel=1.3 -dEmbedAllFonts=true -dSubsetFonts=true -dMaxSubsetPct=100 -dAutoFilterColorImages=false -dColorImageFilter=/FlateEncode -dAutoFilterGrayImages=false -dGrayImageFilter=/FlateEncode -dAutoFilterMonoImages=false -dMonoImageFilter=/CCITTFaxEncode', f])
# aqui ocurre la magia
        workers.append(w)
    for w in list(workers):
        if w.poll() is not None:
            workers.remove(w)
    time.sleep(0.1)
