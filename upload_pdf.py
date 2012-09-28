
import time
from docraptor import DocRaptor

docraptor = DocRaptor(api_key='gnBUcece6TI6A1TXlvo')

print "Create test_basic_url.pdf"
with open("micah-fitzgerald-resume.pdf", "wb") as f:
    f.write(docraptor.create({
        'document_url': 'http://micahf.com/resume_print.html', 
        'test': True
    }).content)
