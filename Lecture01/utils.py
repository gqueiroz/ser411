# encoding: utf-8
import sys

# Carrega a Biblioteca GDAL/OGR
try:
    from osgeo import ogr
except:
    sys.exit("ERRO: Biblioteca GDAL/OGR não encontrada!")


def Geo2Grid(location, dimensions, resolution, extent):
    """
    Converts a geographic coordinate position to a regular grid coordinate.

    Args:
        location (Geometry): A geometric point with coordinates X and Y.
        dimensions (dict): The number of columns and rows in the grid.
        resolution (dict): The spatial resolution along the X and Y coordinates.
        extent (dict): The spatial extent associated to the grid.


    Returns:
        (int, int): the grid column and row where the point lies in.
    """

    x = location.GetX()
    y = location.GetY()

    col = int( ( x - extent['xmin'] ) / resolution['x'])

    row = int ( dimensions['rows'] - (y - extent['ymin']) / resolution['y'] )

    return col, row
