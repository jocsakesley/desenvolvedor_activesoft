## Prova de SQL
A prova de SQL por simplicidade será feita em SQLite, seu banco de dados se encontra neste repositório, sendo ele
o arquivo `backend/chinook.db`, e caso você não possua um cliente SQLite, você pode encontrar um no seguinte link:
https://portableapps.com/apps/development/sqlite_database_browser_portable

Você pode encontrar um diagrama sobre o que tem disponível neste banco na imagem `chinook_db_schema.jpg`.

## Questões
1 - Utilizando o banco de dados fornecido no arquivo chinook.db prepare uma consulta que mostre o nome do artista e a quantidade albuns que ele lançou, ordenados por quem mais tem albuns.
    Colunas da resposta:
        ArtistName | QtdeAlbums

```sql
SELECT artists.name AS ArtistName, count(albums.title) AS QtdeAlbums 
FROM artists INNER JOIN albums ON artists.ArtistId = albums.ArtistId 
GROUP BY artists.name ORDER BY QtdeAlbums DESC;
```
2 - Prepare uma consulta que traga os 20 clientes que mais gastaram. (Na tabela invoices há as compras feitas por cada cliente e seu valor)
    Colunas da resposta:
        CustomerFullName | Total
```sql
SELECT customers.FirstName || ' ' || customers.LastName AS CustomerFullName, sum(invoices.Total) AS Total 
FROM customers INNER JOIN invoices ON customers.CustomerId = invoices.CustomerId 
GROUP BY CustomerFullName ORDER BY Total DESC LIMIT 20;
```

3 - Listar gênero musical com o valor vendido, e a quantidade de vendas.
    Colunas da resposta:
        Genre | TotalSold | QtdeSold

```sql
SELECT genres.name AS Genre, ROUND(sum(tracks.UnitPrice), 2) AS TotalSold, count(tracks.AlbumId) AS QtdeSold 
FROM genres INNER JOIN tracks ON genres.GenreId = tracks.GenreId GROUP BY Genre;
```

4 - Listar os albuns com preço, duração total em minutos, tamanho em MB.
    Colunas da resposta:
        AlbumTitle | Price | Duration_minutes | Size_MB

```sql
SELECT albums.Title AS AlbumTitle, sum(tracks.UnitPrice) AS Price, sum(round(tracks.Milliseconds/1000.0/60.0, 1)) AS Duration_minutes, sum(round(tracks.Bytes/1024.0/1024.0, 2)) AS Size_MB 
FROM albums INNER JOIN tracks ON albums.AlbumId = tracks.AlbumId GROUP BY AlbumTitle;
```
5 - Listar empregados com números de clientes, quanto cada um vendeu até o momento, gênero musical que mais vende em qtd (mais popular), e em valor (mais lucrativo).
    Colunas da resposta:
        EmployeeId | EmployeeFullName | QtdeCustomers | TotalSold | MostPopularGenre | MostLucrativeGenre
```sql
SELECT employees.EmployeeId, employees.FirstName || ' ' || employees.LastName AS EmployeeFullName,
count(DISTINCT customers.CustomerId) AS QtdeCustomers, round(sum(invoice_items.UnitPrice), 2) AS TotalSold,
(SELECT qtdgenre.name from (SELECT employees.EmployeeId,genres.Name,count(invoice_items.InvoiceLineId) AS qtdSold
FROM employees LEFT JOIN customers ON employees.EmployeeId = customers.SupportRepId 
LEFT JOIN invoices ON customers.CustomerId = invoices.CustomerId 
LEFT JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId 
LEFT JOIN tracks ON invoice_items.TrackId = tracks.TrackId 
LEFT JOIN genres ON tracks.GenreId = genres.GenreId
GROUP BY employees.EmployeeId, genres.name) AS qtdgenre
WHERE qtdgenre.EmployeeId = employees.EmployeeId AND qtdgenre.qtdSold = (SELECT max(maxqtd.qtdSold) 
FROM (SELECT employees.EmployeeId, genres.Name, count(invoice_items.InvoiceLineId) as qtdSold
FROM employees 
LEFT JOIN customers ON employees.EmployeeId = customers.SupportRepId 
LEFT JOIN invoices ON customers.CustomerId = invoices.CustomerId 
LEFT JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId 
LEFT JOIN tracks ON invoice_items.TrackId = tracks.TrackId 
LEFT JOIN genres ON tracks.GenreId = genres.GenreId
GROUP BY employees.EmployeeId, genres.name) AS maxqtd
WHERE maxqtd.EmployeeId = qtdgenre.EmployeeId)) as mostPopularGenre,
(SELECT totalgenre.name FROM (SELECT employees.EmployeeId, genres.Name, round(sum(invoice_items.UnitPrice), 2) AS TotalSold
FROM employees 
LEFT JOIN customers ON employees.EmployeeId = customers.SupportRepId 
LEFT JOIN invoices ON customers.CustomerId = invoices.CustomerId 
LEFT JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId 
LEFT JOIN tracks ON invoice_items.TrackId = tracks.TrackId 
LEFT JOIN genres ON tracks.GenreId = genres.GenreId
GROUP BY employees.EmployeeId, genres.name) AS totalgenre
WHERE totalgenre.EmployeeId = employees.EmployeeId
AND totalgenre.totalSold = (SELECT max(maxgenre.totalSold) FROM
(SELECT employees.EmployeeId, genres.Name, round(sum(invoice_items.UnitPrice), 2) AS TotalSold
FROM employees LEFT JOIN customers ON employees.EmployeeId = customers.SupportRepId 
LEFT JOIN invoices ON customers.CustomerId = invoices.CustomerId 
LEFT JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId 
LEFT JOIN tracks ON invoice_items.TrackId = tracks.TrackId 
LEFT JOIN genres ON tracks.GenreId = genres.GenreId
GROUP BY employees.EmployeeId, genres.name) AS maxgenre
WHERE totalgenre.EmployeeId = maxgenre.EmployeeId)) as mostLucrativeGenre
FROM employees
LEFT JOIN customers ON employees.EmployeeId = customers.SupportRepId
LEFT JOIN invoices ON customers.CustomerId = invoices.CustomerId 
LEFT JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
GROUP BY employees.EmployeeId;
```

6 - Consulta que traga a lista de gêneros musicais com 12 colunas (Janeiro a Dezembro) com a qtd de faixas vendidas de um determinado ano a ser especificado num filtro.
    Colunas da resposta:
        GenreId | GenreName | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct | Nov | Dec

```sql
SELECT pivot.GenreId AS GenreId,  pivot.name AS GenreName, 
count(CASE WHEN pivot.Month = "01" THEN pivot.TrackId END) AS Jan, 
count(CASE WHEN pivot.Month = "02" THEN pivot.TrackId END) AS Feb, 
count(CASE WHEN pivot.Month = "03" THEN pivot.TrackId END) AS Mar, 
count(CASE WHEN pivot.Month = "04" THEN pivot.TrackId END) AS Apr, 
count(CASE WHEN pivot.Month = "05" THEN pivot.TrackId END) AS May, 
count(CASE WHEN pivot.Month = "06" THEN pivot.TrackId END) AS Jun, 
count(CASE WHEN pivot.Month = "07" THEN pivot.TrackId END) AS Jul, 
count(CASE WHEN pivot.Month = "08" THEN pivot.TrackId END) AS Aug, 
count(CASE WHEN pivot.Month = "09" THEN pivot.TrackId END) AS Sep, 
count(CASE WHEN pivot.Month = "10" THEN pivot.TrackId END) AS Out, 
count(CASE WHEN pivot.Month = "11" THEN pivot.TrackId END) AS Nov, 
count(CASE WHEN pivot.Month = "12" THEN pivot.TrackId END) AS Dec 
FROM (SELECT genres.GenreId, genres.name, strftime("%m", invoices.InvoiceDate) AS Month, strftime("%Y", invoices.InvoiceDate) AS Year, tracks.TrackId from genres 
INNER JOIN tracks ON genres.GenreId = tracks.GenreId 
INNER JOIN invoice_items ON tracks.TrackId = invoice_items.TrackId
INNER JOIN invoices ON invoice_items.InvoiceId = invoices.InvoiceId) AS pivot WHERE pivot.Year = '2010' GROUP BY pivot.GenreId, pivot.name;
```
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

```sql
SELECT pivot.EmployeeId, pivot.EmployeeFullName,
sum(case when pivot.Month = "01" then pivot.TotalSOldMonth end) TotalSold_Jan, 
sum(case when pivot.Month = "02" then pivot.TotalSOldMonth end) TotalSold_Feb, 
sum(case when pivot.Month = "03" then pivot.TotalSOldMonth end) TotalSold_Mar, 
sum(case when pivot.Month = "04" then pivot.TotalSOldMonth end) TotalSold_Apr, 
sum(case when pivot.Month = "05" then pivot.TotalSOldMonth end) TotalSold_May, 
sum(case when pivot.Month = "06" then pivot.TotalSOldMonth end) TotalSold_Jun, 
sum(case when pivot.Month = "07" then pivot.TotalSOldMonth end) TotalSold_Jul, 
sum(case when pivot.Month = "08" then pivot.TotalSOldMonth end) TotalSold_Aug, 
sum(case when pivot.Month = "09" then pivot.TotalSOldMonth end) TotalSold_Sep, 
sum(case when pivot.Month = "10" then pivot.TotalSOldMonth end) TotalSold_Oct, 
sum(case when pivot.Month = "11" then pivot.TotalSOldMonth end) TotalSold_Nov, 
sum(case when pivot.Month = "12" then pivot.TotalSOldMonth end) TotalSold_Dec,
sum(case when pivot.Month = "01" then pivot.CountTracks end) QtdeTracksSold_Jan, 
sum(case when pivot.Month = "02" then pivot.CountTracks end) QtdeTracksSold_Feb, 
sum(case when pivot.Month = "03" then pivot.CountTracks end) QtdeTracksSold_Mar, 
sum(case when pivot.Month = "04" then pivot.CountTracks end) QtdeTracksSold_Apr, 
sum(case when pivot.Month = "05" then pivot.CountTracks end) QtdeTracksSold_May, 
sum(case when pivot.Month = "06" then pivot.CountTracks end) QtdeTracksSold_Jun, 
sum(case when pivot.Month = "07" then pivot.CountTracks end) QtdeTracksSold_Jul, 
sum(case when pivot.Month = "08" then pivot.CountTracks end) QtdeTracksSold_Aug, 
sum(case when pivot.Month = "09" then pivot.CountTracks end) QtdeTracksSold_Sep, 
sum(case when pivot.Month = "10" then pivot.CountTracks end) QtdeTracksSold_Oct, 
sum(case when pivot.Month = "11" then pivot.CountTracks end) QtdeTracksSold_Nov, 
sum(case when pivot.Month = "12" then pivot.CountTracks end) QtdeTracksSold_Dec  
FROM 
(SELECT employees.EmployeeId, employees.FirstName || " " || employees.LastName AS EmployeeFullName, employees_sold.Month, employees_sold.TotalSoldMonth, employees_sold.CountTracks, employees_sold.Year FROM employees 
INNER JOIN (SELECT employees.ReportsTo, employees.EmployeeId, strftime('%m', invoices.InvoiceDate) AS Month, strftime('%Y', invoices.InvoiceDate) AS Year,
 round(sum(invoice_items.UnitPrice),2) AS TotalSoldMonth, count(tracks.TrackId) AS CountTracks FROM employees 
LEFT JOIN customers ON employees.EmployeeId = customers.SupportRepId
LEFT JOIN invoices ON customers.CustomerId = invoices.CustomerId
LEFT JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
LEFT JOIN tracks ON invoice_items.TrackId = tracks.TrackId WHERE employees.ReportsTo IN (SELECT employees.EmployeeId FROM employees
WHERE employees.ReportsTo IS NOT NULL AND employees.EmployeeId IN (SELECT employees.ReportsTo FROM employees)) 
GROUP BY strftime('%m', invoices.InvoiceDate), employees.EmployeeId) AS employees_sold 
ON employees.EmployeeId = employees_sold.ReportsTo GROUP BY employees.EmployeeId, employees_sold.Month) AS pivot GROUP BY pivot.EmployeeId;
```

8 - Criar uma View que possibilite mostrar os dados da lista de supervisores mencionada acima (questão 7), e que possibilite ser filtrada por ano.
    Quero fazer a consulta simplesmente com `select * from vw_lista_supervisores where ano = 2015`.
    Atenção: A resolução dessa questão é a apresentação do script de criação dessa View. E não a criação dela dentro do banco de
        dados que se encontra neste repositório. Se o candidato apenas criar a view dentro do banco de dados mas não apresentar
        o script por escrito na prova, será considerado como não tendo respondido.
```sql
CREATE VIEW vw_lista_supervisores AS 
SELECT pivot.EmployeeId, pivot.EmployeeFullName, pivot.Year AS ano,
sum(case when pivot.Month = "01" then pivot.TotalSOldMonth end) TotalSold_Jan, 
sum(case when pivot.Month = "02" then pivot.TotalSOldMonth end) TotalSold_Feb, 
sum(case when pivot.Month = "03" then pivot.TotalSOldMonth end) TotalSold_Mar, 
sum(case when pivot.Month = "04" then pivot.TotalSOldMonth end) TotalSold_Apr, 
sum(case when pivot.Month = "05" then pivot.TotalSOldMonth end) TotalSold_May, 
sum(case when pivot.Month = "06" then pivot.TotalSOldMonth end) TotalSold_Jun, 
sum(case when pivot.Month = "07" then pivot.TotalSOldMonth end) TotalSold_Jul, 
sum(case when pivot.Month = "08" then pivot.TotalSOldMonth end) TotalSold_Aug, 
sum(case when pivot.Month = "09" then pivot.TotalSOldMonth end) TotalSold_Sep, 
sum(case when pivot.Month = "10" then pivot.TotalSOldMonth end) TotalSold_Oct, 
sum(case when pivot.Month = "11" then pivot.TotalSOldMonth end) TotalSold_Nov, 
sum(case when pivot.Month = "12" then pivot.TotalSOldMonth end) TotalSold_Dec,
sum(case when pivot.Month = "01" then pivot.CountTracks end) QtdeTracksSold_Jan, 
sum(case when pivot.Month = "02" then pivot.CountTracks end) QtdeTracksSold_Feb, 
sum(case when pivot.Month = "03" then pivot.CountTracks end) QtdeTracksSold_Mar, 
sum(case when pivot.Month = "04" then pivot.CountTracks end) QtdeTracksSold_Apr, 
sum(case when pivot.Month = "05" then pivot.CountTracks end) QtdeTracksSold_May, 
sum(case when pivot.Month = "06" then pivot.CountTracks end) QtdeTracksSold_Jun, 
sum(case when pivot.Month = "07" then pivot.CountTracks end) QtdeTracksSold_Jul, 
sum(case when pivot.Month = "08" then pivot.CountTracks end) QtdeTracksSold_Aug, 
sum(case when pivot.Month = "09" then pivot.CountTracks end) QtdeTracksSold_Sep, 
sum(case when pivot.Month = "10" then pivot.CountTracks end) QtdeTracksSold_Oct, 
sum(case when pivot.Month = "11" then pivot.CountTracks end) QtdeTracksSold_Nov, 
sum(case when pivot.Month = "12" then pivot.CountTracks end) QtdeTracksSold_Dec  
FROM 
(SELECT employees.EmployeeId, employees.FirstName || " " || employees.LastName AS EmployeeFullName, employees_sold.Month, employees_sold.TotalSoldMonth, employees_sold.CountTracks, employees_sold.Year FROM employees 
INNER JOIN (SELECT employees.ReportsTo, employees.EmployeeId, strftime('%m', invoices.InvoiceDate) AS Month, strftime('%Y', invoices.InvoiceDate) AS Year,
 round(sum(invoice_items.UnitPrice),2) AS TotalSoldMonth, count(tracks.TrackId) AS CountTracks FROM employees 
LEFT JOIN customers ON employees.EmployeeId = customers.SupportRepId
LEFT JOIN invoices ON customers.CustomerId = invoices.CustomerId
LEFT JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
LEFT JOIN tracks ON invoice_items.TrackId = tracks.TrackId WHERE employees.ReportsTo IN (SELECT employees.EmployeeId FROM employees
WHERE employees.ReportsTo IS NOT NULL AND employees.EmployeeId IN (SELECT employees.ReportsTo FROM employees)) 
GROUP BY strftime('%m', invoices.InvoiceDate), employees.EmployeeId) AS employees_sold 
ON employees.EmployeeId = employees_sold.ReportsTo GROUP BY employees.EmployeeId, employees_sold.Month) AS pivot GROUP BY pivot.EmployeeId, pivot.Year;
```