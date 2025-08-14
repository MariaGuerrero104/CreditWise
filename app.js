const express = require('express');
const app = express();

app.use(express.json());

app.get('/', (req, res) => {
    res.send('Servidor Node.js para CreditWise en funcionamiento');
});

app.listen(3000, () => {
    console.log('Servidor escuchando en http://localhost:3000');
});
