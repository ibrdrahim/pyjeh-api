from model.SampleModel import SampleModel
from library.logging.Log import logger

class SampleController():

    def __init__(self):
        pass

    def news(self):        
        try:
            sample_model = SampleModel()

            return sample_model.all_news(), None
        except Exception as er:
			logger(str(er))
			return None, str(er)

    def get_news(self, perpage, page):        
        try:
            sample_model = SampleModel()

            return sample_model.get_news_paginate(perpage, page), None
        except Exception as er:
			logger(str(er))
			return None, str(er)

    def get_news_detail(self, id):        
        try:
            sample_model = SampleModel()

            return sample_model.get_news_by_id(id), None
        except Exception as er:
			logger(str(er))
			return None, str(er)

    def get_news_detail_comment(self, slug):        
        try:
            sample_model = SampleModel()

            row_data = sample_model.get_news_by_slug(slug)
            row_data['comment'] = sample_model.get_comment_by_news(row_data['id'])

            return row_data, None
        except Exception as er:
			logger(str(er))
			return None, str(er)

    def get_news_comment(self, perpage, page):  
        data = []

        try:
            sample_model = SampleModel()

            row_data = sample_model.get_news_paginate(perpage, page)

            items = []
            try:
                items = row_data['items']
            except Exception as er:
                logger(str(er))
            
            for row in items:
                row['comment'] = sample_model.get_comment_by_news(row['id'])
                data.append(row)

            row_data['items'] = data

            return row_data, None
        except Exception as er:
			logger(str(er))
			return None, str(er)

    def get_news_likes(self, limit):        
        try:
            sample_model = SampleModel()

            return sample_model.get_news_mostlike(limit), None
        except Exception as er:
			logger(str(er))
			return None, str(er)

    def get_news_viwes(self, limit):        
        try:
            sample_model = SampleModel()

            return sample_model.get_news_mostview(limit), None
        except Exception as er:
			logger(str(er))
			return None, str(er)

    def get_news_most_comment(self, limit):        
        try:
            sample_model = SampleModel()

            return sample_model.get_news_mostcomment(limit), None
        except Exception as er:
			logger(str(er))
			return None, str(er)

    def get_news_by_id(self, id):        
        try:
            sample_model = SampleModel()

            return sample_model.delete_news_id(id), 'Success'
        except Exception as er:
			logger(str(er))
			return None, str(er)

    def get_comment_by_id(self, id):        
        try:
            sample_model = SampleModel()

            return sample_model.delete_comment_id(id), 'Success'
        except Exception as er:
			logger(str(er))
			return None, str(er)

    def add_news(self, params): 
        field = []
        value = []
        try:
            sample_model = SampleModel()

            for item in params:
                if params.get(item):
                    field.append(item)
                    value.append(params.get(item))

            return sample_model.add_news(field, value), 'Success'
        except Exception as er:
			logger(str(er))
			return None, str(er)

    def add_comment_news(self, params): 
        field = []
        value = []
        try:
            sample_model = SampleModel()

            for item in params:
                if params.get(item):
                    field.append(item)
                    value.append(params.get(item))

            return sample_model.add_comment(field, value), 'Success'
        except Exception as er:
			logger(str(er))
			return None, str(er)

    def update_comment_news(self, id, params): 
        try:
            sample_model = SampleModel()

            return sample_model.update_comment(id, params), 'Success'
        except Exception as er:
			logger(str(er))
			return None, str(er)

if __name__ == '__main__':
	SampleController()