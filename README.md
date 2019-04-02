# smallpdf-lotes

  pendiente de probart opciones : https://www.linux.com/learn/creating-pdf-files-ps2pdf  
  `ps2pdf -dPDFSETTINGS=/printer galleyProof.ps
  ps2pdf -dUseFlateCompression=true greatNovel.ps
  ps2pdf -dOptimize=true report.ps`

  pendiente de probart opciones : https://www.volkerschatz.com/tex/hiqpdf.html  
  `ps2pdf -sPAPERSIZE=a4  -dCompatibilityLevel=1.3  \
 -dEmbedAllFonts=true  -dSubsetFonts=true  -dMaxSubsetPct=100  \
 -dAutoFilterColorImages=false  -dColorImageFilter=/FlateEncode  \
 -dAutoFilterGrayImages=false  -dGrayImageFilter=/FlateEncode  \
 -dAutoFilterMonoImages=false  -dMonoImageFilter=/CCITTFaxEncode  \
 document.ps  document.pdf`

* **está sin probar**  
Script python para comprimir todos los archivos PDF usando ghostscript y el comando `ps2pdf` es multiproceso paralelo con varios ficheros.
ghostscript debe estar instalado -> `sudo apt-get install ghostscript`

* **untested**  
Batch processing PDF files in a multi-thread scritp to compress various files at the same time using ghostscript and the command `ps2pdf`.
ghostscript must be installed -> `sudo apt-get install ghostscript`
