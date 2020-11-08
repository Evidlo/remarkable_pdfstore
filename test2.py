# use pymupdf wheel from here: https://github.com/pymupdf/PyMuPDF/issues/709#issuecomment-721686129

import fitz

stroke_layer_name = 'remarkable pen'

# create new document
doc = fitz.open()
page = doc.newPage()
page.setRotation(0)

r = fitz.Rect(72, 72, 100, 100)
page.addFreetextAnnot(r, 'foobar')

# ----- write strokes -----

# create new optional content group
pen_ocg_xref = doc.addOCG(stroke_layer_name, config=-1, on=1, intent=None)
# create new annotation and set as optional content
annot = page.addInkAnnot(
    [
        [(72, 72), (100, 100), (200, 100), (100, 200)],
        [(372, 300), (367, 324), (355, 346), (336, 362), (312, 370), (287, 370), (264, 362), (244, 346), (232, 324), (228, 300)],
    ]
)
annot.setOC(pen_ocg_xref)

doc.save('out.pdf', deflate=True)

# ----- read strokes -----

doc = fitz.open('out.pdf')
pages = doc.pages()

# get reference to optional content group containing strokes
for xref, ocg in doc.getOCGs().items():
    if ocg['name'] == stroke_layer_name:
        break
else:
    print(f"No layer {stroke_layer_name} found")
    quit()

# find annotations in optional content group
for page in pages:
    for annot in page.annots():
        if annot.getOC() == xref:
            print("pen stroke vertices:")
            print(annot.vertices)

