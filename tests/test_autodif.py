import pytest
import autodif

def test_linearoots_result():
    assert autodif.linear_roots(2.0, -3.0) == 1.5

def test_linearroots_types():
    with pytest.raises(TypeError):
        autodif.linear_roots("ocean", 6.0)

def test_linearroots_zerocoeff():
    with pytest.raises(ValueError):
        autodif.linear_roots(a=0.0)
