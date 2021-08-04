from flask_wtf import FlaskForm
from wtforms import validators, IntegerField, StringField, DateTimeField, FloatField


def is_num(form, data):
    if not str(data.data).isnumeric():
        raise validators.ValidationError("This field should be a number")


def is_alpha(form, data):
    if not str(data.data).isalpha():
        raise validators.ValidationError("This field must consist of letters")


def is_float(form, data):
    try:
        f = float(data.data)
    except Exception:
        raise validators.ValidationError("This field is not a floating point number")


class DoctorForm(FlaskForm):
    doctor_name = StringField(
        label="doctor name",
        validators=[validators.Regexp(r"(\w+\s?\w*)+"), validators.DataRequired()],
    )
    hospital_id = IntegerField(
        label="hospital id", validators=[is_num, validators.DataRequired()]
    )
    joining_date = DateTimeField(
        label="joining date", validators=[validators.Optional()]
    )
    speciality = StringField(
        label="speciality", validators=[is_alpha, validators.DataRequired()]
    )
    salary = FloatField(
        label="salary", validators=[is_float, validators.DataRequired()]
    )
    experience = IntegerField(
        label="experience", validators=[is_num, validators.DataRequired()]
    )


class HospitalForm(FlaskForm):
    name = StringField(
        label="name",
        validators=[validators.Regexp(r"(\w+\s?\w*)+"), validators.DataRequired()],
    )
    bed_count = IntegerField(
        label="bed count",
        validators=[is_num, validators.DataRequired(), validators.NumberRange(min=0)],
    )


class HospitalUpdateForm(FlaskForm):
    id = IntegerField(
        label="id",
        validators=[is_num, validators.DataRequired(), validators.NumberRange(min=1)],
    )
    name = StringField(
        label="name",
        validators=[validators.Regexp(r"(\w+\s?\w*)+"), validators.Optional()],
    )
    bed_count = IntegerField(
        label="bed count", validators=[is_num, validators.Optional()]
    )


class DoctorUpdateForm(FlaskForm):
    id = IntegerField(
        label="id",
        validators=[is_num, validators.DataRequired(), validators.NumberRange(min=101)],
    )
    doctor_name = StringField(
        label="doctor name", validators=[is_alpha, validators.Optional()]
    )
    hospital_id = IntegerField(
        label="hospital id", validators=[is_num, validators.Optional()]
    )
    joining_date = DateTimeField(
        label="joining date", validators=[validators.Optional()]
    )
    speciality = StringField(
        label="speciality", validators=[is_alpha, validators.Optional()]
    )
    salary = FloatField(label="salary", validators=[is_float, validators.Optional()])
    experience = IntegerField(
        label="experience", validators=[is_num, validators.Optional()]
    )
