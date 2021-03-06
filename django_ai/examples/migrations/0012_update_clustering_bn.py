# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-10 12:14
from __future__ import unicode_literals

from django.db import migrations


def update_bn_forward(apps, schema_editor):
    """
    Updates the Clustering Example Bayesian Network Object.
    """
    BayesianNetwork = apps.get_model("bayesian_networks",
                                     "BayesianNetwork")
    bn = BayesianNetwork.objects.get(name="Clustering (Example)")
    bn.results_storage = "dmf:examples.UserInfo.cluster_1"
    bn.engine_meta_iterations = 15
    bn.counter_threshold = 10
    bn.threshold_actions = ":recalculate"
    bn.save()


def update_bn_backwards(apps, schema_editor):
    BayesianNetwork = apps.get_model("bayesian_networks",
                                     "BayesianNetwork")
    bn = BayesianNetwork.objects.get(name="Clustering (Example)")
    bn.results_storage = None,
    bn.engine_meta_iterations = 1
    bn.counter_threshold = None
    bn.threshold_actions = None
    bn.save()


class Migration(migrations.Migration):

    dependencies = [
        ('examples', '0011_add_rest_avg_times_visits'),
    ]

    operations = [
        migrations.RunPython(
            update_bn_forward, update_bn_backwards
        )
    ]
