
# Dict can be written per line like this (using indentations)
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
}
 
# Dict can also be written in one line like this
mydict = {'name':'Kevin','year':1999,'likes':'music'}
print(mydict)

newdict = {'color':'', 'shape':'circle'}
print(newdict['color'])
print(newdict['shape'])
newdict['color']='yellow'
print(newdict['color'])
newdict['texture']='soft'
print(newdict)

newdict.pop('texture')
print(newdict)

gumshoedict = {'occupation':'detective', 'supervisor':'Edgeworth'}
gumshoedict.popitem()
print(gumshoedict)

gumshoedict['office','age']='police station','30-ish'
print(gumshoedict)

del gumshoedict[('office','age')]
print(gumshoedict)


# This will delete the entire dict:
# del gumshoedict

gumshoedict.clear()
print(gumshoedict)

# Converting other types of collection into dict won;t work
# pairlist = [1,'a',2,'b',3,'c',4,'d',5,'e',6,'f',7,'g']
# char_list = ['Luffy','Zoro','Nami','Usopp','Sanji','Chopper', 'Robin']
# pair_dict = dict(pairlist)
# print(pairlist)

pairdict = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g'}

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()
car["year"] = 2018
print(x)
print(type(x))
x = list(x)
print(x)
print(type(x))

gumshoedict.update({'name':'Dick'})
print(gumshoedict)
gumshoedict.update({'supervisor':'Edgeworth','occupation':'sleuth'})
print(gumshoedict)
gumshoedict.update({'supervisor':'von Karma'})
print(gumshoedict)

key = gumshoedict.keys()
print(key)
print(type(key))

nani = gumshoedict.items()
print(nani)
print(type(nani))
what = tuple(nani)
print(type(what))
print(what)

boss = gumshoedict.get('supervisor')
gf = gumshoedict.get('girlfriend')
print(boss)
print(gf)
print(type(gf))
poor_gumshoe = gumshoedict.get('occupation','supervisor')
print(poor_gumshoe)    



