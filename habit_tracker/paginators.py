from rest_framework.pagination import PageNumberPagination


class DefaultPaginator(PageNumberPagination):
    """
    Custom pagination
    """
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50
