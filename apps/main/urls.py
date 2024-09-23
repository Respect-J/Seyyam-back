from django.urls import path

from .views import ContactsListView, ProjectsListView, ServicesListView, BannersListView, MaintitleListView, \
    CollectionsListView

urlpatterns = [
    path("contact/", ContactsListView.as_view(), name="contact-get"),
    path("project/", ProjectsListView.as_view(), name="project-get"),
    path("service/", ServicesListView.as_view(), name="service-get"),
    path("banner/", BannersListView.as_view(), name="banner-get"),
    path("maintitle/", MaintitleListView.as_view(), name="main-get"),
    path("collection/", CollectionsListView.as_view(), name="collection-get"),
]
