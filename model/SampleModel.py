from core.db.MySql import Select, Delete, Insert
from library.logging.Log import logger

class SampleModel():

	def __init__(self):
		pass

	def all_news(self):
		query = Select('dbsample')
		query.table('news')
		query.fetchall()

		return query.get()
	
	def get_news_paginate(self, perpage = 3, page = 1):
		query = Select('dbsample')
		query.table('news')
		query.order_by(['created_at','desc'])
		
		return query.paginate(perpage, page)

	def get_news_by_slug(self, slug):
		query = Select('dbsample')
		query.table('news')
		query.where('slug', slug)
		query.fetchone()

		return query.get()
	
	def get_news_by_id(self, id):
		query = Select('dbsample')
		query.table('news')
		query.where('id', id)
		query.fetchone()

		return query.get()

	def get_comment_by_news(self, id_news):
		query = Select('dbsample')
		query.table('comment')
		query.where('id_news', id_news)
		query.order_by(['created_at', 'desc'])
		query.fetchall()

		return query.get()

	def get_comment_by_news_paginate(self, id_news, perpage = 3, page = 1):
		query = Select('dbsample')
		query.table('comment')
		query.where('id_news', id_news)
		query.order_by(['created_at','desc'])
		
		return query.paginate(perpage, page)

	def get_news_mostview(self, limit):
		query = Select('dbsample')
		query.table('news')
		query.order_by(['viwes','desc'])
		query.limit(limit)
		query.fetchall()

		return query.get()

	def get_news_mostlike(self, limit):
		query = Select('dbsample')
		query.table('news')
		query.order_by(['likes','desc'])
		query.limit(limit)
		query.fetchall()

		return query.get()

	def get_news_mostcomment(self, limit):
		query = Select('dbsample')
		query.table('news', 'news.*, COUNT(comment.id) AS cnt')
		query.join('INNER', 'comment', 'news.id = comment.id_news')
		query.group_by('news.id', 'asc')
		query.order_by(['cnt','desc'])
		query.limit(limit)
		query.fetchall()

		return query.get()

	def delete_news_id(self, id):
		query = Delete('dbsample')
		query.table('news')
		query.where('id', id)

		return query.get()

	def delete_comment_id(self, id):
		query = Delete('dbsample')
		query.table('comment')
		query.where('id', id)

		return query.get()

	def add_comment(self, field, value):		
		query = Insert('dbsample')
		query.table('comment')
		query.fields(field)
		query.values(value)

		return query.get()

	def add_news(self, field, value):		
		query = Insert('dbsample')
		query.table('news')
		query.fields(field)
		query.values(value)

		return query.get()