

__author__ = 'Zack'



'url handlers'


from coroweb import get,post

from models import User,Comment,Blog,next_id 
import asyncio

@get('/')
@asyncio.coroutine
def index(request):
	users = yield from User.findAll()
	return {
		'__template__': 'test.html',
		'users': users
	}