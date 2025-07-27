import pytest


def function_a():
    raise SystemExit(1)


def test_multiple_exits():
    with pytest.raises(SystemExit) as exc_info:
        function_a()
    assert exc_info.value.code == 1
    assert exc_info.type == SystemExit
