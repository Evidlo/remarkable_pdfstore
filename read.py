# Evan Widloski - 2020-11-07
# demonstrating storing pen strokes directly in PDF

import fitz

# name of layer where pen strokes live
stroke_layer_name = 'remarkable pen'

# ----- read pen strokes -----

infile = 'out.pdf'
print(f"reading from {infile}")
doc = fitz.open(infile)
pages = doc.pages()

# get reference to optional content group containing strokes
for xref, ocg in doc.get_ocgs().items():
    if ocg['name'] == stroke_layer_name:
        break
else:
    print(f"No layer {stroke_layer_name} found")
    quit()

# find annotations in optional content group
# and retrieve pen stroke coordinates
for page in pages:
    for annot in page.annots():
        if annot.get_oc() == xref:
            print("pen stroke vertices:")
            print(annot.vertices)
