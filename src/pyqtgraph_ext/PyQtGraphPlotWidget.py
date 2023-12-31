""" PlotWidget with matlab color scheme and CustomPlotItem.
"""

from __future__ import annotations
from qtpy.QtCore import *
from qtpy.QtGui import *
from qtpy.QtWidgets import *
import pyqtgraph as pg
from pyqtgraph_ext import PlotItem
import platform


class PlotWidget(pg.PlotWidget):
    """ PlotWidget with matlab color scheme and CustomPlotItem. """

    def __init__(self, *args, **kwargs):
        if 'plotItem' not in kwargs:
            kwargs['plotItem'] = PlotItem()
        pg.PlotWidget.__init__(self, *args, **kwargs)

        # MATLAB color scheme
        self.setBackground(QColor(240, 240, 240))

        if platform.system() == 'Darwin':
            # Fix error message due to touch events on MacOS trackpad.
            # !!! Warning: This may break touch events on a touch screen or mobile device.
            # See https://bugreports.qt.io/browse/QTBUG-103935
            for view in self.scene().views():
                view.viewport().setAttribute(Qt.WidgetAttribute.WA_AcceptTouchEvents, False)


def test_live():
    import sys
    import numpy as np
    from pyqtgraph_ext import XYDataItem
    app = QApplication(sys.argv)
    plot = PlotWidget()
    for i in range(3):
        line = XYDataItem(y=np.random.randn(10), lineWidth=2)
        plot.addItem(line)
    line = XYDataItem(y=np.random.randn(10))
    plot.addItem(line)
    plot.setWindowTitle('pyqtgraph-tools')
    plot.show()
    status = app.exec()
    sys.exit(status)


if __name__ == '__main__':
    test_live()
