# minimal annotation inklist example

    <</Type/Annot/Subtype/Ink/Contents(<enter description here>)/InkList[[150 300 250 300 150 200 250 200]]/Rect[200 250 300 150]/P 3 0 R/F 4/C[1 0 0]>>
    
    <pikepdf.Dictionary(type_="/Annot")({
      "/C": [ 1, 0, 0 ],
      "/Contents": "<enter description here>",
      "/F": 4,
      "/InkList": [ [ 150, 300, 250, 300, 150, 200, 250, 200 ] ],
      "/P": {
        "/Annots": [ <.get_object(4, 0)> ],
        "/MediaBox": [ 0, 0, 500, 800 ],
        "/Parent": <reference to /Pages>,
        "/Resources": {
    
        },
        "/Type": "/Page"
      },
      "/Rect": [ 200, 250, 300, 150 ],
      "/Subtype": "/Ink",
      "/Type": "/Annot"
    })>
    
    
- *C* - object color, RGB.  can be lengths other than 3 for other colorspaces
- *Rect* - (required) location of annotation on page
- *Type* - (optional) type of PDF object.  should be Annot for annotations
- *SubType* - (optional) type of annotation.  should be Ink for Ink annotations
- *P* - (optional?) indirect reference to page object
- *F* - (optional) annotation flags.  controls visibility, whether annotations is printed, etc.
- *Contents* - (optional) human readable annotation description
- *Inklist* - array of stroke arrays.  stroke array is alternating x and y coordinates of each point

# Optional Content Groups (layers)

- https://github.com/pikepdf/pikepdf/issues/118

- p228 - OCProperties
- p222 - Properties

# PDF libs

- mupdf
- pdfium

# PDF-1.7 Spec

https://www.adobe.com/content/dam/acom/en/devnet/pdf/pdfs/PDF32000_2008.pdf

- p383 - Annot attributes table
