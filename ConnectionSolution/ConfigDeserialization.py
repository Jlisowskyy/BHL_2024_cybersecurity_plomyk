import json
import MainFlowLib as MFL


def init_departments(json_data: str) -> list[MFL.Department]:
    data_dict = json.loads(json_data)
    departments_names = data_dict['Departments']
    departments_list = []
    for department_name in departments_names:
        department = MFL.Department(
            department_name,
            data_dict['BaseTestInterval'],
            data_dict['ReportPoints'],
            data_dict['IgnorePoints'],
            data_dict['PenaltyPoints'],
            data_dict['PointsThreshold']
        )
        departments_list.append(department)
    return departments_list

