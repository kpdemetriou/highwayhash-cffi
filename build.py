import os
from cffi import FFI

CFFI_CDEF = """
    uint64_t HighwayHash64(const uint8_t* data, size_t size, const uint64_t key[4]);
    void HighwayHash128(const uint8_t* data, size_t size, const uint64_t key[4], uint64_t hash[2]);
    void HighwayHash256(const uint8_t* data, size_t size, const uint64_t key[4], uint64_t hash[4]);
"""

source_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sources")

highwayhash_ffi = FFI()
highwayhash_ffi.cdef(CFFI_CDEF)

with open(os.path.join(source_directory, "highwayhash.c")) as highwayhash_source_file:
    highwayhash_ffi.set_source(
        "highwayhash._highwayhash", highwayhash_source_file.read(), include_dirs=[source_directory]
    )

if __name__ == "__main__":
    highwayhash_ffi.compile(verbose=True)
