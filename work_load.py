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

template = latex_knowledgd_env.get_template('work_load.jinja2')

if __name__ == "__main__":

    df = pd.read_excel('work_load.xlsx')

    rows = df.to_dict(orient = 'records')


    with open("bs.tex", "w") as f:
    f.write(template.render(
        rows = rows
        ))