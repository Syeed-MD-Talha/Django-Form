from django.urls import path
from . import views
urlpatterns = [
    path('',views.review.as_view(),name='add_rating'),
    path('thank-you',views.thank_you.as_view(),name='thank_you'),
    path('review-list',views.reviewList.as_view(),name='review_list'),
    path('review-list/favorite/',views.addFavorite.as_view(),name='add_favorite'),
    path('review-list/<int:id>',views.single_review.as_view(),name='single_review'),
]
