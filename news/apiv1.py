from django.conf import settings
from pytz import timezone
from rest_framework import viewsets, routers
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action
from itbestnews.utilities import create_response
from .models import *

from django.core.exceptions import ObjectDoesNotExist


class ContentViewSet(viewsets.GenericViewSet, ObtainAuthToken):
    @action(detail=False, methods=['GET'])
    def get_category_list(self, request):
        """
               get:
               Get category List
           """
        dc = Category.objects.all().order_by("id")
        result_list = []
        for pr in dc:
            data = dict()
            data['id'] = pr.pk
            data['name'] = pr.name
            result_list.append(data)
        return create_response(True, None, 200, 100, None, result_list)

    @action(detail=False, methods=['GET'])
    def get_news_list(self, request):
        """
          get:
          Get News List
        """
        if 'page' in request.query_params:
            pg = request.query_params["page"]
        else:
            pg = 0
        page = int(pg) * 10

        if 'categoryId' in request.query_params:
            cat_id = request.query_params["categoryId"]
            list = News.objects.filter(category=cat_id).order_by("-date")[page:page + 10]
        else:
            list = News.objects.all().order_by("-date")[page:page + 10]

        result_list = []
        for nw in list:
            data = dict()
            data['id'] = nw.pk
            data['title'] = nw.title
            cat_list = nw.category.all()
            category_list = []
            for item in cat_list:
                data2 = dict()
                data2['id'] = item.pk
                data2['name'] = item.name
                category_list.append(data2)
            data['categories'] = category_list
            if nw.image:
                data['imageUrl'] = nw.image.url
            else:
                data['imageUrl'] = None
            data['visitCount'] = nw.visit_count
            data['date'] = nw.date
            result_list.append(data)
        return create_response(True, None, 200, 100, None, result_list)

    @action(detail=False, methods=['GET'])
    def get_news_details(self, request):
        """
          get:
          Get News Details
        """
        if 'newsId' in request.query_params:
            news_id = request.query_params["newsId"]
        else:
            return create_response(False, "newsId not exist !", 404, 102, None, None)

        try:
            nw = News.objects.get(pk=news_id)
        except ObjectDoesNotExist:
            return create_response(False, "news with this id not exist", 404, 101, None, None)

        data = dict()
        data['id'] = nw.pk
        data['title'] = nw.title
        cat_list = nw.category.all()
        category_list = []
        for item in cat_list:
            data2 = dict()
            data2['id'] = item.pk
            data2['name'] = item.name
            category_list.append(data2)
        data['categories'] = category_list
        data['description'] = nw.desc
        if nw.image:
            data['imageUrl'] = nw.image.url
        else:
            data['imageUrl'] = None
        data['visitCount'] = nw.visit_count
        data['date'] = nw.date
        return create_response(True, None, 200, 100, data, None)


router = routers.DefaultRouter()
router.register(r'content', ContentViewSet, 'content')
