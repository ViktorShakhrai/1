class Person:
    @classmethod
    def group(cls, n):
        # cls именно тот класс, который вызвал
        return [cls() for _ in range(n)]

    def __repr__(self):
        return 'Person'

class Worker(Person):
    def __repr__(self):
        return 'Worker'

print(Person.group(3))
# [Person, Person, Person]
print(Worker.group(2))
# [Worker, Worker]