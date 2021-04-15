# Prova do backend

1 - A rota `/albums/` está retornando uma listagem dos albuns com os artistas do album, porém em alguns de nossos clientes
    que utilizam bancos armazenados em servidores próprios ela está muito lenta. Ao acompanhar as consultas SQL com um
    profiler foi detectado que está sendo realizado muitas consultas no banco e isso está causando a lentidão.
    Corrigir essa situação, explique o que causava esta situação e como foi resolvido.

2 - A rota `/genres/` também está com um problema de otimização de consultas SQL, sendo realizada várias consultas
    seguidas no banco causando lentidão. Resolva esta situação, explique o que causava o problema e o como a correção
    realizada resolve esse problema.

3 - A rota `/tracks/` está com problemas de performance. Nossos clientes não estão conseguindo utilizar ela para consultar
    a lista de faixas disponíveis. Mesmo em nosso banco de testes está demorando muito para carregar.
    Analisar, identificar o problema, corrigir e explicar a causa do problema e o que foi feito para solucionar.

4 - Crie uma rota `/customer_simplified/` para realizar o cadastro simplificado de clientes.
    Esta rota deverá aceitar somente os campos obrigatórios do cadastro, e deverá fazer a validação dos campos, e do
    e-mail conforme o padrão de funcionamento do Django-Rest-Framework.

5 - A rota `/playlists/` não está funcionando. Conserte seu funcionamento e explique o motivo que causou o erro no código.

6 - Crie uma API que receberá um objeto JSON em uma solicitação POST. Este objeto JSON conterá `customer_id` e `year`.
    Esta rota deverá validar os dados recebidos usando um serializer. E deverá fazer as seguintes validações:
    - `customer_id` é um número inteiro, e existe um cliente com este ID no banco.
    - `year` é um número inteiro, e está entre 1970 e 2100.
    Se os dados recebidos passarem na validação, o retorno dessa API deverá ser o total gasto por este cliente no
    ano determinado.

7 - Na rota `/report_data/` está retornando os dados de clientes através de consulta SQL pura. Porém, ao realizar
    uma consulta nessa rota, foi observado que o cliente de ID=1 (Luís Gonçalves) está retornando com FirstName=Jane e
    LastName=Peacock, enquanto isto, o novo campo criado FullName que é a concatenação dos dois, está retornando
    "Luís Gonçalves" corretamente. Ao realizar a consulta no cliente SQL, a consulta traz os dados corretamente,
    porém ao colocar a mesma consulta na API, os dados da API retornam errados. Identifique a causa do problema,
    explique o motivo de ter ocorrido, e corrija-o.
