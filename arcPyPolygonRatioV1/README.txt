This is a stub project created by the ArcGIS Desktop Python AddIn Wizard.

MANIFEST
========

README.txt   : This file

makeaddin.py : A script that will create a .esriaddin file out of this 
               project, suitable for sharing or deployment

config.xml   : The AddIn configuration file

Images/*     : all UI images for the project (icons, images for buttons, 
               etc)

Install/*    : The Python project used for the implementation of the
               AddIn. The specific python script to be used as the root
               module is specified in config.xml.

NOTES
=====

## ✅ v1
- Initial release of the ArcGIS add-in.
- Calculates the area balance of selected polygon features.
- Displays the total area and individual polygon contributions in hectares and percentages.

## 🚀 How to Install
1. Clone the repository.
2. Run the file: `..\arcPyPolygonRatioV1\arcPyPolygonRatioV1.esriaddin`
3. Open or restart ArcMap.
4. A new button should appear in the toolbar.
5. Select polygons, click the button, and see the area balance displayed on the screen!