import logging
import azure.functions as func
from azure.data.tables import TableServiceClient
import os
import uuid

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('新增裝置 API called.')
    name = req.get_json().get("name")
    if not name:
        return func.HttpResponse("請提供裝置名稱。", status_code=400)

    conn_str = os.environ["AzureWebJobsStorage"]
    table_service = TableServiceClient.from_connection_string(conn_str)
    table_client = table_service.get_table_client("devices")

    try:
        table_client.create_table()
    except:
        pass

    entity = {
        'PartitionKey': 'device',
        'RowKey': str(uuid.uuid4()),
        'name': name
    }
    table_client.create_entity(entity)

    return func.HttpResponse(f"新增裝置 {name} 成功！")