import { useState } from 'react'
import NotaField from './NotaField'

function Questao1() {
    const [nota, setNota] = useState(3)
    return (
      <div>
        <h1>Questão 1</h1>
        <NotaField maxNota={5} value={nota} onChange={setNota} />
      </div>
    );
  }
  
export default Questao1;
