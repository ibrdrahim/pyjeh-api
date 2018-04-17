from helper.Handler import Handler
from model.IsmayaModel import IsmayaModel
import json
from library.logging.Log import logger

class IsmayaController():

    def __init__(self):
        pass

    def get_banner(self):        
        try:
            ismaya_model = IsmayaModel()

            row_data = ismaya_model.all_banner()
            
            json_data = json.dumps(row_data, cls=Handler)
            
            return json.loads(json_data)
        except Exception as er:
			logger(str(er))
			return None

    def get_celebrate(self, limit = 4):        
        try:
            ismaya_model = IsmayaModel()

            row_data = ismaya_model.get_celebrate(limit)
            
            json_data = json.dumps(row_data, cls=Handler)
            
            return json.loads(json_data)
        except Exception as er:
			logger(str(er))
			return None

    def get_whatson(self):        
        try:
            ismaya_model = IsmayaModel()

            row_data = ismaya_model.get_whatson()
            
            json_data = json.dumps(row_data, cls=Handler)
            
            return json.loads(json_data)
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

            json_data = json.dumps(data, cls=Handler)
            
            return json.loads(json_data)
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

            json_data = json.dumps(data, cls=Handler)
            
            return json.loads(json_data)
        except Exception as er:
			logger(str(er))
			return None

    def get_news(self, perpage, page):        
        try:
            ismaya_model = IsmayaModel()

            row_data = ismaya_model.get_news_list(perpage, page)

            json_data = json.dumps(row_data, cls=Handler)
            
            return json.loads(json_data)
        except Exception as er:
			logger(str(er))
			return None

    def get_tv(self, perpage, page):        
        try:
            ismaya_model = IsmayaModel()

            row_data = ismaya_model.get_tv_list(perpage, page)

            json_data = json.dumps(row_data, cls=Handler)
            
            return json.loads(json_data)
        except Exception as er:
			logger(str(er))
			return None

if __name__ == '__main__':
	IsmayaController()