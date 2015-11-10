from PyQt4 import QtGui,QtCore
from PyQt4.QtGui import *
import os,sys 
 

class Image(QLabel):
	def __init__(self, parent=None):
		super(Image, self).__init__(parent)
		self.setAcceptDrops(True) 
 
	def dragEnterEvent(self, event):
		if event.mimeData().hasUrls():
			event.accept()
		else:
			event.ignore()
 
	def dragMoveEvent(self, event):
		if event.mimeData().hasUrls():
			event.setDropAction(QtCore.Qt.CopyAction)
			event.accept()
		else:
			event.ignore()
 
	def dropEvent(self, event):
		if event.mimeData().hasUrls():
			event.setDropAction(QtCore.Qt.CopyAction)
			event.accept()
			l = []
			for url in event.mimeData().urls():
				url=str(url.toLocalFile())
				print 'DragDropListWidget ',url
				icon = QPixmap(url)				
				self.setPixmap(icon.scaled(600,600,QtCore.Qt.KeepAspectRatio))
  
		else:
			event.ignore()


class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow,self).__init__()
		self.statusBar().showMessage("ready...")
		self.setGeometry(200,200,600,600)
		self.setWindowTitle("demo")
		
		exitAction=QAction('&Exit',self)
		exitAction.triggered.connect(QtGui.qApp.quit)

		fileMenu=self.menuBar().addMenu("&File")
		editMenu=self.menuBar().addMenu("&Edit")
		fileMenu.addAction(exitAction)
		editMenu.addAction(exitAction)
 
		self.image=Image(self)
		self.setCentralWidget(self.image) 
 

if __name__=="__main__":
	app=QApplication(sys.argv)
	wnd=MainWindow()
	wnd.show()
	sys.exit(app.exec_())