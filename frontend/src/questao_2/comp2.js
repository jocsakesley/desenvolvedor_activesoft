import { useState } from "react";

function Comp2() {
    const [texto, setTexto] = useState('')
    return (
      <div>
        <input value={texto} onChange={event => setTexto(event.target.value)} />
      </div>
    );
  }
  
export default Comp2;
