import React from "react";
import { Context } from "./provider";

function Comp1() {

  const { text } = React.useContext(Context)
  return (
    <div>
      <h3>{text.text}</h3>
    </div>
  );
}

export default Comp1;
