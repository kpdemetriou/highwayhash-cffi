import pytest
import highwayhash


def test_invalid_key_type(case_data):
    with pytest.raises(TypeError):
        highwayhash.highwayhash_64("", case_data)


def test_invalid_data_type(case_key):
    with pytest.raises(TypeError):
        highwayhash.highwayhash_64(case_key, "")


def test_invalid_key_length(case_key, case_data):
    with pytest.raises(ValueError):
        highwayhash.highwayhash_64(case_key + b"\0", case_data)
