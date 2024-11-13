import arcpy
import pythonaddins

mxd = arcpy.mapping.MapDocument("CURRENT")
layers = arcpy.mapping.ListLayers(mxd)

selected_layer = None

for layer in layers:
    if layer.getSelectionSet():
        selected_layer = layer
        break

if layer is None:
    pythonaddins.MessageBox("Select features to get coordinates", "Info", 0)
elif int(arcpy.GetCount_management(layer).getOutput(0)) != 2:
    pythonaddins.MessageBox("Select 2 features", "Info", 0)
else:
    selected_features = [row for row in arcpy.da.SearchCursor(layer, ["SHAPE@"])]

    area1 = selected_features[0][0].getArea("GEODESIC", "SQUAREMETERS")
    area2 = selected_features[1][0].getArea("GEODESIC", "SQUAREMETERS")

    if area1 >= area2:
        percent_ratio = (area2 / area1) * 100
        pythonaddins.MessageBox("The smaller polygon is {:.2f}% the larger polygon".format(percent_ratio), "Info", 0)
    else:
        percent_ratio = (area1 / area2) * 100
        pythonaddins.MessageBox("The smaller polygon is {:.2f}% the larger polygon".format(percent_ratio), "Info", 0)

        