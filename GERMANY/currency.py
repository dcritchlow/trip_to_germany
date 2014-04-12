""" This module Optimizes a trip through Germany """
class Currency(object):
    """ This class holds the convert method for money types """
    def __init__(self, currency_type):
        super(Currency, self).__init__()
        self.currency_type = currency_type

    def convert_to_dollars(self):
        """ Convert from euro to dollar """
        return 'Currency is', self.currency_type

    def convert_to_euros(self):
        """ Convert from dollar to euro """
        return 'Currency is', self.currency_type
