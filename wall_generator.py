import sys
sys.path.append(r"F:\Farmabim\PY")

from converter import Converter

from Autodesk.Revit.DB import *
from Autodesk.Revit.DB import FilteredElementCollector as fec

uiapp = __revit__
app = uiapp.Application
uidoc = uiapp.ActiveUIDocument
doc = uidoc.Document
view = uidoc.ActiveView

selection = [doc.GetElement(sel) for sel in uidoc.Selection.GetElementIds()]

level = fec(doc).OfClass(Level).FirstElement()         # <Level 1>
walltype = fec(doc).OfClass(WallType).ToElements()[3]  # <Generic - 200 mmm>

t = Transaction(doc, "TRANSACTION_NAME")

try:
	t.Start()
	# TRANSACTION_HERE
	for s in selection:
		wall = Wall.Create(
			doc, 
			s.GeometryCurve,		# Extracts geometry curve out of detail or model curve
			walltype.Id, 
			level.Id, 
			Converter.mm_ft(4000),  # height of the wall
			0,						# base offset
			False,					# flip normal
			False,					# structural
		)
	t.Commit()
except Exception as e:
	print("Exception: ", e)
	t.RollBack()
