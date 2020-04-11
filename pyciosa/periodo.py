"""
@author Marco A. Gallegos
@date 2020/03/10
@description
Este modulo define metodos utiles para el manejo de periodos en formato : YYYYMM -> 202001
"""
import datetime
import pendulum
import numpy as np
import re

regex_periodo_vicioso = r"([0-9]{4}?((0[1-9])|(1[0-2]))){1}"

def is_valid(periodo:str)-> bool:
    """Determina si un periodo pasado por parametro tiene el formato YYYYMM -> 202001 
    y concuerda con una representacion valida de fecha es decir que no se algo
    como 202020
    """
    result = True if re.fullmatch(pattern=regex_periodo_vicioso ,string=periodo) else False
    return result


def explode(periodo:str)-> (int, int):
    """Recibe el periodo como string y regresa estos datos separados como enteros"""
    if is_valid(periodo):
        if isinstance(periodo, str):
            year = int(periodo[:4])
            month = int(periodo[4:])
            return year, month
        elif isinstance(periodo, datetime.date):
            year    = periodo.year
            month   = periodo.month
        else:
            return None, None
    else:
            return None, None