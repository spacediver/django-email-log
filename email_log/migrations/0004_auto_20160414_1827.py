# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_log', '0003_email_html_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='html_body',
            field=models.TextField(null=True, verbose_name='html body', blank=True),
        ),
    ]
