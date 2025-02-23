const { OpenAI, OpenAIEmbeddings } = require("@langchain/openai");
const { initializeAgentExecutorWithOptions } = require("langchain/agents");
const { Calculator } = require("@langchain/community/tools/calculator");
const { WebBrowser } = require("langchain/tools/webbrowser");
const { SerpAPI } = require("@langchain/community/tools/serpapi");

require("dotenv").config(); 


const run = async () => {
  const model = new OpenAI({ temperature: 0,  maxTokens: 1000  }); // Increase maxTokens
  const embeddings = new OpenAIEmbeddings();
  const tools = [
    new SerpAPI(process.env.SERPAPI_API_KEY, {
      location: "Austin,Texas,United States",
      hl: "en",
      gl: "us",
    }),
    new Calculator(),
    new WebBrowser({ model, embeddings }),
  ];

  const executor = await initializeAgentExecutorWithOptions(tools, model, {
    agentType: "zero-shot-react-description",
    verbose: true,
    agentArgs: {
      prefix: `Answer the following questions as best you can. You have access to the following tools:

search: a search engine. useful for when you need to answer questions about current events. input should be a search query.
calculator: Useful for getting the result of a math expression. The input to this tool should be a valid mathematical expression that could be executed by a simple calculator.
web-browser: useful for when you need to find something on or summarize a webpage. input should be a comma separated list of "ONE valid http URL including protocol","what you want to find on the page or empty string for a summary".

Use the following format in your response:

Question: the input question you must answer
Thought: you should always think about what to do. Always complete the thought.
Action: the action to take, should be one of ["search", "calculator", "web-browser"]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!`,
    },
  });

  console.log("Loaded agent.");

  const input = `What is the word of the day on merriam webster. What is the top result on google for that word`;

  console.log(`Executing with input "${input}"...`);

  const result = await executor.invoke({ input });

  console.log(`Got output ${JSON.stringify(result, null, 2)}`);
};

run().catch((error) => console.error(error));
