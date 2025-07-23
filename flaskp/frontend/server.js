const express = require('express');
const bodyParser = require('body-parser');
const app = express();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static('public'));

app.post('/submit', (req, res) => {
    const formData = req.body;

    // Send data to Flask backend
    const fetch = (...args) => import('node-fetch').then(({default: fetch}) => fetch(...args));
    fetch('http://backend:5000/submit', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
    })
    .then(response => response.json())
    .then(data => res.send(`Backend responded: ${JSON.stringify(data)}`))
    .catch(err => res.send(`Error contacting backend: ${err}`));
});

app.listen(3000, () => console.log('Frontend running on port 3000'));
