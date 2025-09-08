// client.js
const request = require('request');

const options = {
  url: 'http://localhost:3000/api/data',
  method: 'POST',
  json: {
    name: 'Alice',
    age: 25,
    interests: ['coding', 'music']
  }
};

request(options, (error, response, body) => {
  if (error) {
    console.error('⚠️ 發送請求時出錯:', error);
  } else {
    console.log('✅ 伺服器回應狀態:', response.statusCode);
    console.log('📨 回傳內容:', body);
  }
});
