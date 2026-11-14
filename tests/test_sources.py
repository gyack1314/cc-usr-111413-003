"""既有来源接口及拒绝错误资料的测试。"""
import unittest,tempfile
from pathlib import Path
from common import read,money,number,release,latest
class CommonTests(unittest.TestCase):
    def test_precise_money_and_finite_measurement(self):
        self.assertEqual(money('0.1')+money('0.2'),money('0.3'))
        with self.assertRaises(ValueError):number(float('nan'))
        with self.assertRaises(ValueError):money(.1)
    def test_release_reuse_and_corruption(self):
        with tempfile.TemporaryDirectory() as folder:
            key=release(folder,{'x':1});self.assertEqual(release(folder,{'x':1}),key)
            Path(folder,key+'.json').write_text('{"x":2}')
            with self.assertRaises(ValueError):release(folder,{'x':1})

from frame import totals
from survey import sample,direct
from city_reference import city_reference
class DomainTests(unittest.TestCase):
    def test_frame_includes_unsampled_town(self):
        d=read();self.assertEqual(len(totals(d)),6);self.assertNotIn('t5',direct(d))
        self.assertEqual(sample(d)[0]['weight'],4)
    def test_external_reference_not_exact(self):
        d=read();self.assertFalse(city_reference(d)['exact']);d['city_reference']['variance']=-1
        with self.assertRaises(ValueError):city_reference(d)
        d=read();d['sample'].append(d['sample'][0])
        with self.assertRaises(ValueError):sample(d)
