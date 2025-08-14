from Autodesk.Revit.DB import Transaction, FilteredElementCollector


uiapp = __revit__
app = uiapp.Application
uidoc = uiapp.ActiveUIDocument
doc = uidoc.Document

selection = doc.GetElement(uidoc.Selection.GetElementIds())  # Manual scene selections by Id
collector = FilteredElementCollector(doc)  # Must get defined at every attempt

t = Transaction(doc, "TRANSACTION_NAME")

try:
	t.Start()
	# Transactions here ...
	t.Commit()
except Exception as e:
	print("Exception:", e)

	t.RollBack()


