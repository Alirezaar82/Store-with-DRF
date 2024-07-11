from rest_framework.pagination import PageNumberPagination


class CustomProductPagination(PageNumberPagination):
    page_size = 9
    def get_page_size(self, request):
        return self.request.GET.get('page_size', self.page_size)