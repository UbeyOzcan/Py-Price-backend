import polars as pl

class EDA:
    def __init__(self, data:pl.DataFrame, y:str, offset:str):
        self.data = data
        self.y = y
        self.offset = offset

    def response(self) -> float:

        y = self.data.select(pl.sum(self.y))
        w = self.data.select(pl.sum(self.offset))
        result = y/w

        return result.item()


    def univariate(self, var:[str]) -> dict:

        uni_dict = {}

        for i in var:
            uni_dict[i] = self.data.group_by(i).agg(pl.col(self.offset).sum(),
                                                    pl.col(self.y).sum())

        return uni_dict
