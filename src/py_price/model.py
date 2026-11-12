from statsmodels.formula.api import smf
import statsmodels.api as sm
import polars as pl

class GLM:
    def __init__(self, data:pl.DataFrame, formula:str, exposure:str, family:class):

        self.data = data
        self.formula = formula
        self.exposure = exposure
        self.family = family

    def fit(self):
        model = smf.glm(
            formula = self.formula,
            data = self.data,
            family = self.family,
            exposure = self.data[self.exposure]).fit()

