import {
  ChatPromptTemplate,
  PromptTemplate,
  SystemMessagePromptTemplate,
  AIMessagePromptTemplate,
  HumanMessagePromptTemplate,
} from "@langchain/core/prompts";
import {
  AIMessage,
  HumanMessage,
  SystemMessage,
} from "@langchain/core/messages";

import { OpenAI } from "@langchain/openai";

const systemTemplate =
  "You are a helpful assistant that translates {input_language} to {output_language}.";
const humanTemplate = "{text}";

const chatPrompt = ChatPromptTemplate.fromMessages([
  ["system", systemTemplate],
  ["human", humanTemplate],
]);

// Format the messages
const formattedChatPrompt = await chatPrompt.formatMessages({
  input_language: "English",
  output_language: "French",
  text: "I love programming.",
});

const llm = new ChatOpenAI({
  model: "gpt-4o-mini",
  temperature: 0,
});



