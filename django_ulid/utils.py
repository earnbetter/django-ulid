from ulid import ULID
import uuid

def parse(value: str | int | bytes | ULID) -> ULID:
    if isinstance(value, ULID):
        return value
    if isinstance(value, uuid.UUID):
            return ULID.from_uuid(value)
    if isinstance(value, str):
        len_value = len(value)
        if len_value == 36:
            return ULID.from_uuid(uuid.UUID(value))
        if len_value == 32:
            return ULID.from_hex(value)
        if len_value == 26:
            return ULID.from_str(value)
        raise ValueError('Cannot create ULID from string of length {}'.format(len_value))
    if isinstance(value, (int, float)):
        return ULID.from_int(int(value))
    if isinstance(value, (bytes, bytearray)):
        return ULID.from_bytes(value)
    if isinstance(value, memoryview):
        return ULID.from_bytes(value.tobytes())
    raise ValueError('Cannot create ULID from type {}'.format(value.__class__.__name__))
