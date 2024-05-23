from langchain_community.utilities.sql_database import SQLDatabase
import os
from decimal import Decimal


db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')
db_host = os.environ.get('DB_HOST')
db_name = os.environ.get('DB_NAME')

def format_user_question(query,job_id):
    question = f"from job_id={job_id}. {query}"
    return question


def connect_database():
    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")
    return db


def convert_2_list(result):
    data_list = eval(result)
    return data_list

def generate_html_table(data):
    is_html = 1
    if len(data[0]) == 1:
        is_html = 0
        return str(data[0][0]),is_html
    
    html_table = """
    <table>
        <tr>
            <th>Name</th>
            <th>Score</th>
            <th>Phone</th>
            <th>Email</th>
            <th>Years of Experience</th>
            <th>Age</th>
            <th>Resume URL</th>
            <th>Summary</th>
            <th>Skills</th>
        </tr>
    """

    for row in data:
        html_table += "<tr>"
        for index, item in enumerate(row[3:], start=3):
            if index == 9:  # Check if it's the Resume URL column
                html_table += f"<td><a href='{item}'>Resume Link</a></td>"
            elif index == 6:
                html_table += f"<td><a href='mailto:{item}'>{item}</a></td>"
            else:
                if isinstance(item, tuple) and len(item) == 1:
                    html_table += f"<td>{item[0]}</td>"
                else:
                    html_table += f"<td>{item}</td>"
        html_table += "</tr>"

    html_table += """
    </table>

    """

    return html_table,is_html
