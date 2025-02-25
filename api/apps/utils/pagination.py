from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"

    def paginate_queryset(self, queryset, request, view=None):
        if request.query_params.get("_all", False) == "true":
            # Set page_size to the length of the queryset to return all results
            self.page_size = len(queryset) or 1
            # Remove page_size_query_param to use the default value
            self.page_size_query_param = None

        return super().paginate_queryset(queryset, request, view)
