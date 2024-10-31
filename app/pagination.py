from rest_framework.pagination import CursorPagination, PageNumberPagination
from rest_framework.response import Response



class FoodPagination(CursorPagination):
    ordering = '-pk'
    page_size = 2

class FoodTypePagination(CursorPagination):
    ordering = '-pk'
    page_size = 2

class CommentPagination(CursorPagination):
    ordering = '-pk'
    page_size = 2

class CustomPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })

