from PyPDF2 import PdfMerger

myPdf = ["1.pdf", "2.pdf", "3.pdf", "4.pdf"];

pdfMerger = PdfMerger();

for Spdf in myPdf:
    pdfMerger.append(Spdf);


PdfMerger = pdfMerger.write("Converted.pdf");
