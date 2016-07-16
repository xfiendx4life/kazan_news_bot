import random
to_do = ["Взять", "Добавить"]
ingrs = ["Масло календулы", "Парацетомол", "Чеснок", "Аспирин", "Экстракт слона"]
the_way_to = ["Втирать", "Выпить", "Принимать внутривенно"]

def message_maker(to_do, ingrs, the_way_to):
	#to_do_num = random.randint(len(to_do))
	#ingrs_num = random.randint(len(ingrs))
	#the_way_to_num = random.randint(len(the_way_to)
	message = "{0} {1} грамм {2}; {3} {4} грамм {5}; {6} {7} раз в день".format(to_do[0],
	 str(random.randint(1, 10)), ingrs[random.randint(0, len(ingrs)-1)], to_do[1], str(random.randint(1, 100)), 
	  ingrs[random.randint(0, len(ingrs) - 1)], the_way_to[random.randint(0, len(the_way_to) - 1)], str(random.randint(1,30)))
	return message

print(message_maker(to_do, ingrs, the_way_to))
