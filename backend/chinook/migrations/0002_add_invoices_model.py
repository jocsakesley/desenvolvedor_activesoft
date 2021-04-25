# Generated by Django 3.2 on 2021-04-25 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chinook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoices',
            fields=[
                ('invoiceid', models.AutoField(db_column='InvoiceId', primary_key=True, serialize=False)),
                ('customerid', models.IntegerField(db_column='CustomerId')),
                ('invoicedate', models.DateTimeField(db_column='InvoiceDate')),
                ('billingaddress', models.TextField(blank=True, db_column='BillingAddress', null=True)),
                ('billingcity', models.TextField(blank=True, db_column='BillingCity', null=True)),
                ('billingstate', models.TextField(blank=True, db_column='BillingState', null=True)),
                ('billingcountry', models.TextField(blank=True, db_column='BillingCountry', null=True)),
                ('billingpostalcode', models.TextField(blank=True, db_column='BillingPostalCode', null=True)),
                ('total', models.TextField(db_column='Total')),
            ],
            options={
                'db_table': 'invoices',
                'managed': False,
            },
        ),
    ]