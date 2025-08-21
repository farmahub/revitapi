import sys
sys.path.append("\path\to\project\dir")  # enables modules to get imported within

from converter import Converter  # find at the same repository

from Autodesk.Revit.DB import *

uiapp = __revit__
app = uiapp.Application
uidoc = uiapp.ActiveUIDocument
doc = uidoc.Document
view = uidoc.ActiveView

selection = [doc.GetElement(id) for id in uidoc.Selection.GetElementIds()]  # Manual scene selections by Id

t = Transaction(doc, "TRANSACTION_NAME")

try:
	t.Start()
	# Transactions here ...
	t.Commit()
except Exception as e:
	print("Exception: ", e)
	t.RollBack()

