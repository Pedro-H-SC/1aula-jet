


nome = str(input('Digite seu nome:'))

idade= int(input('Digite sua idade:'))

ano=int(input('Digite sua serie:'))



if(idade==0):
    print('Idade invalida')
    
else:
    if(ano>0 or ano>3):
        print('Seu nome é', nome,', sua idade é' ,idade, ', serie serie é',ano,'º' )
        
    else:
        print('Serie invalida')
        
        
