from rest_framework import pagination


class NewsPageNumberPagination(pagination.PageNumberPagination):
    page_size = 20
    page_size_query_param = 'count'
    max_page_size = 20
    page_query_param = 'p'
    last_page_strings = ('last', )


class RecursoPageNumberPagination(pagination.PageNumberPagination):
    page_size = 30
    page_size_query_param = 'count'
    max_page_size = 30
    page_query_param = 'p'
    last_page_strings = ('last', )


class CalendarioPageNumberPagination(pagination.PageNumberPagination):
    pass
    # page_size = 2
    # page_size_query_param = 'per_page'
    # max_page_size = 3
    # page_query_param = 'p'


