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

    def get_news(self, params):        
        try:
            sample_model = SampleModel()

            return sample_model.get_news_paginate(int(params.perpage), int(params.page)), None
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

    def get_news_comment(self, params):  
        data = []

        try:
            sample_model = SampleModel()

            row_data = sample_model.get_news_paginate(int(params.perpage), int(params.page))

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

    def get_news_likes(self, params):        
        try:
            sample_model = SampleModel()

            return sample_model.get_news_mostlike(int(params.limit)), None
        except Exception as er:
			logger(str(er))
			return None, str(er)

    def get_news_viwes(self, params):        
        try:
            sample_model = SampleModel()

            return sample_model.get_news_mostview(int(params.limit)), None
        except Exception as er:
			logger(str(er))
			return None, str(er)

    def get_news_most_comment(self, params):        
        try:
            sample_model = SampleModel()

            return sample_model.get_news_mostcomment(int(params.limit)), None
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
        try:
            sample_model = SampleModel()

            return sample_model.add_news(params), 'Success'
        except Exception as er:
			logger(str(er))
			return None, str(er)

    def add_comment_news(self, params):
        try:
            sample_model = SampleModel()

            return sample_model.add_comment(params), 'Success'
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