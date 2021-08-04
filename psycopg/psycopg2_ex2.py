from contextlib import closing
import psycopg2 as db
from psycopg.config import DebugConfig
from psycopg.connection import Cursor
from flask import Flask, request, jsonify
from psycopg.forms import DoctorForm, HospitalForm, HospitalUpdateForm, DoctorUpdateForm
import datetime
from flask_wtf import FlaskForm

app = Flask(__name__)

app.config.from_object(DebugConfig)

cursor = Cursor(
    module=db,
    database="hospital_db",
    host="localhost",
    port=5432,
    user="hospital",
    password="20122000vl",
)


def update_table(cur, form, table_name):
    values = form_to_dict(form)
    item_id = values["id"]
    values.pop("id")

    query = []
    formatted = []

    for key in values.keys():
        v = f'%({str(key) + "__val__"})s'
        formatted.append(v)

    for key, val in zip(values.keys(), formatted):
        query.append("=".join([key, val]))

    query = ", ".join(query)
    query = f"UPDATE {table_name} SET {query} WHERE id=%(id)s;"
    query_dict = {str(key) + "__val__": val for key, val in values.items()}
    query_dict["id"] = item_id

    cur.execute(query, query_dict)
    cur.execute(f"SELECT * FROM {table_name} WHERE id=%(id)s;", {"id": item_id})
    item = [
        cur.fetchone(),
    ]
    return item


def insert_into_table(cur, form, table_name):
    values = form_to_dict(form)

    formatted = []

    for key in values.keys():
        v = f'%({str(key) + "__val__"})s'
        formatted.append(v)

    insert_query = (
        "(" + ", ".join(values.keys()) + ") VALUES (" + ", ".join(formatted) + ");"
    )
    query_dict = {str(key) + "__val__": val for key, val in values.items()}
    cur.execute(f"INSERT INTO {table_name} {insert_query}", query_dict)

    assignments = []
    for key, formatted_val in zip(values.keys(), formatted):
        assignments.append("=".join([key, formatted_val]))
    select_query = " AND ".join(assignments)
    cur.execute(f"SELECT * FROM {table_name} WHERE {select_query};", query_dict)
    items = cur.fetchall()
    return items


def make_doctors_json(doctors: list):
    data = list()
    for doctor in doctors:
        data.append(
            {
                "id": doctor[0],
                "name": doctor[1],
                "hospital_id": doctor[2],
                "joining_date": doctor[3],
                "speciality": doctor[4],
                "salary": doctor[5],
                "experience": doctor[6],
            }
        )
    return jsonify(data)


def make_hospitals_json(hospitals: list):
    data = list()
    for hospital in hospitals:
        data.append(
            {
                "id": hospital[0],
                "name": hospital[1],
                "bed_count": hospital[2],
            }
        )
    return jsonify(data)


def form_to_dict(form: FlaskForm):
    values = {}
    for key in form._fields.keys():
        data = form.__getattribute__(key).data
        if data:
            if isinstance(data, datetime.datetime):
                data = str(data)
            values[key] = data
    return values


@app.route(
    "/version/",
    methods=[
        "GET",
    ],
)
def show_version_of_database():
    with cursor as cur:
        # Print PostgreSQL Connection properties
        dsn_data = cur.connection.get_dsn_parameters()
        cur.execute("SELECT version();")
        version = cur.fetchall()
        version.append(dsn_data)
    return str(version)


@app.route("/doctors/", methods=["GET", "POST", "PUT"])
def get_post_doctors():
    with cursor as cur:
        if request.method == "GET":
            cur.execute("SELECT * FROM doctors")
            doctors = cur.fetchall()
            return make_doctors_json(doctors)

        if request.method == "POST":
            form = DoctorForm(request.form)
            if form.validate():
                doctors = insert_into_table(cur, form, "doctors")
                return make_doctors_json(doctors)
            else:
                return jsonify(form.errors)

        if request.method == "PUT":
            form = DoctorUpdateForm(request.form)
            if form.validate():
                doctor = update_table(cur, form, "doctors")
                return make_doctors_json(doctor)
            else:
                return jsonify(form.errors)


@app.route("/hospitals/", methods=["GET", "POST", "PUT"])
def get__post_hospitals():
    with cursor as cur:
        if request.method == "GET":
            cur.execute("SELECT * FROM hospitals")
            hospitals = cur.fetchall()
            return make_hospitals_json(hospitals)

        if request.method == "POST":
            form = HospitalForm(request.form)
            if form.validate():
                hospitals = insert_into_table(cur, form, "hospitals")
                return make_hospitals_json(hospitals)
            else:
                return jsonify(form.errors)

        if request.method == "PUT":
            form = HospitalUpdateForm(request.form)
            if form.validate():
                hospital = update_table(cur, form, "hospitals")
                return make_hospitals_json(hospital)
            else:
                return jsonify(form.errors)


@app.route("/hospitals/<int:hospital_id>/", methods=["GET", "POST"])
def get_hospital(hospital_id):
    with cursor as cur:
        if request.method == "GET":
            cur.execute(
                "SELECT * FROM hospitals WHERE id=%(id)s", {"id": str(hospital_id)}
            )
            data = cur.fetchone()
            return jsonify(
                {
                    "id": data[0],
                    "name": data[1],
                    "bed_count": data[2],
                }
            )


@app.route("/doctors/<int:doctor_id>/", methods=["GET", "POST"])
def get_doctor(doctor_id):
    with cursor as cur:
        if request.method == "GET":
            cur.execute(
                "SELECT * FROM doctors WHERE id= %(id)s", {"id": str(doctor_id)}
            )
            data = cur.fetchone()
            return jsonify(
                {
                    "id": data[0],
                    "name": data[1],
                    "hospital_id": data[2],
                    "joining_date": data[3],
                    "speciality": data[4],
                    "salary": data[5],
                    "experience": data[6],
                }
            )


@app.route("/doctors/<speciality>/<float:salary>/", methods=["GET", "POST"])
def get_spec_doctor_list(speciality, salary):
    with cursor as cur:
        if request.method == "GET":
            cur.execute(
                "SELECT * FROM doctors WHERE salary >= %(salary)s AND speciality = %(speciality)s;",
                {"salary": salary, "speciality": speciality.title()},
            )
            doctors = cur.fetchall()
            return make_doctors_json(doctors)


@app.route(
    "/doctors_in_hospital/<int:hospital_id>/",
    methods=[
        "GET",
    ],
)
def doctors_in_hospital(hospital_id):
    with cursor as cur:
        if request.method == "GET":
            cur.execute(
                "SELECT * FROM doctors WHERE hospital_id = %(hospital_id)s;",
                {"hospital_id": hospital_id},
            )
            doctors = cur.fetchall()
            return make_doctors_json(doctors)


if __name__ == "__main__":
    app.run()
