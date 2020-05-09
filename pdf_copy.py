Original_file='1.pdf'
New_file='summary.pdf'

Pages_to_copy=[1,9]

import PyPDF2

pdfFile=open(Original_file, 'rb')
pdfReader=PyPDF2.PdfFileReader(pdfFile)
pdfWriter=PyPDF2.PdfFileWriter()

for pageNum in range(pdfReader.numPages):
    if pageNum+1 in Pages_to_copy:
        page=pdfReader.getPage(pageNum)
        pdfWriter.addPage(page)

pdfFile_new=open(New_file, 'wb')
pdfWriter.write(pdfFile_new)

pdfFile_new.close()
pdfFile.close()