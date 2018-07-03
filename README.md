# Calculate Heights

This plugin can be used for calcualting Z values of geometries using DEM

## How to install:

* Copy the entire directory containing your new plugin to the QGIS plugin directory:
```bash
C:/Users/bojko108/.qgis2/python/plugins
```
* Compile the resources file using pyrcc4 (run this in root directory):
```bash
cd C:/Users/bojko108/.qgis2/python/plugins/CalculateHeight
pyrcc4 -o resources.py resources.qrc
```
* Run the tests (`make test`)
* Test the plugin by enabling it in the QGIS plugin manager
* Customize it by editing the implementation file: `calculate_height.py`
* Create your own custom icon, replacing the default icon.png
* Modify your user interface by opening UGISPublisher.ui in Qt Designer
* You can use the Makefile to compile your Ui and resource files when you make changes. This requires GNU make (gmake)