require 'combine_pdf'

pdf = CombinePDF.new
pdf << CombinePDF.load("includes/preface.pdf")
pdf << CombinePDF.load("index.pdf")
pdf.save "public-data-leaks.pdf"
