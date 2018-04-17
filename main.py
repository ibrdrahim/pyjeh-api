from bottle import route, request, abort, run
from core.app.Handler import Format
from library.logging.Log import logger
import dictionary

from controller.SampleController import SampleController

@route('/')
def index():
    abort(401, 'Sorry, access denied.')

@route('/news')
def news():
    key = dictionary.get('apikey')

    if request.get_header('apikey') in key:
        row_data, msg = SampleController().news()

        try:
            return Format().build(row_data, msg)
        except Exception as er:
            logger(str(er))
            abort(500, "Internal Server Error.")
    else:
        abort(401, 'Sorry, access denied.')

@route('/news/pagging')
def news_pagging():
    key = dictionary.get('apikey')

    if request.get_header('apikey') in key:
        perpage = 6
        if request.query.perpage:
            perpage = request.query.perpage

        page = 1
        if request.query.page:
            page = request.query.page

        row_data, msg = SampleController().get_news(int(perpage), int(page))

        try:
            return Format().build(row_data, msg)
        except Exception as er:
            logger(str(er))
            abort(500, "Internal Server Error.")
    else:
        abort(401, 'Sorry, access denied.')

@route('/news/:id')
def news_id(id):
    key = dictionary.get('apikey')

    if request.get_header('apikey') in key:
        row_data, msg = SampleController().get_news_detail(id)

        try:
            return Format().build(row_data, msg)
        except Exception as er:
            logger(str(er))
            abort(500, "Internal Server Error.")
    else:
        abort(401, 'Sorry, access denied.')

@route('/news/detail/:slug')
def news_slug(slug):
    key = dictionary.get('apikey')

    if request.get_header('apikey') in key:
        row_data, msg = SampleController().get_news_detail_comment(slug)

        try:
            return Format().build(row_data, msg)
        except Exception as er:
            logger(str(er))
            abort(500, "Internal Server Error.")
    else:
        abort(401, 'Sorry, access denied.')

@route('/news/comment')
def news_comment():
    key = dictionary.get('apikey')

    if request.get_header('apikey') in key:
        perpage = 6
        if request.query.perpage:
            perpage = request.query.perpage

        page = 1
        if request.query.page:
            page = request.query.page

        row_data, msg = SampleController().get_news_comment(int(perpage), int(page))

        try:
            return Format().build(row_data, msg)
        except Exception as er:
            logger(str(er))
            abort(500, "Internal Server Error.")
    else:
        abort(401, 'Sorry, access denied.')

@route('/news/sort/:sort')
def news_sort(sort):
    key = dictionary.get('apikey')

    if request.get_header('apikey') in key:
        limit = 6
        if request.query.limit:
            limit = request.query.limit

        if sort == 'likes':
            row_data, msg = SampleController().get_news_likes(int(limit))
        elif sort == 'viwes':
            row_data, msg = SampleController().get_news_viwes(int(limit))
        else:
            row_data, msg = SampleController().get_news_most_comment(int(limit))

        try:
            return Format().build(row_data, msg)
        except Exception as er:
            logger(str(er))
            abort(500, "Internal Server Error.")
    else:
        abort(401, 'Sorry, access denied.')

@route('/news/delete/:id')
def news_delete(id):
    key = dictionary.get('apikey')

    if request.get_header('apikey') in key:
        row_data, msg = SampleController().get_news_by_id(id)

        try:
            return Format().build(row_data, msg)
        except Exception as er:
            logger(str(er))
            abort(500, "Internal Server Error.")
    else:
        abort(401, 'Sorry, access denied.')

@route('/comment/delete/:id')
def comment_delete(id):
    key = dictionary.get('apikey')

    if request.get_header('apikey') in key:
        row_data, msg = SampleController().get_comment_by_id(id)

        try:
            return Format().build(row_data, msg)
        except Exception as er:
            logger(str(er))
            abort(500, "Internal Server Error.")
    else:
        abort(401, 'Sorry, access denied.')

@route('/news/add')
def news_add():
    key = dictionary.get('apikey')

    if request.get_header('apikey') in key:
        params = {
            'author': request.query.author,
            'title': request.query.title,
            'slug': request.query.slug,
            'description': request.query.description,
            'img_news': request.query.image
        }

        row_data, msg = SampleController().add_news(params)

        try:
            return Format().build(row_data, msg)
        except Exception as er:
            logger(str(er))
            abort(500, "Internal Server Error.")
    else:
        abort(401, 'Sorry, access denied.')

@route('/comment/add/:id')
def comment_add(id):
    key = dictionary.get('apikey')

    if request.get_header('apikey') in key:
        params = {
            'id_news': id,
            'guest': request.query.guest,
            'email': request.query.email,
            'message': request.query.message
        }

        row_data, msg = SampleController().add_comment_news(params)

        try:
            return Format().build(row_data, msg)
        except Exception as er:
            logger(str(er))
            abort(500, "Internal Server Error.")
    else:
        abort(401, 'Sorry, access denied.')

if __name__ == "__main__":
    from ConfigParser import ConfigParser

    cfg = ConfigParser()
    cfg.read('config/pyjeh.conf') 

    run(host=cfg.get('app','host'), port=int(cfg.get('app','port')), reloader=False)