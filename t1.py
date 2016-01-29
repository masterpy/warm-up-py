# coding=utf-8
import pprint
bob = ['Bob Smith', 42, 30000, 'software']
sue = ['Sue Jones', 45, 40000, 'hardware']
print(bob[0].split()[-1])
people = [bob, sue]
for person in people:
    print(person)
print(people[1][0])

pays = map((lambda x: x[2]), people)
print(pays)
print(list(pays))
print(sum(person[2] for person in people))


NAME, AGE, PAY = range(3)
print(bob[NAME])

print('=' * 50)
bob = {'pay': 30000, 'job': 'dev', 'age': 42, 'name': 'Bob Smith'}
sue = {'job': 'hdw', 'pay': 40000, 'age': 45, 'name': 'Sue Jones'}
people = [bob, sue]

print(list(map((lambda x: x['name']), people)))

print(sum(person['pay'] for person in people))

t1 = [rec['name'] for rec in people if rec['age'] >= 45]
print(t1)

t2 = [(rec['age'] ** 2 if rec['age'] >= 45 else rec['age']) for rec in people]
print(t2)

t3 = (rec['name'] for rec in people if rec['age'] >= 45)
print(next(t3))

t4 = ((rec['age'] ** 2 if rec['age'] >= 45 else rec['age']) for rec in people)
print(t4.__next__())

for person in people:
    print(person['pay'])


pprint.pprint(people)
