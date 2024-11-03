from django.shortcuts import redirect


class SearchMixin:
    """
    This mixin makes modal search work on every view which inherits it.
    """
    def get(self, *args, **kwargs):
        if self.request.GET.get('q'):
            return redirect(f'/category/?q={self.request.GET.get('q')}')
        return super().get(*args, **kwargs)
