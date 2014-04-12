from nose.tools import *
from GERMANY.germany import Currency

def test_dollars():
    dollars = Currency('dollars')
    assert_equal(dollars.currency_type, 'dollars')
