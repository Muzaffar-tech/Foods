from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

class FoodAnonThrottle(AnonRateThrottle):
    scope = 'food_anon_list'

class FoodUserThrottle(UserRateThrottle):
    scope = 'food_user_list'

class FoodTypeAnonThrottle(AnonRateThrottle):
    scope = 'food_type_anon_list'

class FoodTypeUserThrottle(UserRateThrottle):
    scope = 'food_type_user_list'

class CommentAnonThrottle(AnonRateThrottle):
    scope = 'comment_anon_list'

class CommentUserThrottle(UserRateThrottle):
    scope = 'comment_user_list'