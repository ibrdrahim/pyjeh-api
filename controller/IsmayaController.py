from model.IsmayaModel import IsmayaModel
import json
from library.logging.Log import logger

class IsmayaController():

    def __init__(self):
        pass

    def get_banner(self):        
        try:
            ismaya_model = IsmayaModel()

            return ismaya_model.all_banner(), None
        except Exception as er:
			logger(str(er))
			return None, str(er)

    def get_celebrate(self, limit = 4):        
        try:
            ismaya_model = IsmayaModel()

            return ismaya_model.get_celebrate(limit)
        except Exception as er:
			logger(str(er))
			return None

    def get_whatson(self):        
        try:
            ismaya_model = IsmayaModel()

            return ismaya_model.get_whatson()
        except Exception as er:
			logger(str(er))
			return None

    def get_promo_brand(self):
        data = []
        
        try:
            ismaya_model = IsmayaModel()

            row_data = ismaya_model.get_promo()

            for row in row_data:
                row['brand'] = ismaya_model.get_brand_id(row['id_cafe'])
                data.append(row)

            return data
        except Exception as er:
			logger(str(er))
			return None
    
    def get_event_brand(self):
        data = []
        
        try:
            ismaya_model = IsmayaModel()

            row_data = ismaya_model.get_event()

            for row in row_data:
                row['brand'] = ismaya_model.get_brand_id(row['id_cafe'])
                data.append(row)

            return data
        except Exception as er:
			logger(str(er))
			return None

    def get_news(self, perpage, page):        
        try:
            ismaya_model = IsmayaModel()

            return ismaya_model.get_news_list(perpage, page)
        except Exception as er:
			logger(str(er))
			return None

    def get_tv(self, perpage, page):        
        try:
            ismaya_model = IsmayaModel()

            return ismaya_model.get_tv_list(perpage, page)
        except Exception as er:
			logger(str(er))
			return None

if __name__ == '__main__':
	IsmayaController()