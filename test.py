import subprocess
from pdflatex import PDFLaTeX
from pdfCropMargins import crop
from pdf2image import convert_from_path


tex="sample.tex"
pdf="sample.pdf"
svg="sample.svg"
png="sample.png"
aux="sample.aux"
log="sample.log"

pdfl = PDFLaTeX.from_texfile(tex)
pdf_out, log, completed_process = pdfl.create_pdf(keep_pdf_file=True, keep_log_file=False)
pdf_crop = crop(["-o", "crop.pdf", "-p4", "0.5", "0", "0.5", "0", "-u", "-s", pdf]) #l,b,r,t
png = convert_from_path('./crop.pdf', 
	single_file=True,
	dpi=300,
	output_folder='./',
	transparent=True,
	fmt='png',
	output_file=str('output')) 
clean = subprocess.run(["rm", "-rf", pdf, svg, log, aux])
print("The exit code was: %d" % clean.returncode)

