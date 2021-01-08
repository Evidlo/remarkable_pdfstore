# Evan Widloski - 2020-11-07
# demonstrating storing pen strokes directly in PDF

import fitz

# name of layer where pen strokes live
stroke_layer_name = 'remarkable pen'

# create new document
doc = fitz.open()
page = doc.newPage()
page.setRotation(0)

# draw a rectangle and add some text for fun
r = fitz.Rect(72, 72, 100, 100)
page.addFreetextAnnot(r, 'foobar')

# ----- write pen strokes -----

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
print(pen_ocg_xref)

doc.save('out.pdf', deflate=True)
