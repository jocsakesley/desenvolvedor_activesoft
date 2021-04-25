# Prova do backend

1 - A rota `/albums/` está retornando uma listagem dos albuns com os artistas do album, porém em alguns de nossos clientes
    que utilizam bancos armazenados em servidores próprios ela está muito lenta. Ao acompanhar as consultas SQL com um
    profiler foi detectado que está sendo realizado muitas consultas no banco e isso está causando a lentidão.
    Corrigir essa situação, explique o que causava esta situação e como foi resolvido.

> Ao fazer uma consulta do tipo Album.objects.all() em um modelo que possui chave estrangeira, o Django faz consultas recursivas para recuperar esse dado de cada registro. Para esses casos o Django oferece um Queryset .select_related('<Nome_da_chave>'), que em uma única consulta com JOIN entre as tabelas, ele consegue recuperar todos os dados de uma vez.

2 - A rota `/genres/` também está com um problema de otimização de consultas SQL, sendo realizada várias consultas
    seguidas no banco causando lentidão. Resolva esta situação, explique o que causava o problema e o como a correção
    realizada resolve esse problema.

> Para relacionamentos reversos e campos Many to Many o Django oferece o .prefetch_related('<Nome_da_chave>') que nesse caso faz duas consultas, uma para retornar todos os gêneros e outra para retornar todas as "tracks" usando o related_name "tracks" atribuído para "genre" no model "Track".

3 - A rota `/tracks/` está com problemas de performance. Nossos clientes não estão conseguindo utilizar ela para consultar
    a lista de faixas disponíveis. Mesmo em nosso banco de testes está demorando muito para carregar.
    Analisar, identificar o problema, corrigir e explicar a causa do problema e o que foi feito para solucionar.

> A rota `/tracks/` estava com o mesmo problema da questão 1, com consultas recursivas que estavam gerando lentidão, dessa forma foi implementado o .select_related("album"), removidos os campos de filtro na consulta, e implementados os filtros através do "filters_backends" e "search_fields"

4 - Crie uma rota `/customer_simplified/` para realizar o cadastro simplificado de clientes.
    Esta rota deverá aceitar somente os campos obrigatórios do cadastro, e deverá fazer a validação dos campos, e do
    e-mail conforme o padrão de funcionamento do Django-Rest-Framework.

> A rota pedida foi implementada em `chinook/urls.py`, a qual recebe uma view `CustomerSimplifiedAPIView` implementada em `chinook/views.py`, que por sua vez herda de `APIView` os métodos `get()` e `post()` em que foram implemantadas as funções de recuperar e enviar os dados previamente serializados por `CustomerSimplifiedSerializer`. 

5 - A rota `/playlists/` não está funcionando. Conserte seu funcionamento e explique o motivo que causou o erro no código.

> Em `serializers.py`, o campo `fields` da classe `Meta` de `PlaylistSerializer` precisa receber um valor em forma de tupla. Foi adicionada uma vírgula após o nome do campo dentro dos parênteses e a rota voltou a funcionar normalmente.

6 - Crie uma API que receberá um objeto JSON em uma solicitação POST. Este objeto JSON conterá `customer_id` e `year`.
    Esta rota deverá validar os dados recebidos usando um serializer. E deverá fazer as seguintes validações:
    - `customer_id` é um número inteiro, e existe um cliente com este ID no banco.
    - `year` é um número inteiro, e está entre 1970 e 2100.
    Se os dados recebidos passarem na validação, o retorno dessa API deverá ser o total gasto por este cliente no
    ano determinado.

> Foi criada uma rota com o nome `/total_per_customer/` que recebe a view `TotalPerCustomerAPIView` que herda de `APIView`, em que foi implementado o método `post()` que recebe os dados do `request.data` e envia para o serializador `TotalPerCustomerSerializer` que valida se os campos são inteiros, se o ID existe no banco e se o ano está entre 1970 e 2100. Aṕos isso a view verifica se os dados são válidos, se sim é feita uma consulta no modelo Invoices filtrando pelo ID e pelo ano, agregando os valores da coluna `total` em uma soma e passando para outro serializador `CustomerInvoiceSerializer` que monta a resposta, senão é aprensentado um erro com status code 400.

7 - Na rota `/report_data/` está retornando os dados de clientes através de consulta SQL pura. Porém, ao realizar
    uma consulta nessa rota, foi observado que o cliente de ID=1 (Luís Gonçalves) está retornando com FirstName=Jane e
    LastName=Peacock, enquanto isto, o novo campo criado FullName que é a concatenação dos dois, está retornando
    "Luís Gonçalves" corretamente. Ao realizar a consulta no cliente SQL, a consulta traz os dados corretamente,
    porém ao colocar a mesma consulta na API, os dados da API retornam errados. Identifique a causa do problema,
    explique o motivo de ter ocorrido, e corrija-o.

> O problema ocorre devido à ambiguidade dos nomes dos campos das colunas das duas tabelas, que são idênticos. Para resolver o problema foi colocado explicitamente na consulta os valores esperados para `customers.[FirstName]` e `customers.[LastName]`.