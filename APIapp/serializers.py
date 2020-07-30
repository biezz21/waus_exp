from rest_framework import serializers
from .models import DownExp, UpExp, Annotations


class DownExpSerializer(serializers.ModelSerializer):
    class Meta:
        model = DownExp
        fields = ('gene', 'down_exp')


class UpExpSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpExp
        fields = ('gene', 'up_exp')

class AnnotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annotations
        fields = ('gene', 'seed_eggnog_ortholog', 'seed_ortholog_evalue', 'seed_ortholog_score', 'predicted_gene_name', 'go_terms', 
        'kegg_kos', 'bigg_reactions', 'annotation_tax_scope', 'ogs', 'bestog_evalue_score', 'cog_cat', 'eggnog_annot', 'search_terms', )