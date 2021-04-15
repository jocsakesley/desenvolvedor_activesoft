## Prova de SQL
A prova de SQL por simplicidade será feita em SQLite, seu banco de dados se encontra neste repositório, sendo ele
o arquivo `backend/chinook.db`, e caso você não possua um cliente SQLite, você pode encontrar um no seguinte link:
https://portableapps.com/apps/development/sqlite_database_browser_portable

Você pode encontrar um diagrama sobre o que tem disponível neste banco na imagem `chinook_db_schema.jpg`.

## Questões
1 - Utilizando o banco de dados fornecido no arquivo chinook.db prepare uma consulta que mostre o nome do artista e a quantidade albuns que ele lançou, ordenados por quem mais tem albuns.
    Colunas da resposta:
        ArtistName | QtdeAlbums

2 - Prepare uma consulta que traga os 20 clientes que mais gastaram. (Na tabela invoices há as compras feitas por cada cliente e seu valor)
    Colunas da resposta:
        CustomerFullName | Total

3 - Listar gênero musical com o valor vendido, e a quantidade de vendas.
    Colunas da resposta:
        Genre | TotalSold | QtdeSold

4 - Listar os albuns com preço, duração total em minutos, tamanho em MB.
    Colunas da resposta:
        AlbumTitle | Price | Duration_minutes | Size_MB

5 - Listar empregados com números de clientes, quanto cada um vendeu até o momento, gênero musical que mais vende em qtd (mais popular), e em valor (mais lucrativo).
    Colunas da resposta:
        EmployeeId | EmployeeFullName | QtdeCustomers | TotalSold | MostPopularGenre | MostLucrativeGenre

6 - Consulta que traga a lista de gêneros musicais com 12 colunas (Janeiro a Dezembro) com a qtd de faixas vendidas de um determinado ano a ser especificado num filtro.
    Colunas da resposta:
        GenreId | GenreName | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec

7 - Listar supervisores (aqueles funcionários a quem os outros se reportam)
    Há um funcionário que não se reporta a ninguém, este não precisará vir na listagem.
    Há diversos funcionários que ninguém se reporta a eles, este também não devem vir na listagem.
    Aos funcionários que virão na listagem, deverá ser exibida o nome deles, e 12 colunas de meses (Jan-Dez) com o valor que foi vendido por este, ou por alguma das pessoas que se reportam a ele. E outras 12 colunas de meses com a quantidade de faixas vendidas por ele, ou alguém que se reporte a ele.
    Esta tabela será utilizada para gerar gráficos de rendimento das equipes de cada supervisor.
    Deverá conter também uma coluna listando quantos clientes aquela equipe possui.
    Colunas da resposta:
        EmployeeId | EmployeeFullName | QtdeCustomers | 
        TotalSold_Jan | TotalSold_Feb | TotalSold_Mar | TotalSold_Apr | TotalSold_May | TotalSold_Jun |
        TotalSold_Jul | TotalSold_Aug | TotalSold_Sep | TotalSold_Oct | TotalSold_Nov | TotalSold_Dec |
        QtdeTracksSold_Jan | QtdeTracksSold_Feb | QtdeTracksSold_Mar | QtdeTracksSold_Apr | QtdeTracksSold_May | QtdeTracksSold_Jun |
        QtdeTracksSold_Jul | QtdeTracksSold_Aug | QtdeTracksSold_Sep | QtdeTracksSold_Oct | QtdeTracksSold_Nov | QtdeTracksSold_Dec

8 - Criar uma View que possibilite mostrar os dados da lista de supervisores mencionada acima (questão 7), e que possibilite ser filtrada por ano.
    Quero fazer a consulta simplesmente com `select * from vw_lista_supervisores where ano = 2015`.
    Atenção: A resolução dessa questão é a apresentação do script de criação dessa View. E não a criação dela dentro do banco de
        dados que se encontra neste repositório. Se o candidato apenas criar a view dentro do banco de dados mas não apresentar
        o script por escrito na prova, será considerado como não tendo respondido.
