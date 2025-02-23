const dotenv = require('dotenv');
dotenv.config();

const { WebBrowser } = require('langchain/tools/webbrowser');
const { ChatOpenAI, OpenAIEmbeddings } = require('@langchain/openai');

async function run() {
  const model = new ChatOpenAI({ temperature: 0 });
  const embeddings = new OpenAIEmbeddings();

  const browser = new WebBrowser({ model, embeddings });

  const result = await browser.invoke(
    `"https://www.themarginalian.org/2015/04/09/find-your-bliss-joseph-campbell-power-of-myth","who is joseph campbell"`
  );

  console.log(result);
}

// Call the `run` function
run().catch((error) => console.error(error));