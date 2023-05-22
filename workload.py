import jinja2
import os 
from jinja2 import Template
import pandas as pd 
import re

latex_knowledgd_env = jinja2.Environment(
    block_start_string = '\BLOCK{',
    block_end_string = '}',
    variable_start_string = '\VAR{',
    variable_end_string = '}',
    comment_start_string = '\#{',
    comment_end_string = '}',
    line_statement_prefix = '%%',
    line_comment_prefix = '%#',
    trim_blocks = True,
    autoescape = False,
    loader = jinja2.FileSystemLoader(os.path.abspath('.'))
)

template = latex_knowledgd_env.get_template('workload.jinja2')

if __name__ == "__main__":

    df = pd.read_excel('workload.xlsx')


    cat = []
    for i in df['task']:
        cat.append(i)

    index = cat
    hrs = df['hour']

    rows = df.to_dict(orient = 'records')
    tasks = df['task'].str.split(";").squeeze()
    hours = df['hour'].str.split(";").squeeze()


    with open("workload.tex", "w") as f:
        f.write(template.render(
            rows = rows,
            tasks = tasks,
            hours = hours
            ))