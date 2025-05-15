#!/bin/bash
az group create --name iot-demo --location eastasia
az storage account create --name iotstor123456 --resource-group iot-demo --location eastasia --sku Standard_LRS
az functionapp create --resource-group iot-demo --consumption-plan-location eastasia \
  --runtime python --functions-version 4 --name my-iot-func123 \
  --storage-account iotstor123456
az storage table create --name devices --account-name iotstor123456 --auth-mode login