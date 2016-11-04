import sys
from django.test import TestCase
# from django.db.models import TempChart

from chartit import PivotDataPool, DataPool, Chart, PivotChart
# Create your tests here.
from temp_app.models import TempChart
from utils import assertOptionDictsEqual

TestCase.assertOptionDictsEqual = assertOptionDictsEqual


class GoodChartOptionsTests(TestCase):


    def setUp(self):
        series_input = \
        [{'options': {
		'source':TempChart.objects.all()},
		'terms':  [
		'city_name',
		'temperature',
		'created_date' ]},
		{'options': {
		'source':TempChart.objects.all()},
		'terms': [
		{'city_name_dar': 'city_name'},
		'dar_temperature']}]

        self.ds = DataPool(series_input)

    def test_all_terms(self):
        so_input = [{
            'options': {
                'type': 'column'
            },
            'terms': {
                'city_name': [
                    'temperature', {
                        'created_date': {
                            'type': 'area',
                            'xAxis': 1
                        }
                    }
                ],
                'city_name_dar': ['dar_temperature']
            }
        }]
        so_cleaned = {
            'temperature': {
                '_x_axis_term': 'city_name',
                'type': 'column'
            },
            'city_name': {
                '_x_axis_term': 'city_name',
                'type': 'area',
                'xAxis': 1
            },
         
        }
        self.assertOptionDictsEqual(clean_cso(so_input, self.ds),
                                    so_cleaned)