from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

def Create_Cove_SearchClicks_table():
    # TODO(developer): Set table_id to the ID of the table to create.
    table_id = "coveo-search-analytics.Keywords_Coveo.SearchClicks"

    schema = [
        bigquery.SchemaField("Click_Id", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Search_Id", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Date_Time", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("AB_Test_Name", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("AB_Test_Version", "STRING", mode="NULLABLE"),

        bigquery.SchemaField("Additional_Data", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Browser", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Browser_with_Version", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("City", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Click_Cause_1", "STRING", mode="NULLABLE"),

        bigquery.SchemaField("Click_Cause_2", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Click_Additional_Data", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Click_Date_Time", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Click_Origin_1_Page_Hub", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Click_Origin_2_Tab_Interface", "STRING", mode="NULLABLE"),

        bigquery.SchemaField("Click_Rank", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Click_Ranking_Modifier", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Client_Id", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Collection_Name", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Country", "STRING", mode="NULLABLE"),

        bigquery.SchemaField("Device_Category", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Document_Author", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Document_Category", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Document_Title", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Document_URL", "STRING", mode="NULLABLE"),

        bigquery.SchemaField("Event_Cause", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Event_Outcome", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Is_Anonymous", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Is_Internal", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Is_Mobile", "STRING", mode="NULLABLE"),

        bigquery.SchemaField("Language", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Operating_System", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Operating_System_with_Version", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Origin_1_Page_Hub", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Origin_2_tab_interface", "STRING", mode="NULLABLE"),

        bigquery.SchemaField("Origin_3_Referrer", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Origin_Context", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Query_Pipeline", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Region", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Document_sysurihash_Field", "STRING", mode="NULLABLE"),

        bigquery.SchemaField("Source_Name", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("User_Agent", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("User_Id", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("User_Name", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Visit_Id", "STRING", mode="NULLABLE"),

        bigquery.SchemaField("Visitor_Id", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("TechPoint", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("QA_or_PRD_Source", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Document_Title_2", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Document_URL_2", "STRING", mode="NULLABLE"),

    ]

    table = bigquery.Table(table_id, schema=schema)
    table = client.create_table(table)  # Make an API request.
    print(
        "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
    )


def Create_Cove_CustomEvents_table():
    # TODO(developer): Set table_id to the ID of the table to create.
    table_id = "coveo-search-analytics.Keywords_Coveo.SearchEvents"

    schema = [
        bigquery.SchemaField("Custom_EventId", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Search_Id", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Date_Time", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("AB_Test_Name", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("AB_Test_Version", "STRING", mode="NULLABLE"),

        bigquery.SchemaField("Additional_Data", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Browser", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Browser_with_Version", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("City", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Client_Id", "STRING", mode="NULLABLE"),


        bigquery.SchemaField("Country", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Custom_Event_Additional_Data", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Custom_Event_Date_Time", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Custom_Event_Origin_1_Page_Hub", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Custom_Event_Origin_2_Tab_Interface", "STRING", mode="NULLABLE"),

        bigquery.SchemaField("Device_Category", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Event_Outcome", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Event_Type", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Event_Value", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Is_Anonymous", "STRING", mode="NULLABLE"),

        bigquery.SchemaField("Is_Internal", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Is_Mobile", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Lanugae", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Operating_System", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Operating_System_with_Version", "STRING", mode="NULLABLE"),

        bigquery.SchemaField("Origin_1", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Origin_2", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Origin_3", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Origin_Context", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Region", "STRING", mode="NULLABLE"),

        bigquery.SchemaField("User_Agent", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("User_Id", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("User_Name", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Visit_Id", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Visitor_Id", "STRING", mode="NULLABLE"),

        bigquery.SchemaField("TechPoint", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("PRD_Source", "STRING", mode="NULLABLE"),
    ]

    table = bigquery.Table(table_id, schema=schema)
    table = client.create_table(table)  # Make an API request.
    print(
        "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
    )

def Create_SearchResults_table():
    # TODO(developer): Set table_id to the ID of the table to create.
    table_id = "coveo-search-analytics.Keywords_Coveo.SearchResults"

    schema = [
        bigquery.SchemaField("Search_Id", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Date_Time", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("AB_Test_Name", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("AB_Test_Version", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Additional_Data", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Advanced_Query_Expression", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Batch_Id", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Browser", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Browser_with_Version", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("City", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Client_Id", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Country", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Device_Category", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Event_Cause", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Event_Outcame", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Facet_State", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Has_Clicks", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Has_Results", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Is_Anonymous", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Is_Internal", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Is_Mobile", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Lanugae", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Number_of_Results", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Operating_System", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Operating_System_with_Version", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Origin_1", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Origin_2", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Origin_3", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Origin_Context", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Query_Pipeline", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Region", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Response_Time", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Search_Cause", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Search_Cause_1", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Search_Additional_Data", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Search_Date_Time", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Search_Index_Id", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Search_Is_Contextual", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Search_Origin_1", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Search_Origin_2", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("User_Agent", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("User_Id", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("User_Name", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("User_Query", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Visit_Id", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Visitor_Id", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Tab_Select", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Facet_ID", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Facet_Title", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Pager_Number", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("TechPoint", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("PRD_Source", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Source", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Facet_Value", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("Staging", "STRING", mode="NULLABLE"),
    ]

    table = bigquery.Table(table_id, schema=schema)
    table = client.create_table(table)  # Make an API request.
    print(
        "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
    )


if __name__ == "__main__":
    #Create_Coveo_Clicks_table()
    #Create_Cove_CustomEvents_table()
    #Create_SearchResults_table()
    Create_Cove_SearchClicks_table()
