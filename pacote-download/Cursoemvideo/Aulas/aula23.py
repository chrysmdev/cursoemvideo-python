# AULA 23
# TRATAMENTO DE ERROS E EXCEÇÕES

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except:
    print('Infelizmente tivemos um problema... :(')
else:
    print(f'O resultado foi: {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado')

#
  
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b   
except Exception as erro:
    print(f'Problema encontrado foi: {erro.__class__}')
else:
    print(f'O resultado foi: {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado')
    
#

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b   
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as error:
    print(f'O erro encontrado foi: {error.__cause__}')
else:
    print(f'O resultado foi: {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado')
    
