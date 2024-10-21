from django.core.cache import cache
from django.shortcuts import render

from disk_app.api import get_public_files
from disk_app.forms import PublicKeyForm
from disk_app.utils import get_file_type


def file_list_view(request):
    # Функция получения списка файлов с Яндекс.Диска

    form = PublicKeyForm(request.POST or None)
    files = []

    if request.method == "POST" and form.is_valid():
        public_key = form.cleaned_data["public_key"]
        file_type = form.cleaned_data["filter"]

        cache_key = f"yandex_disk_files_{public_key}"
        files = cache.get(cache_key)

        if files is None:
            data = get_public_files(public_key)
            if data and "_embedded" in data:
                files = data["_embedded"]["items"]
                cache.set(cache_key, files, timeout=500)

        if file_type != "all" and files:
            files = [file for file in files if file_type == get_file_type(file["name"])]

    return render(
        request,
        "disk_app/file_list.html",
        {"form": form, "files": files},
    )