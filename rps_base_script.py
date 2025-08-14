from Autodesk.Revit.DB import *

uiapp = __revit__
app = uiapp.Application
uidoc = uiapp.ActiveUIDocument
doc = uidoc.Document


class Converter:
	def ft_to_mm(input):
		return input * 304.8
		
	def mm_to_ft(input):
		return input * 0.00328084

selection = [doc.GetElement(id) for id in uidoc.Selection.GetElementIds()]  # Manual scene selections by Id
collector = FilteredElementCollector(doc)  # Must get defined at every attempt

t = Transaction(doc, "TRANSACTION_NAME")

try:
	t.Start()
	# Transactions here ...
	t.Commit()
except Exception as e:
	print("Exception: ", e)
	t.RollBack()
