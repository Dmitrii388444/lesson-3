# 1 методами строк очистить текст от знаков препинания;
#################

import pymorphy2
morph = pymorphy2.MorphAnalyzer()

tfile = open('text.txt',encoding='utf-8')
text=tfile.read()

str = 'text'

 str = str.replace(',', '').replace('.', '').replace(';','').replace('—','').replace('«','').replace('»','').replace('?','').replace('!','').replace('(','').replace(')','')
 print(str)

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
tdict = answer3 * 1
for i in list(tdict):
    counts = 0
    while i in list(tdict):
        if i in list(tdict):

            counts += 1
            tdict.remove(i)
            answer4[i] = counts
print(answer4)
#################
# 5 вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).
#################

text_list=str.split()
print('Создаём List')
print(text_list)
# Приводим к нижнему регистру
text_list=list(map(lambda x: x.lower(),text_list))
print('Приводим к нижнему регистру')
print(text_list)
# Получаем нормальную форму
text_list=list(map(lambda x: morph.parse(x)[0].normal_form,text_list))
print('Получаем нормальную форму')
print(text_list)
text_dict={a:text_list.count(a) for a in text_list}
print('Создание словаря СЛОВО:ВСТРЕЧАЕТСЯ')
print(text_dict)

sort_list=list(text_dict.items())
sort_list.sort(key=lambda i: i[1],reverse=True)
print('5 наиболее встречающихся')
print(sort_list[:5])
#################

