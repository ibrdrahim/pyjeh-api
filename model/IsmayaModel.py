from core.db.MySqlORM import Select
from library.logging.Log import logger

class IsmayaModel():

	def __init__(self):
		pass

	def all_banner(self):
		query = Select('is_ismaya_banners')
		query.fetchall()

		return query.get()

	def get_celebrate(self, limit):
		query = Select('is_ismaya_celebrate')
		query.order_by(['id', 'desc'])
		query.limit(limit)
		query.fetchall()

		return query.get()

	def get_whatson(self):
		query = Select('is_ismaya_whats_on_banner')
		query.fetchall()

		return query.get()

	def get_promo(self):
		query = Select('is_ismaya_cafe_event_promo')
		query.where('type', 'promo')
		query.fetchall()

		return query.get()

	def get_event(self):
		query = Select('is_ismaya_cafe_event_promo')
		query.where('type', 'event')
		query.fetchall()

		return query.get()

	def get_brand_id(self, id):
		query = Select('is_ismaya_cafe')
		query.where('id', id)
		query.fetchone()

		return query.get()

	def get_news_list(self, perpage = 6, page = 1):
		query = Select('is_ismaya_news')
		query.order_by(['created_at','desc'])
		
		return query.paginate(perpage, page)

	def get_tv_list(self, perpage = 6, page = 1):
		query = Select('is_ismaya_tv')
		query.order_by(['created_at','desc'])
		
		return query.paginate(perpage, page)