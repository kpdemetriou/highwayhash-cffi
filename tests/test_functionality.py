import highwayhash


def test_64(case_key, case_data):
    highwayhash.highwayhash_64(case_key, case_data)


def test_128(case_key, case_data):
    highwayhash.highwayhash_128(case_key, case_data)


def test_256(case_key, case_data):
    highwayhash.highwayhash_256(case_key, case_data)
