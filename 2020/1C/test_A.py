from hypothesis import given, settings
from hypothesis.strategies import integers, text
from A import do_A


@settings(max_examples=5_000)
@given(integers(0, 1000), integers(0, 1000), text('NSEW', min_size=1, max_size=1000))
def test_A(X, Y, route):
    if X + Y == 0:
        return
    result = do_A(X, Y, route)
    assert result == 'IMPOSSIBLE' or result > 0


