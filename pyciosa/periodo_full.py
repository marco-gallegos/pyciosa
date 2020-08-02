"""
@Author Marco A. Gallegos
@Date 2020/08/01
@Description
    Este modulo define metodos utiles para el manejo de periodos completos en formato : YYYYMMDD -> 20200131
"""
import datetime
import re

import numpy as np
import pendulum

regex_periodo_vicioso_completo = r"([0-9]{4}?((0[1-9])|(1[0-2]))((0[1-9])|((1|2)[0-9])|(3[0-1]))){1}"

quarters = [3, 6, 9, 12]


def is_valid(periodo: str) -> bool:
    """
    Determina si un periodo pasado por parametro tiene el formato YYYYMM -> 202001
    y concuerda con una representacion valida de fecha es decir que no se algo
    como 202020 adicionalmente si el parametro full es especificado como true hace los 
    mismo para un periodo completo

    :param periodo: periodo enformato YYYYMM o YYYYMMDD segun :full
    :type periodo: str
    :param full: bandera para determinar si el periodo es completo, defaults to False
    :type full: bool, optional
    :return: bool que determina si el periodo es valido o no
    :rtype: bool
    """
    result = True if re.fullmatch(pattern=regex_periodo_vicioso_completo ,string=periodo) else False
    
    # si tiene el formato valido validamos que se una fecha valida para el caso de fechas como 
    # febrero que puede pasar a la regex el periodo 20200231 pero no es valido
    result2 = False
    if result:
        try:
            date = pendulum.datetime(year=int(periodo[:4]), month=int(periodo[4:6]), day=int(periodo[6:8]))
            result2 = True
        except:
            result2 = False
    result = (result and result2)

    return result


def explode(periodo:str)-> (int, int, int):
    """Recibe el periodo como string y regresa estos datos (dia, mes y año)separados como enteros"""
    if is_valid(periodo):
        if isinstance(periodo, str):
            year = int(periodo[:4])
            month = int(periodo[4:6])
            day = int(periodo[6:8])
            return year, month, day
        elif isinstance(periodo, datetime.date):
            year    = periodo.year
            month   = periodo.month
            day   = periodo.day
            return year, month, day
        else:
            return None, None, None
    else:
            return None, None, None


def split(periodo:str, full:bool=False)-> (int, int, int):
    """Recibe el periodo como string y regresa estos datos (mes y año) separados como enteros"""
    if is_valid(periodo):
        if isinstance(periodo, str):
            year = int(periodo[:4])
            month = int(periodo[4:6])
            day = int(periodo[6:8])
            return year, month, day
        elif isinstance(periodo, datetime.date):
            year    = periodo.year
            month   = periodo.month
            day   = periodo.day
            return year, month, day
        else:
            return None, None, None
    else:
            return None, None, None

