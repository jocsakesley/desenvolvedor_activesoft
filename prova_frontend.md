# A prova de frontend

1 - Transforme o componente `NotaField` em um seletor de estrelhinhas para dar uma nota. Perceba o funcionamento dos
    props e mantenha sua API atual, modificando apenas a forma de exibição.

2 - No diretório da questão 2 tem dois componentes (comp1 e comp2), um deles é um campo para edição de uma string e
    o outro é simplesmente uma exibição do campo. Nenhum dos dois componentes possui props, e nem deverá ser adicionado.
    Utilizando o ContextAPI faça com que o valor alterado no campo que está no `comp2` altere o valor sendo exibido
    pelo `comp1`.

3 - O componente da questão 3 possui apenas um simples campo de texto. Ajuste este componente para que mesmo que a página
    seja atualizada o valor seja mantido. Se for atualizada a página, o valor deverá ser mantido, porém se for aberta
    outra aba, não deve ser ter o mesmo valor. Desse modo deve ser possível ter duas abas na mesma página, e cada uma
    possuir um valor diferente e mesmo atualizando ambas as páginas os valores de cada uma não serão perdidos.

4 - Nesse componente há uma promise no formato tradicional. Altere a implementação da função `chamarPromise` para a
    nova sintaxe async/await.
    - A função `acaoBotao` não deve ter nenhuma linha de código alterada e deverá continuar funcionando como funciona hoje.
    - A função `acaoBota2` deverá ser atualizada para utilizar a nova sintaxe de async/await.

5 - Há um componente chamado `compRodape`, porém ao ser renderizado no local atual da árvore, ele acabou aparecendo
    no lugar errado da estrutura do HTML. Alterando apenas o arquivo `compRodape`, faça com que este componente seja
    renderizado diretamente dentro da tag body ao final do arquivo. De modo que visualmente este componente irá aparecer
    após a questão 6 (no final da tela), porém no código ele continuará sendo chamado no meio do código.
    Atenção: Só é permitido ser alterado o arquivo `compRodape` para resolver esta questão.

6 - Aqui temos um exemplo de formulário para cadastro de revistas com título e autor. Perceba que há restrições sobre
    o tamanho do campo, e sobre a obrigatoriedade dos campos. Utilizando o YUP para realizar as validações, crie uma
    validação que caso o título contenha a palavra "pop" ele gere uma mensagem de erro, tal qual ocorreria se
    qualquer outra validação fosse estourada.
