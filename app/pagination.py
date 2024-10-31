from rest_framework.pagination import LimitOffsetPagination



class FoodPagination(LimitOffsetPagination):
    default_limit = 2


class FoodTypePagination(LimitOffsetPagination):
    default_limit = 2

class CommentPagination(LimitOffsetPagination):
    default_limit = 2



