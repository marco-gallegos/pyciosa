"""
@Author Marco A. Gallegos
@Date 2020/03/10
@Description
Este modulo define metodos utiles para el manejo de periodos en formato : YYYYMM -> 202001
"""
import datetime
import re

import numpy as np
import pendulum

regex_periodo_vicioso = r"([0-9]{4}?((0[1-9])|(1[0-2]))){1}"

quarters = [3, 6, 9, 12]


def is_valid(periodo: str) -> bool:
    """Determina si un periodo pasado por parametro tiene el formato YYYYMM -> 202001
    y concuerda con una representacion valida de fecha es decir que no se algo
    como 202020
    """
    result = True if re.fullmatch(pattern=regex_periodo_vicioso ,string=periodo) else False
    return result


def explode(periodo:str)-> (int, int):
    """Recibe el periodo como string y regresa estos datos (mes y año)separados como enteros"""
    if is_valid(periodo):
        if isinstance(periodo, str):
            year = int(periodo[:4])
            month = int(periodo[4:])
            return year, month
        elif isinstance(periodo, datetime.date):
            year    = periodo.year
            month   = periodo.month
            return year, month
        else:
            return None, None
    else:
            return None, None


def split(periodo:str)-> (int, int):
    """Recibe el periodo como string y regresa estos datos (mes y año) separados como enteros"""
    if is_valid(periodo):
        if isinstance(periodo, str):
            year = int(periodo[:4])
            month = int(periodo[4:])
            return year, month
        elif isinstance(periodo, datetime.date):
            year    = periodo.year
            month   = periodo.month
            return year, month
        else:
            return None, None
    else:
            return None, None


def get_periodo(date: datetime.date =None)->str:
    """Regresar el periodo en formato YYYYMM -> 202001 correspondiente a el parametro date"""
    year = None
    month = None
    periodo = None
    if date is None:
        periodo = pendulum.now().format("YMM")
    elif isinstance(date, datetime.date):
        year = date.year
        month = date.month
        month = f"0{month}" if month < 10 else month
        periodo = f"{year}{month}"
    elif isinstance(date, pendulum.DateTime):
        periodo = date.format("YMM")
    
    if is_valid(periodo):
        return periodo
    else:
        return None


def interpolate(periodo:str, rango:int=13, invertir:bool=False)->list:
    """Regresar un list con los periodos interpolados entre el actual y 'rango'-1 meses anteriores
    es decir que contando el mes pasado como parametro tengamos 'rango' numero de periodos
    """
    year, month = explode(periodo)
    if year and month:
        contador = rango
        fecha = pendulum.datetime(year=year, month=month, day=1)
        periodos = list()
        while contador > 0:
            periodo = get_periodo(fecha)
            periodos.append(periodo)
            fecha = fecha.subtract(months=1)
            contador -= 1
        if invertir:
            return periodos[::-1]
        else:
            return periodos
    else:
        return None


def get_previous_quarter_periodo(periodo:str):
    """obtener el periodo de el 'quarter' anterior inmediato"""
    year, month = explode(periodo)

    if year and month:
        fecha = pendulum.datetime(year=year, month=month, day=1)
        encontrado = False
        quarters = np.array(quarters)
        while not encontrado:
            try:
                posicion = np.where(quarters == fecha.month)
                if len(posicion[0]) == 0:
                    fecha = fecha.subtract(months=1)
                else:
                    encontrado=True
            except:
                return None
        return get_periodo(fecha)
    else:
        return None


def get_periodo_label(periodo:str)-> str:
    """Obtener label de periodo en formato : Ene20"""
    year, month = explode(periodo=periodo)
    if year and month:
        date_candidate = pendulum.datetime(year=year, month=month, day=1)
        return str(date_candidate.format("MMMYY")).replace(".","").capitalize()
    else:
        return periodo


def get_periodo_range_label(periodo_inicio:str, periodo_fin:str)-> str:
    """Obtener label de un rango de fechas en formato : Ene-Feb2020"""
    year, month = explode(periodo=periodo_inicio)
    year2, month2 = explode(periodo=periodo_fin)
    if year and month and year2 and month2:
        date_candidate = pendulum.datetime(year=year, month=month, day=1)
        date_candidate2 = pendulum.datetime(year=year2, month=month2, day=1)
        return str(date_candidate.format("MMM")).replace(".","").capitalize() + "-" + str(date_candidate2.format("MMMYYYY")).replace("."," ").capitalize()
    else:
        return None


def validate_date(date: str, format: str) -> bool:
    """Valida la fecha sea correcta con el formato que se le proporciona"""
    try:
        new_date = pendulum.from_format(date, format)
        if new_date:
            return True
        return False
    except Exception as err:
        return False


def get_period_full_label(periodo: str) -> str:
    """Funcion que regresa el mes y el año en la siguiente forma
    (Enero 2020)
    """
    pendulum.set_locale('es')
    year, month = explode(periodo)
    if year and month:
        date = pendulum.datetime(year=year, month=month, day=1)
        return str(date.format('MMMM.YYYY')).replace('.', ' ').capitalize()
    else:
        return None


def get_date_for_sql_filter_from_periodo(periodo: str=None, explicit_day: int=None) -> str:
    """Recibe un periodo y regresa la fecha en formato YYYY-MM-DD
    dependiendo el periodo. Si el periodo corresponde a el actual, regresa
    la fecha actual. Si el periodo es de un mes pasado, regresa
    la fecha del ultimo dia del mes, el objetivo es tener una fecha para obtener
    informacion de sql.

    :param periodo: description, defaults to None
    :type periodo: str, optional
    :param explicit_day: description, defaults to None
    :type explicit_day: int, optional

    :return: String fecha con formato YYYY-MM-DD
    :rtype: str
    """
    if periodo is None:
        periodo = get_periodo()
    
    if is_valid(periodo):
        date_return = None
        year = periodo[:4]
        month = periodo[4:]
        date_now = pendulum.now()
        periodo_now = get_periodo(date=date_now)
        # la varianza es el dia
        day = 1 if explicit_day is None else int(explicit_day)
        day = str(day) if day > 9 else "0"+str(day) 

        if periodo == periodo_now and explicit_day is None:
            date_return = date_now
        else:
            date_return = pendulum.parse(f"{year}-{month}-{day}")
            if explicit_day is None:
                date_return = date_return.end_of("month")
        
        return date_return.format("YYYY-MM-DD")
    else:
        return None
