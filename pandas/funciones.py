def promedio(NA,NC):
    try:
        NC=NA[NC]
        a=0
        for i in range(len(NC)):
            a+=NC[i]
        return a/len(NC)
    except:
        return "Error al procesar la columna"
    
def  desviacion(NA, NC):
    try:
        NC=NA[NC]
        a= NC.std()
        return a
    except:
        return "Error al procesar la columna"

def percentiles(NA, NC):
    try:
        NC=NA[NC]
        p25 = NC.quantile(0.25)
        p50 = NC.quantile(0.50)
        p75 = NC.quantile(0.75)
        return p25 , p50 , p75
    except:
        return "Error al procesar la columna"
