import { useState } from "react";

function Comp1() {
    const [texto, setTexto] = useState('Texto')
    return (
      <div>
        {texto}
      </div>
    );
  }
  
export default Comp1;
