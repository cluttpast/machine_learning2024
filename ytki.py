text=str
text='На шагающих утят быть похожими хотят, Быть похожими хотят не зря, не зря. Можно хвостик отряхнуть и пуститься в дальний путь И пуститься в дальний путь, крича "кря- кря". И природа хороша, и погода хороша, Нет, не зря поет душа, не зря, не зря. Даже толстый бегемот, неуклюжий бегемот От утят не отстает, кряхтит "кря- кря"'
text=text.lower()
#text=text.replace(',','')
#text=text.replace('!','')
#text=text.replace('"','')
#text=text.replace(',','')
#text=text.replace('.','')
def replace_symbols(string=text, symbols_list=[',','"','.','!',':','-'], replace_to='')->str:
    for symbol in symbols_list:
        string=string.replace(symbol,replace_to)
    return string
text=replace_symbols(text)
text=text.split(' ')
unique_list=list(set(text))
result={}
for word in unique_list:
    result[word]=text.count(word)
    eshkere=result.items()
    items=sorted(eshkere, key=lambda x:(-x[1], x[0]))
print(items)