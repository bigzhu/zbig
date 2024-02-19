from bigzhu_py.time import now_print
import re


def test_now_print(capfd):
    """Check that User instance has the particular properties."""
    now_print('BigZhu')
    out, err = capfd.readouterr()
    assert re.match(
        r'^(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2}:\d{2}) BigZhu$', out) is not None
    assert err == ''
