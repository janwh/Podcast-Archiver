import unicodedata
import re


_slugify_re_1 = re.compile(r"[^\w\s\-\.]")
_slugify_re_2 = re.compile(r"[-\s]+")


def slugify(string):
    string = unicodedata.normalize("NFKD", string)
    string = string.encode("ascii", "ignore").decode("ascii")
    string = _slugify_re_1.sub("", string).strip()
    string = _slugify_re_2.sub("-", string)

    return string
