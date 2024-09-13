Instruções para Utilização do Projeto da Questão 6

Clone ou baixe o repositório referente à questão 6.
Abra o terminal (ou shell).
Navegue até o diretório onde o projeto foi salvo usando o comando cd seguido pelo caminho para a pasta do projeto.
Execute o comando para iniciar o container composto, baixar todas as imagens necessárias e realizar a raspagem. Use docker-compose up --build -d.
Nota: Para acompanhar o log em tempo real, execute o comando sem o -d no final. Se já tiver executado o comando acima e deseja ver os logs, use docker-compose logs python-app.
O container será executado e gerará um arquivo output.json, que será salvo automaticamente na pasta do projeto.
Para parar e remover o container, execute o comando docker-compose down.