import sys
sys.path.append("PATH\TO\PROJECT\DIRECTORY")

from converter import Converter  # converter module existed inside this sam repository

from Autodesk.Revit.DB import *
from Autodesk.Revit.DB import FilteredElementCollector as fec

uiapp = __revit__
app = uiapp.Application
uidoc = uiapp.ActiveUIDocument
doc = uidoc.Document
view = uidoc.ActiveView

selection = [doc.GetElement(sel) for sel in uidoc.Selection.GetElementIds()]

t = Transaction(doc, "TRANSACTION_NAME")

try:
	t.Start()
	# TRANSACTION_HERE
	t.Commit()
except Exception as e:
	print("Exception: ", e)
	t.RollBack()
