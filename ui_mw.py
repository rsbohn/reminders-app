# Form implementation generated from reading ui file 'ignore\main_window.ui'
#
# Created by: PyQt6 UI code generator 6.5.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1146, 609)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 1121, 541))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.listViewReminders = QtWidgets.QListView(parent=self.layoutWidget)
        self.listViewReminders.setObjectName("listViewReminders")
        self.verticalLayout_2.addWidget(self.listViewReminders)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(0, 25))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.line = QtWidgets.QFrame(parent=self.layoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEditReminderName = QtWidgets.QLineEdit(parent=self.layoutWidget)
        self.lineEditReminderName.setObjectName("lineEditReminderName")
        self.horizontalLayout_2.addWidget(self.lineEditReminderName)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.dateTimeEditDueDate = QtWidgets.QDateTimeEdit(parent=self.layoutWidget)
        self.dateTimeEditDueDate.setObjectName("dateTimeEditDueDate")
        self.horizontalLayout.addWidget(self.dateTimeEditDueDate)
        self.pushButtonEditDueDate = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButtonEditDueDate.setObjectName("pushButtonEditDueDate")
        self.horizontalLayout.addWidget(self.pushButtonEditDueDate)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.spinBoxFuzziness = QtWidgets.QSpinBox(parent=self.layoutWidget)
        self.spinBoxFuzziness.setObjectName("spinBoxFuzziness")
        self.horizontalLayout_3.addWidget(self.spinBoxFuzziness)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.comboBoxFrequency = QtWidgets.QComboBox(parent=self.layoutWidget)
        self.comboBoxFrequency.setObjectName("comboBoxFrequency")
        self.horizontalLayout_4.addWidget(self.comboBoxFrequency)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.checkBoxComplete = QtWidgets.QCheckBox(parent=self.layoutWidget)
        self.checkBoxComplete.setObjectName("checkBoxComplete")
        self.horizontalLayout_5.addWidget(self.checkBoxComplete)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButtonSaveChanges = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButtonSaveChanges.setObjectName("pushButtonSaveChanges")
        self.horizontalLayout_6.addWidget(self.pushButtonSaveChanges)
        self.pushButtonCancelChanges = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButtonCancelChanges.setObjectName("pushButtonCancelChanges")
        self.horizontalLayout_6.addWidget(self.pushButtonCancelChanges)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.line_2 = QtWidgets.QFrame(parent=self.layoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(parent=self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(0, 25))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.pushButtonAddAvenue = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButtonAddAvenue.setObjectName("pushButtonAddAvenue")
        self.horizontalLayout_7.addWidget(self.pushButtonAddAvenue)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButtonAPI = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButtonAPI.setObjectName("pushButtonAPI")
        self.gridLayout_2.addWidget(self.pushButtonAPI, 2, 0, 1, 1)
        self.avenue_name = QtWidgets.QLabel(parent=self.layoutWidget)
        self.avenue_name.setMaximumSize(QtCore.QSize(16777215, 25))
        self.avenue_name.setObjectName("avenue_name")
        self.gridLayout_2.addWidget(self.avenue_name, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)
        self.pushButtonTest = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.pushButtonTest.setObjectName("pushButtonTest")
        self.gridLayout_2.addWidget(self.pushButtonTest, 2, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_2)
        self.verticalLayout_3.addLayout(self.verticalLayout_5)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.listViewAvenues = QtWidgets.QListView(parent=self.layoutWidget)
        self.listViewAvenues.setObjectName("listViewAvenues")
        self.verticalLayout_4.addWidget(self.listViewAvenues)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1146, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_Reminder = QtGui.QAction(parent=MainWindow)
        self.actionNew_Reminder.setObjectName("actionNew_Reminder")
        self.actionNew_Set = QtGui.QAction(parent=MainWindow)
        self.actionNew_Set.setObjectName("actionNew_Set")
        self.actionLoad_Set = QtGui.QAction(parent=MainWindow)
        self.actionLoad_Set.setObjectName("actionLoad_Set")
        self.actionSave = QtGui.QAction(parent=MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtGui.QAction(parent=MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.menuFile.addAction(self.actionNew_Reminder)
        self.menuFile.addAction(self.actionNew_Set)
        self.menuFile.addAction(self.actionLoad_Set)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Reminders App"))
        self.label_6.setText(_translate("MainWindow", "Reminders"))
        self.label_7.setText(_translate("MainWindow", "Selected Reminder:"))
        self.label_2.setText(_translate("MainWindow", "Reminder Name:"))
        self.label.setText(_translate("MainWindow", "Due Date:"))
        self.pushButtonEditDueDate.setText(_translate("MainWindow", "Edit..."))
        self.label_3.setText(_translate("MainWindow", "Fuzziness:"))
        self.label_5.setText(_translate("MainWindow", "Frequency:"))
        self.checkBoxComplete.setText(_translate("MainWindow", "Complete?"))
        self.pushButtonSaveChanges.setText(_translate("MainWindow", "Save Changes"))
        self.pushButtonCancelChanges.setText(_translate("MainWindow", "Cancel Changes"))
        self.label_8.setText(_translate("MainWindow", "Avenue Info"))
        self.pushButtonAddAvenue.setText(_translate("MainWindow", "New Avenue..."))
        self.pushButtonAPI.setText(_translate("MainWindow", "Hook Up API..."))
        self.avenue_name.setText(_translate("MainWindow", "avenue_name"))
        self.label_9.setText(_translate("MainWindow", "Name:"))
        self.pushButtonTest.setText(_translate("MainWindow", "Test"))
        self.label_4.setText(_translate("MainWindow", "Reminder Avenues"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionNew_Reminder.setText(_translate("MainWindow", "New Reminder..."))
        self.actionNew_Set.setText(_translate("MainWindow", "New Set..."))
        self.actionLoad_Set.setText(_translate("MainWindow", "Load Set..."))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())