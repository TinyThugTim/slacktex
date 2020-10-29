SOURCE = sample
DPI = 300

make:
	pdflatex $(SOURCE).tex $(SOURCE).pdf
	pdfcrop $(SOURCE).pdf $(SOURCE).pdf
	pdf2svg $(SOURCE).pdf $(SOURCE).svg
	inkscape --export-dpi=$(DPI) $(SOURCE).svg --export-png=$(SOURCE).png
	make clean

clean:
	rm -rf  $(TARGET) $(SOURCE).pdf $(SOURCE).svg  *.class *.html *.log *.aux *.data *.gnuplot

svg:


