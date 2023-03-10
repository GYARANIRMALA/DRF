from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination
# This Pagination Works with only view class or Generic View class itself

class WatchListPagination(PageNumberPagination):
    page_size = 7
    page_query_param = 'p'
    page_size_query_param = 'size'
    max_page_size = 10
    last_page_strings = 'end'


class WatchListLOPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10
    limit_query_param = 'limit'
    offset_query_param = 'start'

class WatchListCPagination(CursorPagination):
    page_size = 5
    ordering = 'created'
    cursor_query_param = 'record'