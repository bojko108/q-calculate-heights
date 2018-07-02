# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CalculateHeight
                                 A QGIS plugin
 Calculates height values for each vertex of a geometry using DEM
                             -------------------
        begin                : 2018-07-02
        copyright            : (C) 2018 by bojko108
        email                : bojko108@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load CalculateHeight class from file CalculateHeight.

    :param iface: A QGIS interface instance.
    :type iface: QgisInterface
    """
    #
    from .calculate_height import CalculateHeight
    return CalculateHeight(iface)
