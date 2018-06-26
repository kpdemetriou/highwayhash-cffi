from ._highwayhash import ffi as __ffi, lib as __lib
from struct import pack


def __process_in(key, data):
    if not isinstance(key, bytes):
        raise TypeError("'key' must be of type 'bytes'")

    if not isinstance(data, bytes):
        raise TypeError("'data' must be of type 'bytes'")

    if len(key) != 32:
        raise ValueError("'key' must be of length '32'")

    return key, data


def __compute_highwayhash_64(key, data):
    key_ptr = __ffi.cast("uint64_t[4]", __ffi.new("char[32]", key))

    unpacked_result = __lib.HighwayHash64(data, len(data), key_ptr)
    return pack("Q", unpacked_result)


def __compute_highwayhash_128(key, data):
    key_ptr = __ffi.cast("uint64_t[4]", __ffi.new("char[32]", key))
    buffer = __ffi.new("uint64_t[2]")

    __lib.HighwayHash128(data, len(data), key_ptr, buffer)
    return bytes(__ffi.buffer(buffer, 16))


def __compute_highwayhash_256(key, data):
    key_ptr = __ffi.cast("uint64_t[4]", __ffi.new("char[32]", key))
    buffer = __ffi.new("uint64_t[5]")  # Intentional

    __lib.HighwayHash256(data, len(data), key_ptr, buffer)
    return bytes(__ffi.buffer(buffer, 32))


def highwayhash_64(key, data):
    key, data = __process_in(key, data)
    return __compute_highwayhash_64(key, data)


def highwayhash_128(key, data):
    key, data = __process_in(key, data)
    return __compute_highwayhash_128(key, data)


def highwayhash_256(key, data):
    key, data = __process_in(key, data)
    return __compute_highwayhash_256(key, data)
