def promedio(NA,NC):
    try:
        NC=NA[NC]
        a=0
        for i in range(len(NC)):
            a+=NC[i]
        return a/len(NC)
    except:
        return "Error al procesar la columna"