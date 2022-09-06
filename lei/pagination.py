from rest_framework import pagination


class NewsPageNumberPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'count'
    max_page_size = 2
    page_query_param = 'p'


class CalendarioPageNumberPagination(pagination.PageNumberPagination):
    pass
    # page_size = 2
    # page_size_query_param = 'per_page'
    # max_page_size = 3
    # page_query_param = 'p'


