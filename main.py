from http.server import HTTPServer, SimpleHTTPRequestHandler
from datetime import datetime
import argparse
from collections import defaultdict

import pandas
from jinja2 import Environment, FileSystemLoader, select_autoescape


def get_arguments():
    parser = argparse.ArgumentParser(
        description="Script creates html file according to template.html."
    )
    parser.add_argument(
        'xlsx_file',
        nargs='?',
        default="wine.xlsx",
        help="the data base for wine's sorts."
    )
    return parser.parse_args()


def get_years_ending(year: int) -> str:
    year_double_end = year % 100
    if 11 <= year_double_end <= 20:
        return "лет"
    year_end = year % 10
    if year_end == 1:
        return "год"
    elif 1 < year_end < 5:
        return "года"
    else:
        return "лет"


def initialize_jinja2(years_together, wine_categories):
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render(
        wine_categories=wine_categories,
        years_together=years_together,
        years_together_end=get_years_ending(years_together),
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


def get_wines_sorts_list_from_xlsx(xlsx_file_name, sheet_name="Лист1"):
    wine_categories = defaultdict(list)
    excel_data_df = pandas.read_excel(
        io=xlsx_file_name,
        sheet_name=sheet_name,
        na_values=['N/A', 'NA'],
        keep_default_na=False,
    )
    for data_row_dict in excel_data_df.to_dict(orient='record'):
        wine_categories[data_row_dict["Категория"]].append(data_row_dict)

    return wine_categories


def main():
    arguments = get_arguments()
    wine_categories = get_wines_sorts_list_from_xlsx(arguments.xlsx_file)
    years_together = datetime.now().year - 1920
    initialize_jinja2(years_together, wine_categories)


if __name__ == '__main__':
    main()
