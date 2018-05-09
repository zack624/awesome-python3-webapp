from orm import Model,StringField,IntegerField,create_pool
import asyncio


class User(Model):
    __table__ = 'users'
    id = IntegerField(primary_key=True)
    name = StringField()


@asyncio.coroutine
def main(loop):
    yield from create_pool(loop, **database)
    user = User()
    user.id = 123
    user.name = 'Test'
    yield from user.save()
    return user.name


loop = asyncio.get_event_loop()
database = {
    'host': 'localhost',
    'user': 'root',
    'password': '1234',
    'db': 'python_test'
}

task = asyncio.ensure_future(main(loop))

res = loop.run_until_complete(task)
print(res)