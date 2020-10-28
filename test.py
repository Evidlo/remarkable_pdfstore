import pikepdf
import copy

pdf_orig = pikepdf.open('basic.pdf')
pdf = pikepdf.open('basic.pdf')

print(f'pages: {len(pdf.pages)}')

# create new page and add new annotation from scratch
page = pdf.pages[0]
page['/Annots'].append(
    {
        '/C': [0, 1, 0], # rgb
        '/Contents': "reMarkable annotation",
        '/F': 4,
        '/InkList': [[100, 100, 200, 100, 200, 200, 100, 200]], # stroke path
        '/Rect': [200, 200, 100, 100], # bounding box
        '/Type': pikepdf.Name('/Annot'),
        '/Subtype': pikepdf.Name('/Ink'),
        # '/P': pdf.make_indirect(pdf.pages[0])
    }
)

pdf.root['/OCProperties'] = {
    '/OCGs': [
        {
            '/Name': 'bar',
            '/Type': pikepdf.Name('/OCG')
        }
    ],
    '/D': {}
}

pdf.objects.append(
    pikepdf.Dictionary(
    {
        '/Name': 'foo',
        '/Type': 'OCG'
    }
    )
)
pdf.root.append(
    {
        '/Name': 'bar',
        '/Type': 'OCG'
    }
)
# page.Annots[0].C = [0, 0, 0]
# page.Annots[0].Contents = "reMarkable annotation"
# page.Annots[0].F = 4
# page.Annots[0].InkList = [[150, 300, 250, 300, 150, 200, 250, 200]] # stroke path
# page.Annots[0].Rect = [200, 250, 300, 150] # bounding box
# page.Annots[0].Type = pikepdf.Name('/Annot')
# page.Annots[0].Subtype = pikepdf.Name('/Ink')

pdf.save('out.pdf')
