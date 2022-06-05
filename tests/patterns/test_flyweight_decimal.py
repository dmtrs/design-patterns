from patterns.flyweight.decimal import Decimal

def test_is() -> None:
    assert Decimal(1) is Decimal(1.0) and not None
    assert Decimal(1) is not Decimal(0) and not None

def test_owner() -> None:
    # arrange
    one = Decimal(1)
    one_dot_zero = Decimal(1.0)

    owner = {'of': one, 'and': one_dot_zero}
    assert one is one_dot_zero
    assert owner['of'] is owner['and'] is one is one_dot_zero is not None

    del owner['and']
    assert owner['of'] is one is one_dot_zero is not None
    
    del one
    assert owner['of'] is one_dot_zero is not None