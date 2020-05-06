# 1 методами строк очистить текст от знаков препинания;
#################
print()
str = '!!!Погружение в IT-профессию!!! подразумевает постоянный контакт с изучаемыми технологиями, выполнение практических заданий и общение с наставником. Для этого мы создали собственную среду обучения.'

# str = str.replace(',', '').replace('.', '').replace(';','').replace('—','').replace('«','').replace('»','').replace('?','').replace('!','').replace('(','').replace(')','')
# print(str)

#################

# 2 сформировать list со словами (split);

#################
answer2 = str.split()
print(answer2)
#################
# 3 привести все слова к нижнему регистру (map);
#################
answer3 = list(map(lambda x: x.lower(), answer2))
print(answer3)
#################
# 4 получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;
#################
answer4 = {}
dict = answer3 * 1
for i in list(dict):
    counts = 0
    while i in list(dict):
        if i in list(dict):
            # print(list(str5))
            counts += 1
            dict.remove(i)
            answer4[i] = counts
print(answer4)
#################
# 5 вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).
#################

list_answer4 = list(answer4.items())
list_answer4.sort(key=lambda i: i[1])
list_answer4.reverse()
count = 0
often_words = ''
for i in list_answer4:
    if count != 5:
        count += 1
        often_words += i[0] + ', '
print('5 наиболее часто встречающихся слов: ', often_words)

set_one = set(answer3)
set_second = set(answer3)
set_third = set_one.intersection(set_second)
count = 0
for i in set_third:
    count += 1
print('Количество разных слов: ', count)
#################

