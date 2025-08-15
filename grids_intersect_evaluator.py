from Autodesk.Revit.DB import Transaction, FilteredElementCollector


uiapp = __revit__
app = uiapp.Application
uidoc = uiapp.ActiveUIDocument
doc = uidoc.Document

selection = uidoc.Selection.GetElementIds()

# COLLECTORS
grids = FilteredElementCollector(doc) \
		.OfCategory(BuiltInCategory.OST_Grids) \
		.WhereElementIsNotElementType() \
		.ToElements()
		 
# ELEMENTS
hor_grids = [g for g in grids if isinstance(g.Curve, Line) and g.Curve.Direction.IsAlmostEqualTo(XYZ(1, 0, 0))]
ver_grids = [g for g in grids if isinstance(g.Curve, Line) and g.Curve.Direction.IsAlmostEqualTo(XYZ(0, -1, 0))]


points = []

for h_grid in hor_grids:
    h_line = h_grid.Curve
    for v_grid in ver_grids:
        v_line = v_grid.Curve
        result_ref = clr.Reference[IntersectionResultArray]()
        
        if h_line.Intersect(v_line, result_ref) == SetComparisonResult.Overlap:
            ira = result_ref.Value  # Get the IntersectionResultArray
            if ira.Size > 0:
                point = (h_grid.Name, v_grid.Name, ira.Item[0].XYZPoint)
                points.append(point)