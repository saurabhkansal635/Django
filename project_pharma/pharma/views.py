from django.shortcuts import render
import pandas as pd
import sqlite3
pd.set_option('display.max_colwidth', 100)
from datetime import datetime

con = sqlite3.connect(r"C:\Work\Saurabh_Kansal\Upgrad\django\project_pharma\db.sqlite3")
# Load the data into a DataFrame
product_start_end_df = pd.read_sql_query("SELECT * from product_start_end", con)
event_start_end_df = pd.read_sql_query("SELECT * from event_start_end", con)
con.close()

product_list = ['None'] + list(product_start_end_df.product_id.unique())
event_list = ['None'] +  list(event_start_end_df.event.unique())

product_start_end_df.start_date = pd.to_datetime(product_start_end_df.start_date,  infer_datetime_format=True)
product_start_end_df.end_date = pd.to_datetime(product_start_end_df.end_date, infer_datetime_format=True)

event_start_end_df.start_date = pd.to_datetime(event_start_end_df.start_date,  infer_datetime_format=True)
event_start_end_df.end_date = pd.to_datetime(event_start_end_df.end_date, infer_datetime_format=True)

# Create your views here.

# demo inputs
product_id_selected = 'Lipitor'
event_name_selected = 'appendicitis'
start_date = '2011-01-27'
end_date = '2016-12-31'


def pharma_view(request):
    product_id_selected = request.GET.get("product_id", None)
    event_name_selected = request.GET.get("event_name", None)
    start_date = request.GET.get("start_date", '')
    print(start_date)
    end_date = request.GET.get("end_date", '')
    print(end_date)
    if (start_date != "") and (end_date != ""):
        start_date1 = datetime.strptime(start_date, '%Y-%m-%d')
        end_date1 = datetime.strptime(end_date, '%Y-%m-%d')
        product_start_end_df1 = product_start_end_df[(product_start_end_df.start_date >= start_date1)
                                                     & (product_start_end_df.end_date <= end_date1)]

        product_start_end_df_html = product_start_end_df1.to_html(index=False, index_names=False, justify='center')

        product_start_end_df_html_str = product_start_end_df_html.replace('\n', '')

        event_start_end_df1 = event_start_end_df[(event_start_end_df.start_date >= start_date1)
                                                     & (event_start_end_df.end_date <= end_date1)]
        event_start_end_df1 = event_start_end_df1

        event_start_end_df_html = event_start_end_df1.to_html(index=False, index_names=False, justify='center')

        event_start_end_df_html_str = event_start_end_df_html.replace('\n', '')

        product_event_start_end_df = pd.concat([product_start_end_df1, event_start_end_df1], axis=1)
        product_event_start_end_df_html = product_event_start_end_df.to_html(index=False, index_names=False, justify='center')

        product_event_start_end_df_html_str = product_event_start_end_df_html.replace('\n', '')

    else:
        product_start_end_df_html_str = None
        event_start_end_df_html_str = None
        product_event_start_end_df_html_str = None


    context = {'product_list': product_list, 'event_list': event_list,
               'product_id_selected': product_id_selected,
               'event_name_selected': event_name_selected,
               'start_date': start_date,
               'end_date': end_date,
               'product_start_end_df_html_str': product_start_end_df_html_str,
               'event_start_end_df_html_str': event_start_end_df_html_str,
               'product_event_start_end_df_html_str': product_event_start_end_df_html_str,
               }

    return render(request=request,
                  template_name='pharma/pharma_website.html',
                  context=context)