# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_log', '0002_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='html_body',
            field=models.TextField(default='', verbose_name='html body'),
            preserve_default=False,
        ),
    ]
