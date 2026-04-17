'''
Uma instituição de ensino avalia seus alunos ao longo do semestre com base em
diferentes atividades.
'''

cp1 = float(input('Digite a nota do primeiro checkpoint (0 a 10)  : '))
cp2 = float(input('Digite a nota do segundo checkpoint (0 a 10) : '))
cp3 = float(input('Digite a nota do terceiro checkpoint (0 a 10) : '))
sp1 = float(input('Digite a nota da primeira sprint (0 a 10) : '))
sp2 = float(input('Digite a nota da segunda sprint (0 a 10) : '))
gs = float(input('Digite a nota da Global Solution (0 a 10) : '))

if cp1 <= cp2 and cp1 <= cp3:
    menor = cp1
elif cp2 <= cp3:
    menor = cp2
else:
    menor = cp3

#Média
media = ((cp1+cp2+cp3-menor+ sp1 +sp2)/4)*0.4 +(gs * 0.6)
#Média com peso
mediaPeso = media * 0.4

print(f'\nA média do semestre : {media:.1f} \nMédia do primeiro semestre com peso ficou : {mediaPeso:.1f}')



