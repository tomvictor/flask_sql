from models import Organization, db
from flask import jsonify


def build_query(qps):
    qry = db.session.query(Organization)
    for attr, value in qps.items():
        qry = qry.filter(getattr(Organization, attr).equal(value))
    return qry


def db_query():

    organization = db.session.query(Organization)

    print(list(organization))

    resp = [org.as_dict() for org in organization]
    resp = jsonify(resp)

    return resp, 200
