# -*- coding: utf-8 -*-

import pyodbc
import sys
from collections import OrderedDict
from contextlib import contextmanager
# from logger import Log


@contextmanager
def connect_db_sap(commit=False):
   dsn = 'sqlserverdatasource'
   user = 'sa'
   password = 'SBOartatlas'
   database = 'SBO_ATLAS_PRODUCCION'

   con_string = 'DSN=%s;UID=%s;PWD=%s;DATABASE=%s;' % (dsn, user,
                                                       password, database)
   cnxn = pyodbc.connect(con_string)
   cursor = cnxn.cursor()

   try:
       yield cursor
   except pyodbc.DatabaseError as err:
       sys.stderr.write(str(err))
       cursor.rollback()
       raise err
   else:
       if commit:
           cursor.commit()
       else:
           cursor.rollback()
   finally:
       cursor.close()
       del cursor
       cnxn.close()


def get_articulos(modelo, almacen):
    query_string = (
       "SELECT "
        "    ITSM_impresion_stock.itemcode2 AS itemcode2, "
        "    ITSM_impresion_stock.OnHand AS onhand, "
        "    ITSM_impresion_stock.U_SYP_CL_DESCMOD AS descripcion, "
        "    ITSM_impresion_stock.U_SYP_PT_COLOR AS color, "
        "    ITSM_impresion_stock.U_SYP_PT_TALLA AS talla, "
        "    ITSM_impresion_stock.U_SYP_PRECIO_DOLAR AS precio, "
        "    ITSM_impresion_stock.U_SYP_CODANT AS modelo, "
        "    ITSM_impresion_stock.U_SYP_DESCCOMP, "
        "    ITSM_impresion_stock.U_SYP_AA_COMOD, "
        "    ITSM_impresion_stock.WhsCode "
        "FROM "
        "    SBO_ATLAS_PRODUCCION.dbo.ITSM_impresion_stock ITSM_impresion_stock "
        "WHERE "
        "    (ITSM_impresion_stock.U_SYP_AA_COMOD='{0}') AND (ITSM_impresion_stock.WhsCode={1}) "
        "ORDER BY itemcode2"
       .format(
           modelo,
           almacen
       )
    )
    # log = Log()
    # log.logger.info(query_string)
    result = []
    with connect_db_sap() as cursor:
        cursor.execute(query_string)
        rows = cursor.fetchall()
        result = [
            {
                'itemcode2': row.itemcode2,
                'onhand': row.onhand,
                'descripcion': row.descripcion,
                'color': row.color,
                'talla': row[4],
                'descripcion': row.talla,
                'precio': row.precio,
                'modelo': row.modelo
            }
            for row in rows
        ]
    return result

