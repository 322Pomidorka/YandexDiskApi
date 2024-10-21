from django import forms


class PublicKeyForm(forms.Form):
    class Filter:
        ALL = ('all', "Все")
        ARCHIVE = ('archive', "Архивы")
        DOCUMENT = ('document', "Документы")
        IMAGE = ('image', "Изображения")
        EXECUTABLE = ('executable', "Исполняемые файлы")
        MEDIA = ('media', "Медиа файлы")

        choices = [ALL, ARCHIVE, DOCUMENT, IMAGE, EXECUTABLE, MEDIA]

    public_key = forms.CharField(label="Публичная ссылка", max_length=100)
    filter = forms.ChoiceField(label='Фильтр', choices=Filter.choices)