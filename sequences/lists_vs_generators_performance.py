import mem_profile
import random
import time

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

print(f'Memory (Before): {mem_profile.memory_usage_resource()}Mb')

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result





def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person

t1 = time.time()
people = people_list(1000000)
t2 = time.time()

#t1 = time.clock()
#people = people_generator(10**5)
#t2 = time.clock()


print(f'Memory (After): {mem_profile.memory_usage_resource()}Mb')
print(f'Took {t2 -t1} secs')
