import subprocess

tex="sample.tex"
pdf="sample.pdf"
svg="sample.svg"
png="sample.png"
aux="sample.aux"
log="sample.log"

pdflatex = subprocess.run(["pdflatex", tex, pdf])
pdfcrop  = subprocess.run(["pdfcrop", pdf, pdf])
pdf2svg  = subprocess.run(["pdf2svg", pdf, svg])
inkscape = subprocess.run(["inkscape", "--export-dpi=300", svg, "--export-png="+png])
clean    = subprocess.run(["rm", "-rf", pdf, svg, log, aux])

print("The exit code was: %d" % pdflatex.returncode)
print("The exit code was: %d" % pdfcrop.returncode)
print("The exit code was: %d" % pdf2svg.returncode)
print("The exit code was: %d" % inkscape.returncode)
print("The exit code was: %d" % clean.returncode)

