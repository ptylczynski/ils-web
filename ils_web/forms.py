from django.forms import Form, CharField, IntegerField, FloatField


class DataForm(Form):
    friction_expression = CharField(
        max_length=100,
        label="Friction Expression"
    )

    gravity_expression = CharField(
        max_length=100,
        label="Gravity Expression"
    )

    plane_expression = CharField(
        max_length=100,
        label="Plane Expression"
    )

    tick_time = FloatField(
        min_value=0,
        label="Tick Time"
    )

    total_ticks = IntegerField(
        min_value=0,
        label="Total Ticks"
    )

    start_point = IntegerField(
        label="Start Point"
    )

    end_point = IntegerField(
        label="End Point"
    )
