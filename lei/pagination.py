from rest_framework import pagination


class NewsPageNumberPagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = 'count'
