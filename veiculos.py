# -*- coding: utf-8 -*-
"""Veiculos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cNhApXm3dowliTdvfS_xaGqUku5fig-t
"""

qnt_rodas = 4
qnt_pessoas = 8
peso_bruto = 4.500

if(qnt_rodas <= 3):
  print("A")
elif(qnt_rodas == 4 and qnt_pessoas <= 8 and peso_bruto <= 3.500):
  print("B")
elif(qnt_rodas >= 4 and peso_bruto >= 3.500 and peso_bruto <= 6.000):
  print("C")
elif(qnt_rodas >= 4 and qnt_pessoas > 8):
  print("D")
elif(qnt_rodas >= 4 and peso_bruto > 6.000):
  print("E")