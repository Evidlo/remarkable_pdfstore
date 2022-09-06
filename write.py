# Evan Widloski - 2020-11-07
# demonstrating storing pen strokes directly in PDF

import fitz

# name of layer where pen strokes live
stroke_layer_name = 'remarkable pen'

# create new document
doc = fitz.open()
page = doc.new_page()
page.set_rotation(0)

# draw a rectangle and add some text for fun
r = fitz.Rect(72, 72, 100, 100)
page.add_freetext_annot(r, 'foobar')

# ----- write pen strokes -----

# create new optional content group
pen_ocg_xref = doc.add_ocg(stroke_layer_name, config=-1, on=1, intent=None)
# create new annotation and set as optional content
annot = page.add_ink_annot(
    [
        [(72, 72), (100, 100), (200, 100), (100, 200)],
        [(372, 300), (367, 324), (355, 346), (336, 362), (312, 370), (287, 370), (264, 362), (244, 346), (232, 324), (228, 300)],
    ]
)
annot.set_oc(pen_ocg_xref)
annot = page.add_ink_annot(
    [
        [(82, 82), (120, 120), (220, 120), (120, 220)],
        [(382, 320), (387, 334), (355, 356), (356, 352), (322, 380), (297, 380), (274, 372), (254, 356), (242, 334), (238, 310)],
    ]
)

outfile = 'out.pdf'
print(f"saved PDF to {outfile}")
doc.save(outfile, deflate=True)
