import Comp1 from './comp1'
import Comp2 from './comp2'
import Provider from './provider';

function Questao2() {
  return (
    <div>
      <h1>Questão 2</h1>
      <Provider>
        <Comp1 />
        <Comp2 />
      </Provider>
    </div>
  );
}

export default Questao2;
