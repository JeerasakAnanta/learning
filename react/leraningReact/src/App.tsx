import './App.css'
import { FC } from 'react'

let name: string = "Jeerasak";
let age: number | string;

age = 20;
age = "twenty"

const Hello: FC = () => {
  return (
    <>
      <h1> Hello  {name}</h1>
      <h1> Age  {age}</h1>
    </>
  )
}

function App() {
  const name: string = "hello";

  return (
    < >
      <h2> name: {name} </h2>
      <Hello />
    </>
  )
}

export default App
