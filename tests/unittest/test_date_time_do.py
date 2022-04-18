import unittest
from pytest_bdd import scenario, given, when, then, parsers, scenarios
from date_timee import DateTimee
from datetime import datetime

scenarios('DateTimeDO.feature')

@given("que quiero obtener el horario dominicano", target_fixture="date_timee")
def step_impl():
    return DateTimee()

@when(parsers.cfparse("desee {operacion:String}", 
                    extra_types=dict(String=str)),  target_fixture="date_timee_result",
)
def step_impl(date_timee, operacion):
    if operacion == "datetimee":
        return date_timee.dateTimeDO();

@then(parsers.cfparse("el resultado debe ser {result}"))
def step_impl(date_timee_result, result):
    dateNew = datetime.now().strftime("%d %B, %Y %H:%M:%S");
    assert dateNew == str(date_timee_result)
