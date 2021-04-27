import React from "react";
import { Context } from "./provider";


function Comp2() {
  const { text, setTexto } = React.useContext(Context)

  return (
    <div>
      <Context.Provider value={{ text, setTexto }}>
        <input type="text" onChange={event => setTexto({ text: event.target.value })} />
      </Context.Provider>
    </div >
  );
}

export default Comp2;
