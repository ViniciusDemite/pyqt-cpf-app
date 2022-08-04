import sys
from cpf import CpfApp
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
  qt = QApplication(sys.argv)
  app = CpfApp()

  app.show()
  qt.exec_()