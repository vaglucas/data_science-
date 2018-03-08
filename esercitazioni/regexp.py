import re
#re.I ignora maiuscoli e minuscoli
#re.M attiva la modalita multiriga e consente di utsar gli operatori ~ e $ per individuare rispettivamente l'inizio o la fine di una riga
#email il minimo serber a@a.a o a.a@a.c

r"\w[-\w\./*@\w[-\w/*(\.\w[-\w/*)+"

mo = re.match(r"\d+","067 Stars wuth a number")
mo.group()
print(mo)
print(re.match(r"\d+","Does not Stars wuth a number"))

#search
print(re.search(r"[a-z]+","0010010 Has at least one 010 letter 004505050",re.I))
print(re.search(r"[a-z]+","0010010 Has at least one 010 letter 004505050"))
print(re.findall(r"[a-z]+","0010010 Has at least one 010 letter 004505050"))
print(re.sub(r"[a-z ]+","[...]","0010010 has at least one 010 letter 004505050"))
