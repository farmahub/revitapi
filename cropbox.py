import sys
sys.path.append(r"path\to\project")

from converter import Converter

from Autodesk.Revit.DB import *

uiapp = __revit__
app = uiapp.Application
uidoc = uiapp.ActiveUIDocument
doc = uidoc.Document
view = uidoc.ActiveView

selection = [doc.GetElement(sel) for sel in uidoc.Selection.GetElementIds()]

bbox = BoundingBoxXYZ()

t = Transaction(doc, "TRANSACTION_NAME")

try:
	t.Start()
	# TRANSACTION_HERE
	bbox.Min = XYZ(-5, -5, -5)
	bbox.Max = XYZ(5, 5, 5)
	
	view.CropBox = bbox
	view.CropBoxActive = True
	view.CropBoxVisible = True
	t.Commit()
except Exception as e:
	print("Exception: ", e)
	t.RollBack()
