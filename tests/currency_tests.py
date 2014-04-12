from nose.tools import *
from GERMANY.currency import Currency

def test_dollars():
    dollars = Currency('dollars')
    assert_equal(dollars.currency_type, 'dollars')

def test_euros():
    euros = Currency('euros')
    assert_equal(euros.currency_type, 'euros')
