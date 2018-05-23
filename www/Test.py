# -*- coding:utf-8 -*-
from models import User,Blog,Comment
import orm
import asyncio


loop = asyncio.get_event_loop()


@asyncio.coroutine
def test():
    yield from orm.create_pool(loop,user='root',password='1234',db='awesome')
    user = User(name='Zack',email='Zack@zack.com',passwd='1234',image='about:blank')
    yield from user.save()


loop.run_until_complete(test())
