# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Annotations(models.Model):
    gene = models.TextField(db_column='#query_name', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    seed_eggnog_ortholog = models.TextField(db_column='seed_eggNOG_ortholog', blank=True, null=True)  # Field name made lowercase.
    seed_ortholog_evalue = models.FloatField(blank=True, null=True)
    seed_ortholog_score = models.FloatField(blank=True, null=True)
    predicted_gene_name = models.TextField(blank=True, null=True)
    go_terms = models.TextField(db_column='GO_terms', blank=True, null=True)  # Field name made lowercase.
    kegg_kos = models.TextField(db_column='KEGG_KOs', blank=True, null=True)  # Field name made lowercase.
    bigg_reactions = models.TextField(db_column='BiGG_reactions', blank=True, null=True)  # Field name made lowercase.
    annotation_tax_scope = models.TextField(db_column='Annotation_tax_scope', blank=True, null=True)  # Field name made lowercase.
    ogs = models.TextField(db_column='OGs', blank=True, null=True)  # Field name made lowercase.
    bestog_evalue_score = models.TextField(db_column='bestOG|evalue|score', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cog_cat = models.TextField(db_column='COG cat', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    eggnog_annot = models.TextField(db_column='eggNOG annot', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    search_terms = models.TextField(db_column='SearchTerm', blank=True, null=True)
    # id = models.IntegerField(blank=True, null=True)
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'Annotations'


class DownExp(models.Model):
    gene = models.TextField(blank=True, null=True)
    down_exp = models.TextField(db_column='Down', blank=True, null=True)  # Field name made lowercase.
    # id = models.IntegerField(blank=True, null=True)
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'Down_exp'


class UpExp(models.Model):
    gene = models.TextField(blank=True, null=True)
    up_exp = models.TextField(db_column='Up', blank=True, null=True)  # Field name made lowercase.
    # id = models.IntegerField(blank=True, null=True)
    id = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'Up_exp'