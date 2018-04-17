from core.db.MySqlORM import Select
from library.logging.Log import logger

class SampleModel():

	def __init__(self):
		pass

	def all_news(self):
		query = Select('news')
		query.fetchall()

		return query.get()
	
	def get_news_paginate(self, perpage = 3, page = 1):
		query = Select('news')
		query.order_by(['created_at','desc'])
		
		return query.paginate(perpage, page)

	def get_news_by_slug(self, slug):
		query = Select('news')
		query.where('slug', slug)
		query.fetchone()

		return query.get()
	
	def get_news_by_id(self, id):
		query = Select('news')
		query.where('id', id)
		query.fetchone()

		return query.get()

	def get_comment_by_news(self, id_news):
		query = Select('comment')
		query.where('id_news', id_news)
		query.order_by(['created_at', 'desc'])
		query.fetchall()

		return query.get()

	def get_comment_by_news_paginate(self, id_news, perpage = 3, page = 1):
		query = Select('comment')
		query.where('id_news', id_news)
		query.order_by(['created_at','desc'])
		
		return query.paginate(perpage, page)

	def get_news_mostview(self, limit):
		query = Select('news')
		query.order_by(['viwes','desc'])
		query.limit(limit)
		query.fetchall()

		return query.get()

	def get_news_mostlike(self, limit):
		query = Select('news')
		query.order_by(['likes','desc'])
		query.limit(limit)
		query.fetchall()

		return query.get()

	def get_news_mostcomment(self, limit):
		query = Select('news', 'news.*, COUNT(comment.id) AS cnt')
		query.join('INNER', 'comment', 'news.id = comment.id_news')
		query.group_by('news.id', 'asc')
		query.order_by(['cnt','desc'])
		query.limit(limit)
		query.fetchall()

		return query.get()