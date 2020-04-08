Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> "Teste para ser fatiado"[0:6]
'Teste '
>>> "Teste para ser fatiado"[0:10]
'Teste para'
>>> "Teste para ser fatiado"[3:10]
'te para'
>>> "Teste para ser fatiado"[:10]
'Teste para'
>>> "Teste para ser fatiado"[0:]
'Teste para ser fatiado'
>>> "Teste para ser fatiado"[0:10:3]
'Ttpa'
>>> "Teste para ser fatiado"[::-1]
'odaitaf res arap etseT'
>>> nome = "ana"
>>> nome == nome[::-1]
True
>>> 
>>> 
>>> nome = "Marcos"
>>> nome
'Marcos'
>>> nome = 'B' + nome[1:]
>>> nome
'Barcos'
>>> nome.startwwiths('B')
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    nome.startwwiths('B')
AttributeError: 'str' object has no attribute 'startwwiths'
>>> nome.startwiths('B')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    nome.startwiths('B')
AttributeError: 'str' object has no attribute 'startwiths'
>>> nome.startwiths('B')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    nome.startwiths('B')
AttributeError: 'str' object has no attribute 'startwiths'
>>> nome.startwith('B')
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    nome.startwith('B')
AttributeError: 'str' object has no attribute 'startwith'
>>> nome.startswith('B')
True
>>> nome.startswith('b')
False
>>> nome.replace('r', '3')
'Ba3cos'
>>> texto = 'Testando split no python'
>>> texto
'Testando split no python'
>>> s =texto.split()
>>> s
['Testando', 'split', 'no', 'python']
>>> data = ['18', '05', '1979']
>>> data
['18', '05', '1979']
>>> '/'.join(data)
'18/05/1979'
>>> 
