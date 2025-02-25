from django.urls import reverse


class TestModel:
    namespace: str

    def get_view_name(self, view_name, args):
        return f"{self.namespace}-{view_name}"

    def get_url(self):
        return reverse(self.namespace)
