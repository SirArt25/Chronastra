import sys
import streamlit as st
from functools import partial


# add strict strict_method to ensure that user can create strictly
class strict_method:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is not None:
            raise TypeError("This method cannot be called from instances")
        return partial(self.func, owner)
