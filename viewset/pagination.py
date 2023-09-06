from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'page'
    page_size_query_param = 'pagesize'


class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 3
