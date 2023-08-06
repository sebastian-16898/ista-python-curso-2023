import pytest
import csv
class TestEstudianteAsistencia:

    def test_prueba(self):
       with open('asistencia.csv') as a:
            reader = csv.reader(a, delimiter=",")
            for row in reader:
                if("0107291452"==row[0] and "java"==row[1]):
                    assert row