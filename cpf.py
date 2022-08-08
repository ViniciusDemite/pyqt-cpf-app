from PyQt5.QtWidgets import QMainWindow
from design import *
from random import randint
import re


class CpfApp(QMainWindow, Ui_MainWindow):
  def __init__(self, parent=None):
    super().__init__(parent)
    super().setupUi(self)
    self.cpf: str = ''
    self.btnValidateCpf.clicked.connect(self.validate_cpf)
    self.btnGenerateCpf.clicked.connect(self.generate_cpf)

  def validate_cpf(self) -> None:
    self.cpf = self._remove_especial_chars(self.inputCpf.text())
    cpf_without_digits = self.cpf[:-2]

    cpf = self._validate(cpf_without_digits)

    if cpf != self.cpf:
      print(cpf, self.cpf)
      self.labelResponse.setText('CPF INVÁLIDO')
      self.labelResponse.setStyleSheet('color: red;')
      return

    self.labelResponse.setText('CPF VÁLIDO')
    self.labelResponse.setStyleSheet('color: green;')

  def generate_cpf(self) -> None:
    cpf_without_digits = str(randint(100000000, 999999999))

    cpf = self._validate(cpf_without_digits)

    self.labelGeneratedCpf.setText(self._format_cpf(cpf))

  def _validate(self, cpf_without_digits: str) -> str:
    cpf: str = cpf_without_digits

    for _ in range(0, 2):
      digit = str(
        self._calculateDigit(
          self._calculateTotal(cpf)
        )
      )

      cpf += digit

    return cpf

  @staticmethod
  def _calculateDigit(value: int) -> int:
    digit = 11 - (value % 11)

    return digit if digit <= 9 else 0

  @staticmethod
  def _calculateTotal(incomplete_cpf: str) -> int:
    total = 0

    for i, number in enumerate(reversed(incomplete_cpf), start=2):
      total += int(number) * i

    return total

  @staticmethod
  def _format_cpf(cpf: str) -> str:
    if len(cpf) != 11:
      raise ValueError('O CPF passado não tem o mínimo de 11 caracteres!!')

    return '{}.{}.{}-{}'.format(
      cpf[:3], cpf[3:6], cpf[6:9], cpf[9:]
    )

  @staticmethod
  def _remove_especial_chars(cpf: str) -> str:
    return re.sub(r'[^0-9]', '', cpf)
