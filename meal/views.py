import os
import random
import string

import pyexcel

from django.conf import settings
from django.views.generic.edit import FormView

from .forms import ExcelUploadForm
from .models import Meal


class ExcelUploadFormView(FormView):
    form_class = ExcelUploadForm
    template_name = 'excel/upload.html'
    success_url = './'

    def form_valid(self, form):
        file = self.request.FILES['file']
        file_name = '{0}.xlsx'.format(''.join(random.choice(string.ascii_lowercase) for _ in range(10)))
        file_path = os.path.join(os.path.join(settings.BASE_DIR, 'swp'), file_name)

        with open(file_path, 'wb') as f:

            for chunk in file.chunks():
                f.write(chunk)

        records = pyexcel.iget_records(file_name=file_path)

        for record in records:
            data = Meal(
                date=record['date'],
                time=record['time'],
                menu=record['menu']
            )

            data.save()

        os.remove(file_path)

        return super().form_valid(form)
