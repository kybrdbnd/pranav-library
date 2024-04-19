from pydelhi.hello import say_hello
from pydelhi.date_helper import get_month
from dateutil import parser


def test_hello():
    dt = parser.parse("2021-01-01")
    name = "Pranav"
    msg = say_hello(name, dt)
    month = get_month(dt)
    assert msg == f"Hello {name}!. Welcome to Pydelhi {month} talk"
