# gerenciador-de-senhas
Pequeno projeto de um Gerenciador de Senhas em Python, com uso de SQL, Tkinter.

Converti o resultado final da aplicação em um arquivo executável com ícone personalizado e com todas as funções requeridas funcionando. 
O aplicativo necessita, primeiramente, de um acesso com senha, que já está predefinida no "Gerenciador_de_Senhas.py". A partir do acesso com senha o usuário é capaz de registrar perfis de seus serviços preferidos, como Youtube, Facebook, Twitter, seus jogos ou plataformas preferidas. 

Login:

(Senha MESTRE - 123)
![](https://user-images.githubusercontent.com/56975955/75189706-83868f00-572d-11ea-9498-b67b03e6d4db.png)

Inserção de Serviços:

![](https://user-images.githubusercontent.com/56975955/75190312-cc8b1300-572e-11ea-8812-c3a2c4109d3f.png)

Listagem dos Serviços:

![](https://user-images.githubusercontent.com/56975955/75190339-dad92f00-572e-11ea-84de-06d14b3edb65.png)

No momento em que ele envia um serviço, ele fica registrado dentro de um arquivo gerado automaticamente, chamado "passwords.db".

Restaurar Serviço:

![](https://user-images.githubusercontent.com/56975955/75190356-e6c4f100-572e-11ea-9184-7be472cb0672.png)
![](https://user-images.githubusercontent.com/56975955/75190377-ef1d2c00-572e-11ea-9e53-055b80f58b14.png)

O programa é capaz de ler as informações inseridas e com posterior requisição de "Recuperar Senha", dando como parâmetro o Serviço desejado, é mostrado em tela o Usuário e a Senha anteriormente cadastrados.

Gerar senha aleatória:

![](https://user-images.githubusercontent.com/56975955/75190396-f6dcd080-572e-11ea-93f3-f87ebb112819.png)

Além das funções de "Inserir Serviço", "Listar Serviços" e "Recuperar Senhas", o programa também gera uma senha aleatória com 12 dígitos, maiúsculos e números.

