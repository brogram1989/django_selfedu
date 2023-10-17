#https://www.youtube.com/watch?v=cFJqMXxVNsI&list=PLA0M1Bcd0w8wfmtElObQrBbZjY6XeA06U&index=1

from jinja2 import Template


# name= 'Dilshod'
# age = 33
#
# tm = Template("Assalomu alaykum {{n}}, sizning yoshingiz {{a}}")
#
# msg = tm.render(n=name, a =age)
# print(msg)


#for operatori

# shaharlar = [
#     {'id':1, 'city':'Toshkent'},
#     {'id':4, 'city':'Samarqand'},
#     {'id':7, 'city':'Jizzah'},
#     {'id':10, 'city':'Buxoro'},
#     {'id':11, 'city':'Xiva'}
# ]

# link = """<select name='cities'>
# {% for c in cities -%}
#     <option value = '{{c['id']}}'>{{c['city']}}</option>
#     {% endfor -%}
#     </select>    """
#
# tm = Template(link)
# msg = tm.render(cities = shaharlar)
# print(msg)

# tm = Template(link)
# msg = tm.render(cities = shaharlar)
# print(msg)


#if operatori

# link = """<select name='cities'>
# {% for c in cities -%}
# {% if c.id > 8 -%}
#     <option value = '{{c['id']}}'>{{c['city']}}</option>
#     {% elif c.city == 'Toshkent' -%}
#     <option> {{c['city']}} </option>
#     {% else -%}
#     {{c['city']}}
#     {% endif -%}
#     {% endfor -%}
#     </select>    """
#
# tm = Template(link)
# msg = tm.render(cities = shaharlar)
# print(msg)


#Django 3 для python (уроки)

#Jinja2 #3: Фильтры и макросы macro, call


# cars = [
#     {'model': 'spark', 'price' : 10000},
#     {'model': 'nexia3', 'price' : 12000},
#     {'model': 'cobalt', 'price' : 15000},
#     {'model': 'gentra', 'price' : 18000},
#     {'model': 'tracer', 'price' : 20000}
# ]
#
# tpl = "Umumiy avtomobillar soni {{cs | sum(attribute='price') }} "
# tm = Template(tpl)
# msg = tm.render(cs = cars)
# print(msg)
# tpl_max = "Eng qimmat avtoulov {{cs | max(attribute='price') }} "
# tm_max = Template(tpl_max)
# msg_max = tm_max.render(cs = cars)
# print(msg_max)
#
# digs = [1,2,3,4]
# tpl = "Umumiy sonlar yig`indisi {{cs | sum }} "
# tm = Template(tpl)
# msg = tm.render(cs = digs)
# print(msg)


#filtr bloki
persons = [
    {'name': 'Aziz', 'old': 18, 'vazni':70},
    {'name': 'Shokir', 'old': 48, 'vazni': 100},
    {'name': 'Temur', 'old': 28, 'vazni': 72},
    {'name': 'Sohib', 'old': 22, 'vazni': 68},
    {'name': 'sardor', 'old': 30, 'vazni': 75},
]


tpl = '''
{%- for u in users -%}
{% filter upper %} {{u.name}} {% endfilter %}
{% endfor -%}
'''

tm = Template(tpl)
msg = tm.render(users = persons)
print(msg)
