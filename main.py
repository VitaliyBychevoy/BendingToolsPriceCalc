import sys

from PyQt5 import QtWidgets, uic
#from PyQt5.QtWidgets import QApplication, QMainWindow

type_item_list = [
	"Оберіть тип кріплення",
	"Amada",
	"Trumpf",
	"Wila",
	"Bystronic"
]

item_list = [
	"Пуансон",
	"Матриця",
	"Пуансон плющення",
	"Матриця плющення",
]


class Ui(QtWidgets.QMainWindow):
	def __init__(self):
		super(Ui, self).__init__()
		uic.loadUi("BendingPriceCalc.ui", self)
		for item_connection in type_item_list:
			self.type_value.addItem(item_connection)

		self.item_value.addItem("Оберіть тип кріплення")
		self.number_value.addItem("?")
		self.length_value.addItem("Оберіть номер виробу")
		# if self.type_value.currentText() == "Оберіть тип кріплення":
		# 	self.item_value.clear()
		# 	self.item_value.addItem(self.type_value)
		# else:
		# 	self.item_value.clear()
		# 	self.item_value.addItem("Заглушка")
		#print(type(self.type_value.currentText()))

		self.show()


app = QtWidgets.QApplication(sys.argv)
window = Ui()

app.exec_()

