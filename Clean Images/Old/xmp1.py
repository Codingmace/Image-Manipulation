# Getting and Transferring XMP data. FAIL
from libxmp import XMPFiles, consts

xmpfile = XMPFiles(file_path="008 (2).JPG", open_forupdate=True)
xmp = xmpfile.get_xmp()
xmp.set_property(consts.XMP_NS_DC, u'format', u'application/vnd.adobe.illustrator')
xmpfile.put_xmp(xmp)
