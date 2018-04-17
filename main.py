from bottle import route, request, abort, run
from ConfigParser import ConfigParser
from controller.IsmayaController import IsmayaController
from helper.Helper import Helper
from library.logging.Log import logger
import dictionary

@route('/')
def index():
    abort(401, 'Sorry, access denied.')

@route('/banner')
def banner():
    key = dictionary.get('apikey')

    if request.get_header('apikey') in key:
        row_data = IsmayaController().get_banner()

        try:
            return Helper().raw(row_data)
        except Exception as er:
            logger(str(er))
            abort(500, "Internal Server Error.")
    else:
        abort(401, 'Sorry, access denied.')

@route('/celebrate')
def celebrate():
    key = dictionary.get('apikey')

    if request.get_header('apikey') in key:
        row_data = IsmayaController().get_celebrate(request.query.perpage)

        try:
            return Helper().raw(row_data)
        except Exception as er:
            logger(str(er))
            abort(500, "Internal Server Error.")
    else:
        abort(401, 'Sorry, access denied.')

@route('/whatson')
def whatson():
    key = dictionary.get('apikey')

    if request.get_header('apikey') in key:
        row_data = IsmayaController().get_whatson()

        try:
            return Helper().raw(row_data)
        except Exception as er:
            logger(str(er))
            abort(500, "Internal Server Error.")
    else:
        abort(401, 'Sorry, access denied.')

@route('/whatson/promo')
def brand_promo():
    key = dictionary.get('apikey')

    if request.get_header('apikey') in key:
        row_data = IsmayaController().get_promo_brand()

        try:
            return Helper().raw(row_data)
        except Exception as er:
            logger(str(er))
            abort(500, "Internal Server Error.")
    else:
        abort(401, 'Sorry, access denied.')

@route('/whatson/event')
def brand_event():
    key = dictionary.get('apikey')

    if request.get_header('apikey') in key:
        row_data = IsmayaController().get_event_brand()

        try:
            return Helper().raw(row_data)
        except Exception as er:
            logger(str(er))
            abort(500, "Internal Server Error.")
    else:
        abort(401, 'Sorry, access denied.')

@route('/news')
def news():
    key = dictionary.get('apikey')

    if request.get_header('apikey') in key:
        perpage = 6
        if request.query.perpage:
            perpage = request.query.perpage

        page = 1
        if request.query.page:
            page = request.query.page

        row_data = IsmayaController().get_news(int(perpage), int(page))

        try:
            return Helper().raw(row_data)
        except Exception as er:
            logger(str(er))
            abort(500, "Internal Server Error.")
    else:
        abort(401, 'Sorry, access denied.')

@route('/news/tv')
def tv():
    key = dictionary.get('apikey')

    if request.get_header('apikey') in key:
        perpage = 6
        if request.query.perpage:
            perpage = request.query.perpage

        page = 1
        if request.query.page:
            page = request.query.page

        row_data = IsmayaController().get_tv(int(perpage), int(page))

        try:
            return Helper().raw(row_data)
        except Exception as er:
            logger(str(er))
            abort(500, "Internal Server Error.")
    else:
        abort(401, 'Sorry, access denied.')

if __name__ == "__main__":
    cfg = ConfigParser()
    cfg.read('config/api.conf') 

    run(host=cfg.get('app','host'), port=int(cfg.get('app','port')), reloader=False)