import os
import sys

from rv import rvtypes, commands
import widget_form


sys.path.append('/home/aberg/py26/lib/python2.6/site-packages')

from PyQt4 import QtGui
from PyQt4 import QtCore

class GradeWidget(QtGui.QWidget, widget_form.Ui_Form):
    def __init__(self):
        super(GradeWidget, self).__init__()
        self.setupUi(self)

class DockWidget(QtGui.QDockWidget):
    def __init__(self, parent=None):
        super(DockWidget, self).__init__(parent)
        self.setWindowTitle('Colourista')
        self.setWidget(GradeWidget())


class PropertyMode(rvtypes.MinorMode):
    """
    property explorer
    """

    def show_panel(self, event):

        # odd, need to keep a reference to the widget here or the
        # signals wouldn't come through
        if self.dock_wid is None:
            self.dock_wid = DockWidget()
        self.dock_wid.show()

        main_win = self.get_main_window()
        if not main_win:
            return
        main_win.addDockWidget(QtCore.Qt.BottomDockWidgetArea, self.dock_wid)


    def get_main_window(self):
        widgets = QtGui.QApplication.topLevelWidgets()
        for wid in widgets:
            if not isinstance(wid, QtGui.QMainWindow):
                continue
            return wid


    def __init__(self):
        rvtypes.MinorMode.__init__(self)
        self.dock_wid = None
        self.init("ColouristaPanel",
                  None,
                  None,
                  [
                      ("Tools",
                       [("Colourista Panel", self.show_panel, None, None)]
                      )
                  ]
        )


def createMode():
    "Required to initialize the module. RV will call this function to create your mode."
    return PropertyMode()
