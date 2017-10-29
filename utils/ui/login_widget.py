# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'utils\ui\files\LoginWidget.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):
    # "Login Info" font
    header_font = QtGui.QFont()
    header_font.setFamily("Consolas")
    header_font.setPointSize(16)

    # Body font
    body_font = header_font
    body_font.setPointSize(10)
    
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(800, 600)
        LoginWindow.setDocumentMode(False)
        LoginWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.LoginWidget = QtWidgets.QWidget(LoginWindow)
        self.LoginWidget.setStyleSheet("color: #EDEDED;\n"
"    background-color: #212121;\n"
"    line-height: 2;")
        self.LoginWidget.setObjectName("LoginWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.LoginWidget)
        self.gridLayout.setContentsMargins(9, 9, 9, 9)
        self.gridLayout.setObjectName("gridLayout")
        self.MainPanel = QtWidgets.QWidget(self.LoginWidget)
        self.MainPanel.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.MainPanel.setObjectName("MainPanel")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.MainPanel)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.PanelSplitter = QtWidgets.QSplitter(self.MainPanel)
        self.PanelSplitter.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.PanelSplitter.setOrientation(QtCore.Qt.Vertical)
        self.PanelSplitter.setObjectName("PanelSplitter")
        self.UserInfoHeader = QtWidgets.QLabel(self.PanelSplitter)

        self.UserInfoHeader.setFont(self.header_font)
        self.UserInfoHeader.setStyleSheet("color: #EDEDED;\n"
"            background-color: #212121;")
        self.UserInfoHeader.setTextFormat(QtCore.Qt.PlainText)
        self.UserInfoHeader.setAlignment(QtCore.Qt.AlignCenter)
        self.UserInfoHeader.setObjectName("UserInfoHeader")
        self.FormWidget = QtWidgets.QWidget(self.PanelSplitter)
        self.FormWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.FormWidget.setStyleSheet(
                """color: #EDEDED;\n
                background-color: #212121;\n"""
        )

        self.FormWidget.setObjectName("FormWidget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.FormWidget)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem)

        # Username text
        self.UsernameText = QtWidgets.QLabel(self.FormWidget)

        self.UsernameText.setFont(self.body_font)
        # self.UsernameText.setStyleSheet(
        #         """color: #EDEDED;\n
        #            background-color: #212121;"""
        # )
        self.UsernameText.setTextFormat(QtCore.Qt.PlainText)
        self.UsernameText.setObjectName("UsernameText")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.UsernameText)

        # Username field
        self.UsernameField = QtWidgets.QLineEdit(self.FormWidget)

        self.UsernameField.setFont(self.body_font)
        # self.UsernameField.setStyleSheet(
        #         """color: #EDEDED;\n
        #            background-color: #212121;"""
        # )
        self.UsernameField.setFrame(False)
        self.UsernameField.setObjectName("UsernameField")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.UsernameField)

        # Password text
        self.PasswordText = QtWidgets.QLabel(self.FormWidget)

        self.PasswordText.setFont(self.body_font)
        self.PasswordText.setStyleSheet("color: #EDEDED;\n"
"                background-color: #212121;")
        self.PasswordText.setTextFormat(QtCore.Qt.PlainText)
        self.PasswordText.setObjectName("PasswordText")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.PasswordText)

        # Password field
        self.PasswordField = QtWidgets.QLineEdit(self.FormWidget)

        self.PasswordField.setFont(self.body_font)
        self.PasswordField.setStyleSheet("color: #EDEDED;\n"
"              background-color: #212121;")
        self.PasswordField.setInputMask("")
        self.PasswordField.setFrame(False)
        self.PasswordField.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordField.setObjectName("PasswordField")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.PasswordField)

        # Login button
        self.LoginButton = QtWidgets.QPushButton(self.FormWidget)
        self.LoginButton.setEnabled(True)

        self.LoginButton.setFont(self.body_font)
        self.LoginButton.setStyleSheet("color: #EDEDED;\n"
"              background-color: #434343;")
        self.LoginButton.setAutoDefault(True)
        self.LoginButton.setDefault(True)
        self.LoginButton.setFlat(False)
        self.LoginButton.setObjectName("LoginButton")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.LoginButton)

        # Error text
        self.ErrorText = QtWidgets.QLabel(self.FormWidget)
        self.ErrorText.setEnabled(True)

        self.ErrorText.setFont(self.body_font)
        self.ErrorText.setStyleSheet("background-color: #212121;\n"
"              color: #F44336;")
        self.ErrorText.setText("")
        self.ErrorText.setTextFormat(QtCore.Qt.PlainText)
        self.ErrorText.setAlignment(QtCore.Qt.AlignCenter)
        self.ErrorText.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.ErrorText.setObjectName("ErrorText")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.ErrorText)
        spacerItem1 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(6, QtWidgets.QFormLayout.FieldRole, spacerItem1)

        # Address text
        self.AddressText = QtWidgets.QLabel(self.FormWidget)

        self.AddressText.setFont(self.body_font)
        self.AddressText.setStyleSheet("color: #EDEDED;\n"
"              background-color: #212121;")
        self.AddressText.setTextFormat(QtCore.Qt.PlainText)
        self.AddressText.setObjectName("AddressText")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.AddressText)

        # Address field
        self.AddressField = QtWidgets.QLineEdit(self.FormWidget)

        self.AddressField.setFont(self.body_font)
        self.AddressField.setStyleSheet("color: #EDEDED;\n"
"              background-color: #212121;")
        self.AddressField.setInputMask("")
        self.AddressField.setFrame(False)
        self.AddressField.setObjectName("AddressField")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.AddressField)

        # Port text
        self.PortText = QtWidgets.QLabel(self.FormWidget)

        self.PortText.setFont(self.body_font)
        self.PortText.setStyleSheet("color: #EDEDED;\n"
"              background-color: #212121;")
        self.PortText.setTextFormat(QtCore.Qt.PlainText)
        self.PortText.setObjectName("PortText")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.PortText)

        # Port field
        self.PortField = QtWidgets.QLineEdit(self.FormWidget)

        self.PortField.setFont(self.body_font)
        self.PortField.setStyleSheet("color: #EDEDED;\n"
"              background-color: #212121;")
        self.PortField.setInputMask("")
        self.PortField.setFrame(False)
        self.PortField.setObjectName("PortField")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.PortField)

        # Enable Markdown Text
        self.MarkdownText = QtWidgets.QLabel(self.FormWidget)

        self.MarkdownText.setFont(self.body_font)
        # self.MarkdownText.setStyleSheet("color: #EDEDED;\n"
        # "background-color: #212121;")
        self.MarkdownText.setTextFormat(QtCore.Qt.PlainText)
        self.MarkdownText.setObjectName("MarkdownText")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.MarkdownText)

        # Enable Markdown Check button
        self.MarkdownCheck = QtWidgets.QCheckBox(self.FormWidget)

        self.MarkdownCheck.setFont(self.body_font)
        # self.MarkdownCheck.setStyleSheet("color: #EDEDED;\n"
        # "background-color: #212121;")
        self.MarkdownCheck.setTristate(False)
        self.MarkdownCheck.setObjectName("MarkdownCheck")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.MarkdownCheck)
        self.verticalLayout.addWidget(self.PanelSplitter)
        self.gridLayout.addWidget(self.MainPanel, 0, 0, 1, 1)
        LoginWindow.setCentralWidget(self.LoginWidget)

        # Secure (wss://) text
        self.SecureText = QtWidgets.QLabel(self.FormWidget)
        self.SecureText.setFont(self.body_font)
        self.SecureText.setTextFormat(QtCore.Qt.PlainText)
        self.SecureText.setObjectName("SecureText")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.SecureText)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

        # Secure (wss://) Check button
        self.SecureCheck = QtWidgets.QCheckBox(self.FormWidget)

        self.SecureCheck.setFont(self.body_font)
        # self.MarkdownCheck.setStyleSheet("color: #EDEDED;\n"
        # "background-color: #212121;")
        self.SecureCheck.setTristate(False)
        self.SecureCheck.setObjectName("SecureCheck")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.SecureCheck)
        self.verticalLayout.addWidget(self.PanelSplitter)
        self.gridLayout.addWidget(self.MainPanel, 0, 0, 1, 1)
        LoginWindow.setCentralWidget(self.LoginWidget)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "LoginWindow"))
        self.LoginWidget.setWindowTitle(_translate("LoginWindow", "Form"))
        self.UserInfoHeader.setText(_translate("LoginWindow", "Login Info"))
        self.UsernameText.setText(_translate("LoginWindow", "Username"))
        self.UsernameField.setPlaceholderText(_translate("LoginWindow", "> Username"))
        self.PasswordText.setText(_translate("LoginWindow", "Password"))
        self.PasswordField.setPlaceholderText(_translate("LoginWindow", "> Password"))
        self.LoginButton.setText(_translate("LoginWindow", "Login"))
        self.AddressText.setText(_translate("LoginWindow", "Address"))
        self.AddressField.setPlaceholderText(_translate("LoginWindow", "> IP address or hostname"))
        self.PortText.setText(_translate("LoginWindow", "Port"))
        self.PortField.setPlaceholderText(_translate("LoginWindow", "> Port"))
        self.MarkdownText.setText(_translate("LoginWindow", "Enable Markdown"))
        self.SecureText.setText(_translate("LoginWindow", "Secure Connect"))
