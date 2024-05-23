# abrindo o arquivo CSV
with open("meus_livros.csv",'w') as fp:
    # títulos das colunas
    fp.write("Título, Autor, Ano de Publicação, Nº páginas\n")

    # escrevendo as informações dos livros
    fp.write("Misbehaving:A construção da economia comportamental, Richard H. Taller,2015,448\n")
    fp.write("Curso Intensivo de Python, Eric Matthes, 2016, 793\n")
    fp.write("Teoria geral do emprego do juro e da moeda,John Maynard Keynes,1936, 542\n")
    fp.write("Guia prático e visual: HTML5 e CSS3,Elizabeth Castro-Bruce Hyslop, 2013, 552\n")
    fp.write("CSS: Grid Layout, Maujor,2017,164\n")
    fp.write("Código limpo: Habilidades práticas do Agile Software,Robert C. Martin, 2009,425\n")
    fp.write("O guia definitivo do mochileiro das galáxias,Douglas Adams, 2020,784\n")
    fp.write("Pythonn para todos: Explorando dados com Python 3, Charles R. Severance, 2015, 260\n")
    fp.write("A Arte da Estatística: Como aprender a partir de dados, David Spiegelhalter,2022, 352\n")
    fp.write("Estatística: o que é para que serve e como funciona, Charles Wheelan, 2016,328\n")

print("Arquivos 'meus_livros.csv' criado com sucesso")
