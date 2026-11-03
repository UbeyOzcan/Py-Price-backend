import polars as pl

class EDA:
    def __init__(self, data:pl.DataFrame, res:str, w:str):
        self.data = data
        self.res = res
        self.w = w

    def response(self) -> float:

        y = self.data.select(pl.sum(self.res))
        w = self.data.select(pl.sum(self.w))
        result = y/w

        return result.item()

    def univariate(self, var:str) -> pl.DataFrame:
        return None
