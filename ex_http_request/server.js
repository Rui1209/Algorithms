// server.js
const express = require('express');
const app = express();

app.use(express.json()); // 支援 JSON body

app.post('/api/data', (req, res) => {
  console.log('伺服器收到資料:', req.body);

  // 回應一個訊息給 Client
  res.json({
    message: '伺服器已成功接收資料！',
    receivedData: req.body
  });
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`🚀 伺服器正在 port ${PORT} 運行...`);
});
