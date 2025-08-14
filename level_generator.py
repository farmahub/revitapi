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

# LEVELS_DATA

levels_data = [
	("S_B7", -22700),
	("S_B6", -21960),
	("S_B5", -18720),
	("S_B4", -15480),
	("S_B3", -12240),
	("S_B2", -9000),
	("S_B1", -5400),
	("S_GF", 0),
	("S_M1", 3150),
	("S_01", 6480),
	("S_02", 11880),
	("S_03", 17280),
	("S_04", 22680),
	("S_05", 26280),
	("S_06", 29880),
	("S_07", 33480),
	("S_08", 37080),
	("S_09", 41040),
	("S_10", 45520),
]


t = Transaction(doc, "TRANSACTION_NAME")

try:
	t.Start()
	# Transactions here ...
	for index, item in enumerate(levels_data):
		level = Level.Create(doc, Converter.mm_to_ft(item[1]))
		level.Name = f"{item[0]}_({item[1]})"
	t.Commit()
except Exception as e:
	print("Exception: ", e)
	t.RollBack()