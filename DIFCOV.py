# -*- coding: utf-8 -*-
"""
Practica 2 
Materia Sistemas expertos
Luis Eduardo Zamora Alvarado
Registro 19110410
Grado y grupo 6°E5

INSTALACION EXPERTA :    
    pip install experta 
    pip3 install experta 
    conda install experta
    install package experta 
    kite experta add
"""

from experta import *
import time
import os
Continuar = lambda: os.system ("cls")

class ContactoContagiado(Fact): #base del conocimiento
    ""
    
class FaltaDeAire(Fact):
    ""
    
class Estornudos(Fact):
    ""
    
class Fiebre(Fact):
    ""

class Tos(Fact):
    ""

class EscurrimientoNasal(Fact):
    ""

class CuerpoCortado(Fact):
    ""

class DolorGarganta(Fact):
    ""

class Diarrea(Fact):
    ""

class NoFuncionaTratamiento(Fact):
    ""

class SintomasPersistentes(Fact):
    ""
#########################################     MOTOR DE INFERENCIA      #############
class COVID(KnowledgeEngine):
    contador=0
    contador2=0
    @Rule(ContactoContagiado(contactoContagiado = '1')) #de experta, para definir regla, metodo y consecuente
    def sintomaCovid(self):
        self.contador=self.contador + 1
        self.declare(FaltaDeAire(faltaDeAire = input("¿Tienes sensación de falta de aire? (que no sea causada por alguna enfermedad crónica o previamente diagnosticada) \n1) Si \n2) No \n ")))
        print()

    @Rule(ContactoContagiado(contactoContagiado = '2'))#haciendo match
    def sintomaGripa(self):
        self.contador2=self.contador2 + 1
        self.declare(FaltaDeAire(faltaDeAire = input("¿Tienes sensación de falta de aire? (que no sea causada por alguna enfermedad crónica o previamente diagnosticada) \n1) Si \n2) No \n ")))
        print()
    
    @Rule(ContactoContagiado(contactoContagiado = '3'))
    def sintomaConfuso(self):
        self.contador2=self.contador2 + 1
        self.declare(FaltaDeAire(faltaDeAire = input("¿Tienes sensación de falta de aire? (que no sea causada por alguna enfermedad crónica o previamente diagnosticada) \n1) Si \n2) No \n ")))
        print()
    
    @Rule(FaltaDeAire(faltaDeAire = '1'))
    def sintomaCovid2(self):
        self.contador=self.contador + 1
        self.declare(Estornudos(estornudos = input("¿Tienes Estornudos? \n1) No \n2) Si \n ")))
        print()

    @Rule(FaltaDeAire(faltaDeAire = '2'))
    def sintomaGripa2(self):  
        self.contador2=self.contador2 + 1
        self.declare(Estornudos(estornudos = input("¿Tienes Estornudos? \n1) No \n2) Si \n ")))
        print()

    @Rule(Estornudos(estornudos = '1'))
    def sintomaCovid3(self):
        self.contador=self.contador + 1
        self.declare(Fiebre(fiebre = input("¿Tienes fiebre mayor a 38°C? \n1) Si \n2) No \n ")))
        print()

    @Rule(Estornudos(estornudos = '2'))
    def sintomaGripa3(self):  
        self.contador2=self.contador2 + 1
        self.declare(Fiebre(fiebre = input("¿Tienes fiebre mayor a 38°C? \n1) Si \n2) No \n ")))
        print()     

    @Rule(Fiebre(fiebre = '1'))
    def sintomaCovid4(self):
        self.contador=self.contador + 1
        self.declare(Tos(tos = input("¿Tienes tos seca? \n1) Siempre \n2) Algunas veces \n ")))
        print()

    @Rule(Fiebre(fiebre = '2'))
    def sintomaGripa4(self):
        self.contador2=self.contador2 + 1
        self.declare(Tos(tos = input("¿Tienes tos seca? \n1) Siempre \n2) Algunas veces \n ")))
        print()      
    
    @Rule(Tos(tos = '1'))
    def sintomaCovid5(self):
        self.contador=self.contador + 1
        self.declare(EscurrimientoNasal(escurrimientoNasal = input("¿Tienes escurrimiento nasal? \n1) Rara vez \n2) Casi siempre \n ")))
        print()

    @Rule(Tos(tos = '2'))
    def sintomaGripa5(self): 
        self.contador2=self.contador2 + 1
        self.declare(EscurrimientoNasal(escurrimientoNasal = input("¿Tienes escurrimiento nasal? \n1) Rara vez \n2) Casi siempre \n ")))
        print()  
    
    @Rule(EscurrimientoNasal(escurrimientoNasal = '1'))
    def sintomaCovid6(self):
        self.contador=self.contador + 1
        self.declare(CuerpoCortado(cuerpoCortado= input("¿Tienes cuerpo cortado o dolor muscular? \n1) Algunas veces \n2) Siempre \n ")))
        print()

    @Rule(EscurrimientoNasal(escurrimientoNasal = '2'))
    def sintomaGripa6(self): 
        self.contador2=self.contador2 + 1
        self.declare(CuerpoCortado(cuerpoCortado= input("¿Tienes cuerpo cortado o dolor muscular? \n1) Algunas veces \n2) Siempre \n ")))
        print()  
    
    @Rule(CuerpoCortado(cuerpoCortado = '1'))
    def sintomaCovid7(self):
        self.contador=self.contador + 1
        self.declare(DolorGarganta(dolorGarganta= input("¿Tienes dolor de garganta? \n1) Algunas veces \n2) Siempre \n ")))
        print()

    @Rule(CuerpoCortado(cuerpoCortado = '2'))
    def sintomaGripa7(self):
        self.contador2=self.contador2 + 1
        self.declare(DolorGarganta(dolorGarganta= input("¿Tienes dolor de garganta? \n1) Algunas veces \n2) Siempre \n ")))
        print()   

    @Rule(DolorGarganta(dolorGarganta = '1'))
    def sintomaCovid8(self):
        self.contador=self.contador + 1
        self.declare(Diarrea(diarrea= input("¿Tienes diarrea o malestar estomacal? \n1) Si \n2) No \n ")))
        print()

    @Rule(DolorGarganta(dolorGarganta = '2'))
    def sintomaGripa8(self):
        self.contador2=self.contador2 + 1
        self.declare(Diarrea(diarrea= input("¿Tienes diarrea o malestar estomacal? \n1) Si \n2) No \n ")))
        print()
               
    @Rule(Diarrea(diarrea = '1'))
    def sintomaCovid9(self):
        self.contador=self.contador + 1
        self.declare(NoFuncionaTratamiento(noFuncionaTratamiento= input("¿Has recibido tratamiento médico para tus síntomas? \n1) Sí, pero no funciona \n2) Sí, esta funcionando \n3) No \n ")))
        print()

    @Rule(Diarrea(diarrea = '2'))
    def sintomaGripa9(self):
        self.contador2=self.contador2 + 1
        self.declare(NoFuncionaTratamiento(noFuncionaTratamiento= input("¿Has recibido tratamiento médico para tus síntomas? \n1) Sí, pero no funciona \n2) Sí, esta funcionando \n3) No \n ")))
        print()      
    
    @Rule(NoFuncionaTratamiento(noFuncionaTratamiento = '1'))
    def sintomaCovid10(self):
        self.contador=self.contador + 1
        self.declare(SintomasPersistentes(sintomasPersistentes= input("¿Has salido los últimos días de casa? \n1) Si \n2) No \n ")))
        print()

    @Rule(NoFuncionaTratamiento(noFuncionaTratamiento = '2'))
    def sintomaGripa10(self):
        self.contador2=self.contador2 + 1
        self.declare(SintomasPersistentes(sintomasPersistentes= input("¿Has salido los últimos días de casa? \n1) Si \n2) No \n ")))
        print()

    @Rule(NoFuncionaTratamiento(noFuncionaTratamiento = '3'))
    def sintomaConfuso10(self):
        self.contador=self.contador + 1
        self.declare(SintomasPersistentes(sintomasPersistentes= input("¿Has salido los últimos días de casa? \n1) Si \n2) No \n ")))
        print()    

    @Rule(SintomasPersistentes(sintomasPersistentes = '1'))          #MOTOR DE EXPLICACION
    def sintomaCovid11(self):
        self.contador=self.contador + 1
        if(self.contador > self.contador2):
           Continuar()
           print()
           print("--> Tus síntomas coinciden con los de COVID-19, por favor acude a tu medico general, sin olvidar tu condición.")
           print("--> Acuda de inmediato, cuidese y cuide a los demas protegiendoso adecuadamente")
           print("--> Mientras te mantengas enfermo evita el contacto fisico y manten SusanaDistancia")
           print()
        else:
           Continuar()
           print() 
           print("--> Presentas algunos síntomas de enfermedad respiratoria, pero es poco probable que se trate de COVID-19.")
           print("--> En esta temporada es común presentar un resfriado o alergias.")
           print("--> Descansar en casa, beber muchos líquidos e incluir vitaminas y minerales en tu alimentación puede ayudarte a sentirte mejor.")
           print("--> Recuerda no automedicarte y seguir las medidas de prevención.")
           print()

    @Rule(SintomasPersistentes(sintomasPersistentes = '2'))
    def sintomaGripa11(self): 
        self.contador2=self.contador2 + 1
        if(self.contador > self.contador2):
           Continuar()
           print()
           print("--> Muy probablemente te encuentres contagiado con COVID-19. Acude a tu medico con las respectivas medidas de salubridad")
           print("--> Recuerda que el Covid-19, es mas contagioso que peligroso, asi que maten la calma.")
           print("--> Durante tu traslado y llegada al medico, evita el contaco fisico.")
           print()
        else:
           Continuar()
           print()
           print("--> Presentas algunos síntomas de enfermedad respiratoria, pero es poco probable que se trate de COVID-19.")
           print("--> En esta temporada es común presentar un resfriado o alergias.")
           print("--> Descansar en casa, beber muchos líquidos e incluir vitaminas y minerales en tu alimentación puede ayudarte a sentirte mejor.")
           print("--> Recuerda no auto medicarte y seguir las medidas de prevención.")
           print()
engine = COVID()
engine.reset()

Continuar()
print("DIAGNOSTICO PARA LA DETECCIÓN Y DIFERENCIACIÓN DE COVID-19 RESPECTO GRIPA")
print()
Continuar()
time.sleep(3)
print("Conteste las preguntas escribendo '1' '2' ó '3' segun sea su caso")
p1 = input("¿Has tenido contacto directo con algún paciente positivo confirmado con COVID-19? \n1) Si \n2) No \n3) No sé \n " )

print()

engine.declare((ContactoContagiado(contactoContagiado = p1)))
engine.run()