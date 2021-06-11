import base64
import mimetypes

from typing.io import BinaryIO


def bytes_to_datauri(fp: BinaryIO, name: str) -> str:
    """Convert a file (specified by a path) into a data URI."""
    mime, _ = mimetypes.guess_type(name)
    fp.seek(0)
    data = fp.read()
    data64 = b"".join(base64.encodebytes(data).splitlines())
    return "data:%s;base64,%s" % (mime, data64.decode("utf-8"))
