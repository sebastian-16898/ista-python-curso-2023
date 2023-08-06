import csv
class datos:
    
    def __init__(self,curso, cedula):
        self.curso=curso
        self.cedula=cedula

    def imprimir(self):
        print ("El curso es: "+ f"{self.curso}" " y la cedula es: "+f"{self.cedula}")   
    
    def leer_archivo():
        
        results=[]
        with open('estudiante.csv') as a:
            reader = csv.DictReader(a)
            for row in reader:
                results.append(row)
        return results
    

    def escrbir_datos(cedula, nombre_materia, ano, mes , hora):
       
        with open('asistencia.csv','a',newline='') as a:
           escribir=csv.writer(a)
           escribir.writerow([cedula, nombre_materia, ano, mes , hora])
        
    
    def leer_asistencia():
        
        results=[]
        with open('asistencia.csv') as a:
            reader = csv.DictReader(a)
            for row in reader:
                results.append(row)
        return results
    
    def buscar_asistencia(cedula, curso):
        cont=0
        with open('asistencia.csv') as a:
            reader = csv.reader(a, delimiter=",")
            for row in reader:
                if(cedula==row[0] and curso==row[1]):
                    cont+=1
        return "Asistencias: "+str(cont)
         