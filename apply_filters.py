from typing import List

from PIL import Image


class NFTImage:

    _RESULT_SIZE = 300

    def __init__(self, path: str):
        self._path = path
        with Image.open(path) as original:
            self._original = original
            self._result = self._original.copy()

    def convert_to_bw(self):
        self._result = self._result.convert('L')
        return self

    def resize(self):
        size = self._RESULT_SIZE, self._RESULT_SIZE
        self._result.thumbnail(size, Image.ANTIALIAS)
        return self

    def flip(self):
        self._result = self._result.transpose(Image.FLIP_LEFT_RIGHT)
        return self

    def save(self):
        self._result.save(f"result_{self._path}")

    @property
    def result(self):
        return self._result


class NFTBuilder:

    BW_TRANS = "bw"
    FL_TRANS = "fl"
    RES_TRANS = "res"

    def __init__(self, nfts: List[List[NFTImage]]):
        self._nfts = nfts

    def build(self) -> Image:
        border_size = 10
        n = len(self._nfts)
        nft_size = self._nfts[0][0].result.size
        width, height = tuple([x * len(self._nfts) + 3 * border_size for x in nft_size])
        result = Image.new('RGB', (width, height))
        for r, row in enumerate(self._nfts):
            y_pos = int(r * (height / n) + border_size)
            for c, nft in enumerate(row):
                x_pos = int(c*(width/n) + border_size)
                result.paste(nft.result, (x_pos, y_pos))
        return result

    def transform(self, trans_str: List[List[str]]):
        for r, row in enumerate(self._nfts):
            for c, nft in enumerate(row):
                trans = trans_str[r][c].split(",")
                for t in trans:
                    if t == self.BW_TRANS:
                        nft.convert_to_bw()
                    elif t == self.FL_TRANS:
                        nft.flip()
                    elif t == self.RES_TRANS:
                        nft.resize()


def main():
    nft_paths = [["zombie.png"]*2]*2
    trans = [
        [NFTBuilder.RES_TRANS, f"{NFTBuilder.BW_TRANS},{NFTBuilder.FL_TRANS}"],
        [NFTBuilder.BW_TRANS, NFTBuilder.FL_TRANS]
    ]
    nfts = [[NFTImage(path).resize() for path in row] for row in nft_paths]
    builder = NFTBuilder(nfts)
    builder.transform(trans)
    result = builder.build()
    result.show()


if __name__ == '__main__':
    main()
