# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow/mainwindow.ui'
#
# Created: Fri Jul 22 22:10:33 2011
#      by: PyQt4 UI code generator 4.7.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1075, 792)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setStatusTip(_fromUtf8(""))
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setDockOptions(QtGui.QMainWindow.AllowNestedDocks|QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setFrameShape(QtGui.QFrame.NoFrame)
        self.splitter.setFrameShadow(QtGui.QFrame.Plain)
        self.splitter.setLineWidth(0)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(7)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.sliceGraphicsView = CustomQGraphicsView(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sliceGraphicsView.sizePolicy().hasHeightForWidth())
        self.sliceGraphicsView.setSizePolicy(sizePolicy)
        self.sliceGraphicsView.setMinimumSize(QtCore.QSize(0, 0))
        self.sliceGraphicsView.setBaseSize(QtCore.QSize(480, 0))
        self.sliceGraphicsView.setMouseTracking(True)
        self.sliceGraphicsView.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.sliceGraphicsView.setFrameShadow(QtGui.QFrame.Plain)
        self.sliceGraphicsView.setLineWidth(0)
        self.sliceGraphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sliceGraphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.sliceGraphicsView.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.TextAntialiasing)
        self.sliceGraphicsView.setDragMode(QtGui.QGraphicsView.NoDrag)
        self.sliceGraphicsView.setTransformationAnchor(QtGui.QGraphicsView.AnchorUnderMouse)
        self.sliceGraphicsView.setResizeAnchor(QtGui.QGraphicsView.AnchorUnderMouse)
        self.sliceGraphicsView.setViewportUpdateMode(QtGui.QGraphicsView.MinimalViewportUpdate)
        self.sliceGraphicsView.setObjectName(_fromUtf8("sliceGraphicsView"))
        self.pathGraphicsView = CustomQGraphicsView(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pathGraphicsView.sizePolicy().hasHeightForWidth())
        self.pathGraphicsView.setSizePolicy(sizePolicy)
        self.pathGraphicsView.setMinimumSize(QtCore.QSize(0, 0))
        self.pathGraphicsView.setMouseTracking(True)
        self.pathGraphicsView.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pathGraphicsView.setFrameShadow(QtGui.QFrame.Plain)
        self.pathGraphicsView.setLineWidth(0)
        self.pathGraphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pathGraphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pathGraphicsView.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.TextAntialiasing)
        self.pathGraphicsView.setViewportUpdateMode(QtGui.QGraphicsView.MinimalViewportUpdate)
        self.pathGraphicsView.setObjectName(_fromUtf8("pathGraphicsView"))
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1075, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuOpen_recent_files = QtGui.QMenu(self.menuFile)
        self.menuOpen_recent_files.setObjectName(_fromUtf8("menuOpen_recent_files"))
        self.menuExport = QtGui.QMenu(self.menuFile)
        self.menuExport.setObjectName(_fromUtf8("menuExport"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        self.menuCADnano = QtGui.QMenu(self.menubar)
        self.menuCADnano.setObjectName(_fromUtf8("menuCADnano"))
        MainWindow.setMenuBar(self.menubar)
        self.topToolBar = QtGui.QToolBar(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topToolBar.sizePolicy().hasHeightForWidth())
        self.topToolBar.setSizePolicy(sizePolicy)
        self.topToolBar.setBaseSize(QtCore.QSize(0, 0))
        self.topToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.topToolBar.setObjectName(_fromUtf8("topToolBar"))
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea(QtCore.Qt.TopToolBarArea), self.topToolBar)
        self.rightToolBar = QtGui.QToolBar(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rightToolBar.sizePolicy().hasHeightForWidth())
        self.rightToolBar.setSizePolicy(sizePolicy)
        self.rightToolBar.setMinimumSize(QtCore.QSize(0, 0))
        self.rightToolBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rightToolBar.setAllowedAreas(QtCore.Qt.LeftToolBarArea|QtCore.Qt.RightToolBarArea|QtCore.Qt.TopToolBarArea)
        self.rightToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.rightToolBar.setObjectName(_fromUtf8("rightToolBar"))
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea(QtCore.Qt.RightToolBarArea), self.rightToolBar)
        self.leftToolBar = QtGui.QToolBar(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftToolBar.sizePolicy().hasHeightForWidth())
        self.leftToolBar.setSizePolicy(sizePolicy)
        self.leftToolBar.setMinimumSize(QtCore.QSize(0, 0))
        self.leftToolBar.setAllowedAreas(QtCore.Qt.LeftToolBarArea|QtCore.Qt.RightToolBarArea|QtCore.Qt.TopToolBarArea)
        self.leftToolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.leftToolBar.setObjectName(_fromUtf8("leftToolBar"))
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea(QtCore.Qt.LeftToolBarArea), self.leftToolBar)
        self.actionNew = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/filetools/new")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionOpen = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/filetools/open")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionClose = QtGui.QAction(MainWindow)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        self.actionSave = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/filetools/save")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSave_As = QtGui.QAction(MainWindow)
        self.actionSave_As.setObjectName(_fromUtf8("actionSave_As"))
        self.actionSave_a_Copy = QtGui.QAction(MainWindow)
        self.actionSave_a_Copy.setObjectName(_fromUtf8("actionSave_a_Copy"))
        self.actionPrint = QtGui.QAction(MainWindow)
        self.actionPrint.setObjectName(_fromUtf8("actionPrint"))
        self.actionSVG = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/filetools/svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSVG.setIcon(icon3)
        self.actionSVG.setObjectName(_fromUtf8("actionSVG"))
        self.actionX3D = QtGui.QAction(MainWindow)
        self.actionX3D.setObjectName(_fromUtf8("actionX3D"))
        self.actionCut = QtGui.QAction(MainWindow)
        self.actionCut.setObjectName(_fromUtf8("actionCut"))
        self.actionCopy = QtGui.QAction(MainWindow)
        self.actionCopy.setObjectName(_fromUtf8("actionCopy"))
        self.actionPaste = QtGui.QAction(MainWindow)
        self.actionPaste.setObjectName(_fromUtf8("actionPaste"))
        self.actionSelect_All = QtGui.QAction(MainWindow)
        self.actionSelect_All.setObjectName(_fromUtf8("actionSelect_All"))
        self.actionNewHoneycombPart = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/parttools/new-honeycomb")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewHoneycombPart.setIcon(icon4)
        self.actionNewHoneycombPart.setObjectName(_fromUtf8("actionNewHoneycombPart"))
        self.actionPathBreak = QtGui.QAction(MainWindow)
        self.actionPathBreak.setCheckable(True)
        self.actionPathBreak.setChecked(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/pathtools/break")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPathBreak.setIcon(icon5)
        self.actionPathBreak.setObjectName(_fromUtf8("actionPathBreak"))
        self.actionPathSelect = QtGui.QAction(MainWindow)
        self.actionPathSelect.setCheckable(True)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/pathtools/select")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPathSelect.setIcon(icon6)
        self.actionPathSelect.setObjectName(_fromUtf8("actionPathSelect"))
        self.actionSliceSelect = QtGui.QAction(MainWindow)
        self.actionSliceSelect.setCheckable(False)
        self.actionSliceSelect.setEnabled(True)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/slicetools/select")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/slicetools/images/slice-edit.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.actionSliceSelect.setIcon(icon7)
        self.actionSliceSelect.setObjectName(_fromUtf8("actionSliceSelect"))
        self.actionSliceFirst = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/slicetools/go first")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSliceFirst.setIcon(icon8)
        self.actionSliceFirst.setObjectName(_fromUtf8("actionSliceFirst"))
        self.actionSliceLast = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/slicetools/go last")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSliceLast.setIcon(icon9)
        self.actionSliceLast.setObjectName(_fromUtf8("actionSliceLast"))
        self.actionPathErase = QtGui.QAction(MainWindow)
        self.actionPathErase.setCheckable(True)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/pathtools/erase")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPathErase.setIcon(icon10)
        self.actionPathErase.setObjectName(_fromUtf8("actionPathErase"))
        self.actionAutoStaple = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/pathtools/autostaple")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAutoStaple.setIcon(icon11)
        self.actionAutoStaple.setObjectName(_fromUtf8("actionAutoStaple"))
        self.actionPathPencil = QtGui.QAction(MainWindow)
        self.actionPathPencil.setCheckable(True)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/pathtools/force")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPathPencil.setIcon(icon12)
        self.actionPathPencil.setObjectName(_fromUtf8("actionPathPencil"))
        self.actionPathInsert = QtGui.QAction(MainWindow)
        self.actionPathInsert.setCheckable(True)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/pathtools/insert")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPathInsert.setIcon(icon13)
        self.actionPathInsert.setObjectName(_fromUtf8("actionPathInsert"))
        self.actionNewSquarePart = QtGui.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/parttools/new-square")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewSquarePart.setIcon(icon14)
        self.actionNewSquarePart.setObjectName(_fromUtf8("actionNewSquarePart"))
        self.actionPathSkip = QtGui.QAction(MainWindow)
        self.actionPathSkip.setCheckable(True)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8(":/pathtools/skip")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPathSkip.setIcon(icon15)
        self.actionPathSkip.setObjectName(_fromUtf8("actionPathSkip"))
        self.actionRenumber = QtGui.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(_fromUtf8(":/slicetools/renumber")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRenumber.setIcon(icon16)
        self.actionRenumber.setObjectName(_fromUtf8("actionRenumber"))
        self.actionDeleteLast = QtGui.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(_fromUtf8(":/slicetools/del-last")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDeleteLast.setIcon(icon17)
        self.actionDeleteLast.setObjectName(_fromUtf8("actionDeleteLast"))
        self.actionPathPaint = QtGui.QAction(MainWindow)
        self.actionPathPaint.setCheckable(True)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(_fromUtf8(":/pathtools/paint")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPathPaint.setIcon(icon18)
        self.actionPathPaint.setObjectName(_fromUtf8("actionPathPaint"))
        self.actionPathAddSeq = QtGui.QAction(MainWindow)
        self.actionPathAddSeq.setCheckable(True)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(_fromUtf8(":/pathtools/add seq")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPathAddSeq.setIcon(icon19)
        self.actionPathAddSeq.setObjectName(_fromUtf8("actionPathAddSeq"))
        self.actionCSV = QtGui.QAction(MainWindow)
        self.actionCSV.setObjectName(_fromUtf8("actionCSV"))
        self.actionPreferences = QtGui.QAction(MainWindow)
        self.actionPreferences.setObjectName(_fromUtf8("actionPreferences"))
        self.actionFrame = QtGui.QAction(MainWindow)
        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap(_fromUtf8(":/pathtools/frame")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFrame.setIcon(icon20)
        self.actionFrame.setObjectName(_fromUtf8("actionFrame"))
        self.menuOpen_recent_files.addSeparator()
        self.menuExport.addAction(self.actionSVG)
        self.menuExport.addAction(self.actionX3D)
        self.menuExport.addAction(self.actionCSV)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.menuOpen_recent_files.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionSave_a_Copy)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuExport.menuAction())
        self.menuFile.addAction(self.actionPrint)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionSelect_All)
        self.menuCADnano.addAction(self.actionPreferences)
        self.menubar.addAction(self.menuCADnano.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.topToolBar.addAction(self.actionNew)
        self.topToolBar.addAction(self.actionOpen)
        self.topToolBar.addAction(self.actionSave)
        self.topToolBar.addSeparator()
        self.topToolBar.addAction(self.actionNewHoneycombPart)
        self.topToolBar.addAction(self.actionNewSquarePart)
        self.topToolBar.addSeparator()
        self.topToolBar.addAction(self.actionFrame)
        self.rightToolBar.addAction(self.actionPathSelect)
        self.rightToolBar.addAction(self.actionPathPencil)
        self.rightToolBar.addAction(self.actionPathBreak)
        self.rightToolBar.addAction(self.actionPathErase)
        self.rightToolBar.addAction(self.actionPathPaint)
        self.rightToolBar.addAction(self.actionPathInsert)
        self.rightToolBar.addAction(self.actionPathSkip)
        self.rightToolBar.addSeparator()
        self.rightToolBar.addAction(self.actionAutoStaple)
        self.rightToolBar.addAction(self.actionPathAddSeq)
        self.leftToolBar.addAction(self.actionSliceFirst)
        self.leftToolBar.addAction(self.actionSliceLast)
        self.leftToolBar.addAction(self.actionRenumber)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionClose, QtCore.SIGNAL(_fromUtf8("activated()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "CADnano", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOpen_recent_files.setTitle(QtGui.QApplication.translate("MainWindow", "Open recent files", None, QtGui.QApplication.UnicodeUTF8))
        self.menuExport.setTitle(QtGui.QApplication.translate("MainWindow", "Export...", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuCADnano.setTitle(QtGui.QApplication.translate("MainWindow", "CADnano", None, QtGui.QApplication.UnicodeUTF8))
        self.topToolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Main Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.rightToolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Path Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.leftToolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Slice Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("MainWindow", "New...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setText(QtGui.QApplication.translate("MainWindow", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClose.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+W", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_As.setText(QtGui.QApplication.translate("MainWindow", "Save As...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_As.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Shift+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_a_Copy.setText(QtGui.QApplication.translate("MainWindow", "Save a Copy...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPrint.setText(QtGui.QApplication.translate("MainWindow", "Print...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSVG.setText(QtGui.QApplication.translate("MainWindow", "SVG", None, QtGui.QApplication.UnicodeUTF8))
        self.actionX3D.setText(QtGui.QApplication.translate("MainWindow", "X3D", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setText(QtGui.QApplication.translate("MainWindow", "Cut", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCut.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+X", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setText(QtGui.QApplication.translate("MainWindow", "Copy", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopy.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+C", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setText(QtGui.QApplication.translate("MainWindow", "Paste", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPaste.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+V", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelect_All.setText(QtGui.QApplication.translate("MainWindow", "Select All", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelect_All.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewHoneycombPart.setText(QtGui.QApplication.translate("MainWindow", "Honeycomb", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewHoneycombPart.setToolTip(QtGui.QApplication.translate("MainWindow", "Click to add new part with honeycomb lattice", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathBreak.setText(QtGui.QApplication.translate("MainWindow", "Break Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathBreak.setIconText(QtGui.QApplication.translate("MainWindow", "Break", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathBreak.setToolTip(QtGui.QApplication.translate("MainWindow", "(B)reak Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathBreak.setShortcut(QtGui.QApplication.translate("MainWindow", "B", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathSelect.setText(QtGui.QApplication.translate("MainWindow", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathSelect.setIconText(QtGui.QApplication.translate("MainWindow", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathSelect.setToolTip(QtGui.QApplication.translate("MainWindow", "Select Tool (v)", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathSelect.setShortcut(QtGui.QApplication.translate("MainWindow", "V", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSliceSelect.setText(QtGui.QApplication.translate("MainWindow", "Select", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSliceSelect.setShortcut(QtGui.QApplication.translate("MainWindow", "Shift+V", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSliceFirst.setText(QtGui.QApplication.translate("MainWindow", "First", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSliceFirst.setToolTip(QtGui.QApplication.translate("MainWindow", "Move the slice bar to the first position.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSliceLast.setText(QtGui.QApplication.translate("MainWindow", "Last", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSliceLast.setToolTip(QtGui.QApplication.translate("MainWindow", "Move the slice bar to the last position.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathErase.setText(QtGui.QApplication.translate("MainWindow", "Erase", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathErase.setToolTip(QtGui.QApplication.translate("MainWindow", "(E)rase Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathErase.setShortcut(QtGui.QApplication.translate("MainWindow", "E", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAutoStaple.setText(QtGui.QApplication.translate("MainWindow", "Staple", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAutoStaple.setToolTip(QtGui.QApplication.translate("MainWindow", "Click this button to generate a default set of staples.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathPencil.setText(QtGui.QApplication.translate("MainWindow", "Pencil", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathPencil.setToolTip(QtGui.QApplication.translate("MainWindow", "Pe(n)cil Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathPencil.setShortcut(QtGui.QApplication.translate("MainWindow", "N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathInsert.setText(QtGui.QApplication.translate("MainWindow", "Insert", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathInsert.setToolTip(QtGui.QApplication.translate("MainWindow", "(I)nsert Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathInsert.setShortcut(QtGui.QApplication.translate("MainWindow", "I", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewSquarePart.setText(QtGui.QApplication.translate("MainWindow", "Square", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewSquarePart.setToolTip(QtGui.QApplication.translate("MainWindow", "Click to add new part with square lattice", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathSkip.setText(QtGui.QApplication.translate("MainWindow", "Skip", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathSkip.setToolTip(QtGui.QApplication.translate("MainWindow", "(S)kip Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathSkip.setShortcut(QtGui.QApplication.translate("MainWindow", "S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRenumber.setText(QtGui.QApplication.translate("MainWindow", "Rnum", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRenumber.setToolTip(QtGui.QApplication.translate("MainWindow", "Renumber Slice helices according to helix ordering in Path panel.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeleteLast.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeleteLast.setToolTip(QtGui.QApplication.translate("MainWindow", "Remove the highest-numbered helix if it does not connect to any other helices.", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathPaint.setText(QtGui.QApplication.translate("MainWindow", "Paint", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathPaint.setToolTip(QtGui.QApplication.translate("MainWindow", "(P)aint Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathPaint.setShortcut(QtGui.QApplication.translate("MainWindow", "P", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathAddSeq.setText(QtGui.QApplication.translate("MainWindow", "Seq", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathAddSeq.setToolTip(QtGui.QApplication.translate("MainWindow", "(A)dd Sequence Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPathAddSeq.setShortcut(QtGui.QApplication.translate("MainWindow", "A", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCSV.setText(QtGui.QApplication.translate("MainWindow", "CSV", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCSV.setToolTip(QtGui.QApplication.translate("MainWindow", "export oligos as *.CSV", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate("MainWindow", "Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+,", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFrame.setText(QtGui.QApplication.translate("MainWindow", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFrame.setShortcut(QtGui.QApplication.translate("MainWindow", "F", None, QtGui.QApplication.UnicodeUTF8))

from views.customqgraphicsview import CustomQGraphicsView
import icons_rc
