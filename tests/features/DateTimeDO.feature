Feature: Trae la fecha y hora de la Republica Dominicana

    Scenario Outline: DateTimeDO
        Given que quiero obtener el horario dominicano
        When desee <operacion> 
        Then el resultado debe ser <result>
        
        Examples: resta de Numeros
        | operacion   | result  |
        | datetimee   |  true   |