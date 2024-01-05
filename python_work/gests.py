gests = ['іван', 'вася', 'стас', 'павло']
print(f'Hello {gests[0].title()} come to me on 15:00')
print(f'Hello {gests[1].title()} come to me on 15:00')
print(f'Hello {gests[2].title()} come to me on 15:00')
print(f'Hello {gests[3].title()} come to me on 15:00')

print(f'\nНажаль {gests[3].title()} не зможе прийти до нас')

gests[3] = 'Христина'
print(gests)

print(f'\nПривіт {gests} я купив більший стіл тож тепер будуть нові гості нище я скину список')

gests.insert(0, 'Гліб')
print(gests)

gests.insert(5, 'Олеся')
print(gests)

gests.append('Вероніка')
print(gests)

print(f'\nПривіт {gests[0].title()} приходи до мене на 15:00')
print(f'\nПривіт {gests[1].title()} приходи до мене на 15:00')
print(f'\nПривіт {gests[2].title()} приходи до мене на 15:00')
print(f'\nПривіт {gests[3].title()} приходи до мене на 15:00')
print(f'\nПривіт {gests[4].title()} приходи до мене на 15:00')
print(f'\nПривіт {gests[5].title()} приходи до мене на 15:00')
print(f'\nПривіт {gests[6].title()} приходи до мене на 15:00')

print(f'\nПривіт {gests} нажаль тепер я можу прийняти тільки двох гостей')


print(f'\nМені дуже шкода {gests[0]} що я не можу прийняти тебе на свою вечірку')
poped_gests = gests.pop(0)
print(gests)

print(f'\nМені дуже шкода {gests[0]} що я не можу прийняти тебе на свою вечірку')
poped_gests = gests.pop(0)
print(gests)

print(f'\nМені дуже шкода {gests[0]} що я не можу прийняти тебе на свою вечірку')
poped_gests = gests.pop(0)
print(gests)

print(f'\nМені дуже шкода {gests[0]} що я не можу прийняти тебе на свою вечірку')
poped_gests = gests.pop(0)
print(gests)

print(f'\nМені дуже шкода {gests[0]} що я не можу прийняти тебе на свою вечірку')
poped_gests = gests.pop(0)
print(gests)

del gests[0]
print(gests)
del gests[0]
print(gests)
