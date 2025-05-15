# IoT Minimal Azure Demo

這是一個最小可執行的 IoT 雲端架構，包含：
- 前端：HTML 表單（App Service）
- 後端：Azure Function API
- 資料儲存：Azure Table Storage
- 自動化部署：GitHub Actions

## 快速啟動
```bash
bash deploy/deploy.sh
```

## GitHub Actions 設定
在 repo 的 Secrets 中新增：
- `AZURE_CREDENTIALS`: 你的 Service Principal JSON

## 手動測試 API
```bash
curl -X POST https://YOUR-FUNCTION-APP.azurewebsites.net/api/addDevice \
     -H "Content-Type: application/json" \
     -d '{"name": "測試裝置"}'
```