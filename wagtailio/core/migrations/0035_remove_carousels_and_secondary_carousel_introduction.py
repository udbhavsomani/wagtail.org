# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-12-01 14:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0034_add_body_field_to_home_page"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="homepagemaincarouselitem",
            name="call_to_action_internal_link",
        ),
        migrations.RemoveField(
            model_name="homepagemaincarouselitem",
            name="image",
        ),
        migrations.RemoveField(
            model_name="homepagemaincarouselitem",
            name="page",
        ),
        migrations.DeleteModel(
            name="HomePageMainCarouselItem",
        ),
        migrations.RemoveField(
            model_name="homepagesecondarycarouselitem",
            name="author_image",
        ),
        migrations.RemoveField(
            model_name="homepagesecondarycarouselitem",
            name="desktop_image",
        ),
        migrations.RemoveField(
            model_name="homepagesecondarycarouselitem",
            name="mobile_image",
        ),
        migrations.RemoveField(
            model_name="homepagesecondarycarouselitem",
            name="page",
        ),
        migrations.DeleteModel(
            name="HomePageSecondaryCarouselItem",
        ),
        migrations.RemoveField(
            model_name="homepage",
            name="secondary_carousel_introduction",
        ),
    ]
