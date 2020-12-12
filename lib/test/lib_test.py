def test_trivial_assert():
    assert 1 == 1


if __name__ == "__main__":
    import pytest

    raise SystemExit(pytest.main([__file__]))