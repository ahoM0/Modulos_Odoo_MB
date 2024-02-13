# -*- coding: utf-8 -*-

from odoo import models, fields, api

#Definimos el modelo de datos
class lista_tareas(models.Model):
    #Nombre y descripcion del modelo de datos
    _name = 'lista_tareas.lista'
    _description = 'Modelo de la lista de tareas'

    #Como no tenemos un atributo "name" en nuestro modelo, indicamos que cuando
    #se necesite un nombre, se usara el atributo tarea
    _rec_name="tarea"

   
    tarea = fields.Char("Título")
    prioridad = fields.Integer("Prioridad")
    fecha = fields.Date("Fecha Inicio")
    horas = fields.Integer("Horas")
    fecha_fin = fields.Date("Fecha Fin")
    imagen_medium = fields.Image("Imagen")
    
    urgente = fields.Boolean(compute="_value_urgente", store=True)
    realizada = fields.Boolean()


    #Este es un ejemplo de "valor computado." Este computo depende de la variable prioridad.
    #La dependencia se indica mediante el decorador
    @api.depends('prioridad')
    
    #Funcion para calcular el valor de urgente.
    #Recibe "self" que se refiere al modelo completo (no a un registro solo)
    def _value_urgente(self):
        #Para cada registro... (recordamos, self es el modelo, no un registro)
        for record in self:
            #Si la prioridad es mayor que 10, se considera urgente, en otro caso no lo es
            if record.prioridad>10:
                record.urgente = True
            else:
                record.urgente = False

                