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


# GRID_INFORMATION : CHANGE ONLY GRID_NAMES AND GRID_DISTS

grid_names = {
	"hor": ["1a", 1, 2, 3, 4, 5, 6, 7],
	"ver": ["A", "B", "B1", "C", "C1", "D", "E", "F", "G", "H", "I", "I1", "J"],
}
# grid_dists are based on dimensioning lines of the drawing
grid_dists = {
	"hor": [0, -4100, -6900, -6300, -7600, -8800, -11000, -8000],  # negative amounts are in opposite direction of the Y-AXIS
	"ver": [0, 5800, 4100, 4500, 3800, 6000, 7800, 9800, 7800, 9800, 7800, 4400, 7200],
}
# distances from grid_dists get summed here.
grid_coords = {
	"hor": [sum(grid_dists["hor"][:i+1]) for i in range(len(grid_dists["hor"]))],
	"ver": [sum(grid_dists["ver"][:i+1]) for i in range(len(grid_dists["ver"]))]
}


t = Transaction(doc, "TRANSACTION_NAME")

try:
	t.Start()
	# HORIZONTAL GRIDS
	for index, item in enumerate(grid_coords["hor"]):
		start_pt = app.Create.NewXYZ(
			0, 
			Converter.mm_to_ft(grid_coords["hor"][index]), 
			0,
		)
		end_pt = app.Create.NewXYZ(
			Converter.mm_to_ft(grid_coords["ver"][-1]), 
			Converter.mm_to_ft(grid_coords["hor"][index]), 
			0,
		)
		grid = Grid.Create(
			doc,
			Line.CreateBound(
				start_pt,
				end_pt,
			)
		)
		grid.Name = str(grid_names["hor"][index])

	# VERTICAL GRIDS
	for index, item in enumerate(grid_coords["ver"]):
		start_pt = app.Create.NewXYZ(
			Converter.mm_to_ft(grid_coords["ver"][index]), 
			0,
			0,
		)
		end_pt = app.Create.NewXYZ(
			Converter.mm_to_ft(grid_coords["ver"][index]), 
			Converter.mm_to_ft(grid_coords["hor"][-1]), 
			0,
		)
		grid = Grid.Create(
			doc,
			Line.CreateBound(
				start_pt,
				end_pt,
			)
		)
		grid.Name = str(grid_names["ver"][index])
	t.Commit()
except Exception as e:
	print("Exception: ", e)

	t.RollBack()
