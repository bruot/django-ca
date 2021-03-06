# Generated by Django 2.2.1 on 2019-05-18 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_ca', '0014_auto_20190518_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='revoked_reason',
            field=models.CharField(blank=True, choices=[('aa_compromise', 'Attribute Authority compromised'), ('affiliation_changed', 'Affiliation changed'), ('ca_compromise', 'CA compromised'), ('certificate_hold', 'On Hold'), ('cessation_of_operation', 'Cessation of operation'), ('key_compromise', 'Key compromised'), ('privilege_withdrawn', 'Privilege withdrawn'), ('remove_from_crl', 'Removed from CRL'), ('superseded', 'Superseded'), ('unspecified', 'Unspecified')], max_length=32, null=True, verbose_name='Reason for revokation'),
        ),
        migrations.AlterField(
            model_name='certificateauthority',
            name='revoked_reason',
            field=models.CharField(blank=True, choices=[('aa_compromise', 'Attribute Authority compromised'), ('affiliation_changed', 'Affiliation changed'), ('ca_compromise', 'CA compromised'), ('certificate_hold', 'On Hold'), ('cessation_of_operation', 'Cessation of operation'), ('key_compromise', 'Key compromised'), ('privilege_withdrawn', 'Privilege withdrawn'), ('remove_from_crl', 'Removed from CRL'), ('superseded', 'Superseded'), ('unspecified', 'Unspecified')], max_length=32, null=True, verbose_name='Reason for revokation'),
        ),
    ]
