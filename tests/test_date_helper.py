from dateutil import parser
from pydelhi.date_helper import get_month

def test_date():
    dt = parser.parse('2021-01-01')
    month = get_month(dt)
    assert month == 'January'
