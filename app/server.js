import express from 'express';
import axios from 'axios';
import path from 'path';
import { config } from 'dotenv';

config();
const SUGGESTIONS_SERVICE_URL = process.env.SUGGESTIONS_SERVICE_URL;

const app = express();

const staticFilePath = path.join(path.resolve(), 'web/build');
app.use(express.static(staticFilePath));
app.use(express.json()); 

app.get('/', (_req, res) => {
  return res.sendFile(path.join(staticFilePath, 'index.html'));
});

app.post('/suggestions', async (req, res) => {
  const { prefix = null} = req.body;

  if (!prefix) return res.send([]);

  const { data } = await axios({
    method: 'POST',
    url: SUGGESTIONS_SERVICE_URL,
    data: {
      prefix
    }
  });

  return res.send(data);
});

/**
 * 404 for unmatched routes
 */
app.use((_req, res) => {
  return res.status(404);
});

app.listen(process.env.PORT || 8000, () => {console.log('Started.')});
