
function chamarPromise (x){
  let myPromise = new Promise(function(myResolve, myReject) {
    if (x > 7) {
      myResolve('Deu certo')
    } else {
      myReject('Deu errado')
    }
  })
  return myPromise
}

function acaoBotao(){
  chamarPromise(8).then(res => alert(res)).catch(err => alert(err))
}

function acaoBotao2(){
  chamarPromise(8).then(res => alert(res)).catch(err => alert(err))
}

function Questao4() {
    return (
      <div>
        <h1>Questão 4</h1>
        <button onClick={acaoBotao}>Ativar</button>
        <button onClick={acaoBotao2}>Ativar2</button>
      </div>
    );
  }
  
export default Questao4;
