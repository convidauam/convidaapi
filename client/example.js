const OpenAPIClientAxios = require('openapi-client-axios').default;

const api = new OpenAPIClientAxios({
  definition: 'http://0.0.0.0:6543/openapi/openapi.json',
  axiosConfigDefaults: { baseURL: 'http://0.0.0.0:6543' }
});

async function createExamples() {
  const client = await api.init();
  const result = await client.getExample();
  console.log('GET result:', result.data);
  const res = await client.createExample(null, { id: 4, name: 'Garfield', bee: 'Felidae' });
  console.log('Example created', res.data);
}

createExamples();