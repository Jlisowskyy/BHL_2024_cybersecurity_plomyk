import json
import MainFlowLib as mfl
from MainFlowLib import Worker

def init_departments(json_data: str) -> list[mfl.Department]:
    data_dict = json.loads(json_data)
    departments_names = data_dict['Departments']
    departments_list = []
    for department_name in departments_names:
        department = mfl.Department(
            department_name,
            data_dict['BaseTestInterval'],
            data_dict['ReportPoints'],
            data_dict['IgnorePoints'],
            data_dict['PenaltyPoints'],
            data_dict['PointsThreshold']
        )
        departments_list.append(department)
    return departments_list


def init_workers(json_data: str) -> list[list[str, mfl.Worker]]:
    rv = list()

    data_dict = json.loads(json_data)
    for record in data_dict:
        worker = mfl.Worker(
            record['name'],
            record['surname'],
            record['mail'],
            [mfl.LinkedinData(link) for link in record['dataset']],
            record['points'],
            record['lastTest']
        )

        rv.append([record['department'], worker])

    return rv
