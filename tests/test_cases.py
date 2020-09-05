import binascii
import highwayhash


def test_64(case_key, case_data, cases_highwayhash_64):
    for i, case in enumerate(cases_highwayhash_64):
        output = highwayhash.highwayhash_64(case_key, case_data[:i])
        hex_output = binascii.hexlify(output).decode("utf8")

        assert case == hex_output


def test_128(case_key, case_data, cases_highwayhash_128):
    for i, case in enumerate(cases_highwayhash_128):
        output = highwayhash.highwayhash_128(case_key, case_data[:i])
        hex_output = binascii.hexlify(output).decode("utf8")

        assert case == hex_output


def test_256(case_key, case_data, cases_highwayhash_256):
    for i, case in enumerate(cases_highwayhash_256):
        output = highwayhash.highwayhash_256(case_key, case_data[:i])
        hex_output = binascii.hexlify(output).decode("utf8")
        assert case == hex_output
