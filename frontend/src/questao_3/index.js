import { useState } from "react";

function Questao3() {



  const [valor, setValor] = useState("")

  let value;

  if (valor.length > 0) {
    sessionStorage.setItem("storage", valor);
    value = sessionStorage.getItem("storage")
  } else if (valor.length === 0) {
    sessionStorage.setItem("storage2", valor);
    value = sessionStorage.getItem("storage")
  }



  return (
    <div>
      <h1>Questão 3</h1>
      <input value={value} onChange={event => setValor(event.target.value)} />
    </div>
  );
}

export default Questao3;
