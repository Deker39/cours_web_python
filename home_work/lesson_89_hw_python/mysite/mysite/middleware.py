from django.shortcuts import redirect


class SearchMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == "POST":
            search_slug = request.POST.get('searchInput')
            return redirect('search prod', search_slug=search_slug)

        response = self.get_response(request)
        return response
