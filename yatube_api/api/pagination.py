from rest_framework.pagination import LimitOffsetPagination


class OptionalLimitOffsetPagination(LimitOffsetPagination):

    def paginate_queryset(self, queryset, request, view=None):
        if self.limit_query_param not in request.query_params:
            return None
        return super().paginate_queryset(queryset, request, view)
