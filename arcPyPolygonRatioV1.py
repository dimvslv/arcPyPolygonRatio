import arcpy
import pythonaddins

mxd = arcpy.mapping.MapDocument("CURRENT")
layers = arcpy.mapping.ListLayers(mxd)

selected_layers = []
selected_features = []

for layer in layers:
    if layer.getSelectionSet():
        selected_layers.append(layer)
        selected_features.extend([(layer.name, row[0]) for row in arcpy.da.SearchCursor(layer, ["SHAPE@"])])

if len(selected_features) == 0:
    pythonaddins.MessageBox("Select polygon features", "Info", 0)
else:
    areas = [(name, feature.getArea("GEODESIC", "HECTARES")) for name, feature in selected_features]
    total_area = sum(area for _, area in areas)

    message = "Total area: {:.1f} ha\n\n".format(total_area)
    
    for i, (layer_name, area) in enumerate(areas):
        percent = (area / total_area) * 100
        message += "{}: {:.1f} ha ({:.1f}%)\n".format(layer_name, area, percent)
    
    pythonaddins.MessageBox(message, "Area Balance", 0)
