#!/usr/bin/env python

# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Simple application that performs a query with BigQuery."""
# [START bigquery_simple_app_all]
# [START bigquery_simple_app_deps]
from google.cloud import bigquery
import os


# [END bigquery_simple_app_deps]


def ingest_CoveoSearchClicksField():
    # [START bigquery_simple_app_client]
    client = bigquery.Client()
    # [END bigquery_simple_app_client]
    # [START bigquery_simple_app_query]
    # TODO(developer): Set table_id to the ID of the table to create.

    table_id = "coveo-search-analytics.Keywords_Coveo.SearchClicks"

    file_path = '/Users/satyen/projects/Digital_CX/Coveo/Clicks/xak.csv'

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV, skip_leading_rows=1, autodetect=False,
    )

    with open(file_path, "rb") as source_file:
        job = client.load_table_from_file(source_file, table_id, job_config=job_config)

        job.result()  # Waits for the job to complete.

        table = client.get_table(table_id)  # Make an API request.
        print("Loaded {} rows and {} columns to {}".format(table.num_rows, len(table.schema), table_id))


def ingest_CoveoSearchKeywordField():
    # [START bigquery_simple_app_client]
    client = bigquery.Client()
    # [END bigquery_simple_app_client]
    # [START bigquery_simple_app_query]
    # TODO(developer): Set table_id to the ID of the table to create.

    table_id = "coveo-search-analytics.Keywords_Coveo.Keyword"
    file_path = '/Users/satyen/projects/Digital_CX/Coveo/keywords/'

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV, skip_leading_rows=1, autodetect=False,
    )


    for fileName in os.listdir(file_path):
        if fileName != '.DS_Store':
            with open(file_path + fileName, "rb") as source_file:
                job = client.load_table_from_file(source_file, table_id, job_config=job_config)

                job.result()  # Waits for the job to complete.

                table = client.get_table(table_id)  # Make an API request.
                print("Loaded {} rows and {} columns to {}".format(table.num_rows, len(table.schema), table_id))


def ingest_CoveoSearchesField():
    # [START bigquery_simple_app_client]
    client = bigquery.Client()
    # [END bigquery_simple_app_client]
    # [START bigquery_simple_app_query]
    # TODO(developer): Set table_id to the ID of the table to create.

    table_id = "coveo-search-analytics.Keywords_Coveo.SearchResults"
    file_path = '/Users/satyen/projects/Digital_CX/Coveo/searches/'

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV, skip_leading_rows=1, autodetect=False,
    )

    for fileName in os.listdir(file_path):
        if fileName != '.DS_Store':
            with open(file_path + fileName, "rb") as source_file:
                print (source_file)
                job = client.load_table_from_file(source_file, table_id, job_config=job_config)

                job.result()  # Waits for the job to complete.

                table = client.get_table(table_id)  # Make an API request.
                print("Loaded {} rows and {} columns to {}".format(table.num_rows, len(table.schema), table_id))


def ingest_Coveo_Custom_Events():
    # [START bigquery_simple_app_client]
    client = bigquery.Client()
    # [END bigquery_simple_app_client]
    # [START bigquery_simple_app_query]
    # TODO(developer): Set table_id to the ID of the table to create.

    table_id = "coveo-search-analytics.Keywords_Coveo.SearchEvents"
    file_path = '/Users/satyen/projects/Digital_CX/Coveo/custom_events/'

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV, skip_leading_rows=1, autodetect=False,
    )

    for fileName in os.listdir(file_path):
        if fileName != '.DS_Store':
            with open(file_path + fileName, "rb") as source_file:
                print (source_file)
                job = client.load_table_from_file(source_file, table_id, job_config=job_config)

                job.result()  # Waits for the job to complete.

                table = client.get_table(table_id)  # Make an API request.
                print("Loaded {} rows and {} columns to {}".format(table.num_rows, len(table.schema), table_id))



def query_stackoverflow():
    # [START bigquery_simple_app_client]
    client = bigquery.Client()
    # [END bigquery_simple_app_client]
    # [START bigquery_simple_app_query]
    query_job = client.query(
        """
        SELECT *
        FROM `coveo-search-analytics.Keywords_Coveo.Keyword`
        LIMIT 1000"""
    )

    results = query_job.result()  # Waits for job to complete.
    # [END bigquery_simple_app_query]

    # [START bigquery_simple_app_print]
    for row in results:
        print(row.Search_Id, row.Date_Time, row.Keyword)
    # [END bigquery_simple_app_print]


if __name__ == "__main__":
    #query_stackoverflow()
    #ingest_CoveoSearchKeywordField()
    #ingest_CoveoSearchesField()
    #ingest_CoveoSearchClicksField()
    ingest_Coveo_Custom_Events()
# [END bigquery_simple_app_all]
