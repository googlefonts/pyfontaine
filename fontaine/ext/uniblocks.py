import re
import unicodedata

from fontaine.ext.base import BaseExt
from fontaine.ext.update import get_from_cache

UNIDATA_URL = "http://www.unicode.org/Public/UNIDATA/Blocks.txt"


class Extension(BaseExt):
    extension_name = "uniblocks"
    description = "Uniblocks collections"

    @staticmethod
    def __getcharsets__():
        content = open(get_from_cache("Blocks.txt", UNIDATA_URL)).read()

        regex = re.compile(r"^([\da-f]+)..([\da-f]+);\s*(.*)$", re.I | re.U)
        for line in content.split("\n"):
            m = regex.match(line.strip())
            # 100000..10FFFF; Supplementary Private Use Area-B
            if not m:
                continue

            glyphlist = f"0x{m.group(1)}-0x{m.group(2)}"
            unicodes = Extension.convert_to_list_of_unicodes(glyphlist)
            yield type(
                "Charset",
                (object,),
                dict(
                    glyphs=unicodes,
                    common_name="Unicode Block %s" % m.group(3),
                    native_name="",
                    short_name=unicodedata.normalize(
                        "NFKD", "uni-{}".format(m.group(3).lower().replace(" ", "-"))
                    ),
                ),
            )
