import pdftotext
with open("PATH-OF-PDF-FILE",'rb') as f:     # to write the path of pdf file
    pdf = pdftotext.PDF(f)
with open('PATH-OF-OUTPUT-TEXT-FILE','w') as f:       # to write the path of output text file
    f.write('\n\n'.join(pdf))