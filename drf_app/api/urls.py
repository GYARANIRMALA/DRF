from rest_framework.routers import DefaultRouter

from django.urls import include, path
# from drf_app.api.views import movie_list, movie_detail
from drf_app.api.views import (ReviewCreate, ReviewDetail, ReviewList,
                               StreamPlatformVS, UserReview, WatchListAV,
                               WatchListDetailAV, WatchListGV)

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchListDetailAV.as_view(), name='movie-detail'),
    path('list2/', WatchListGV.as_view(), name='movie-list'),

    path('', include(router.urls)),

    # path('stream/', StreamPlatformListAV.as_view(), name='stream-list'),
    # path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='stream-detail'),
    
    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),

    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),

    # path('reviews/<str:username>/', UserReview.as_view(), name='user-review-detail'),   # Here we have to provide the exact URL
    path('reviews/', UserReview.as_view(), name='user-review-detail'),         # It will take the query_params from views only

]