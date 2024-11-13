import arcpy
import pythonaddins

mxd = arcpy.mapping.MapDocument("CURRENT")
layers = arcpy.mapping.ListLayers(mxd)

selected_layers = []  # Список для хранения выбранных слоев
selected_features = []  # Список для хранения выбранных объектов

# Получаем все выбранные объекты из слоев
for layer in layers:
    if layer.getSelectionSet():
        selected_layers.append(layer)
        # Добавляем выбранные объекты в список
        selected_features.extend([row for row in arcpy.da.SearchCursor(layer, ["SHAPE@"])])

# Проверяем, сколько объектов выбрано
if len(selected_features) != 2:
    pythonaddins.MessageBox("Select 2 features in one or two layers", "Info", 0)
else:
    # Получаем площади двух выбранных полигонов
    area1 = selected_features[0][0].getArea("GEODESIC", "SQUAREMETERS")
    area2 = selected_features[1][0].getArea("GEODESIC", "SQUAREMETERS")

    # Рассчитываем процентное соотношение
    if area1 >= area2:
        percent_ratio = (area2 / area1) * 100
        pythonaddins.MessageBox("The smaller polygon is {:.2f}% the larger polygon".format(percent_ratio), "Info", 0)
    else:
        percent_ratio = (area1 / area2) * 100
        pythonaddins.MessageBox("The smaller polygon is {:.2f}% the larger polygon".format(percent_ratio), "Info", 0)