Estrutura das Classes do Sistema

O sistema foi desenvolvido utilizando cinco classes, cada uma com uma função específica:

Animal (Classe principal): Guarda os dados básicos dos animais cadastrados, como nome, idade e informações sobre seu tutor.

Cachorro (Classe derivada): Utiliza as características herdadas de Animal e acrescenta informações e funcionalidades próprias dos cachorros.

Gato (Classe derivada): Aproveita os atributos da classe Animal e possui características e comportamentos específicos dos gatos.

Pássaro (Classe derivada): Também herda as propriedades de Animal, adicionando informações e ações relacionadas aos pássaros.

Clinica (Classe responsável pelo gerenciamento): Controla os animais registrados no sistema, permitindo realizar cadastros, consultas e listagens.

Diagrama de Classes

O diagrama apresenta a organização das classes e como elas estão conectadas. A classe Animal funciona como base para Cachorro, Gato e Pássaro, enquanto a classe Clinica administra os objetos cadastrados.


Aplicação dos Conceitos de POO

Encapsulamento: Os dados das classes são mantidos como privados, evitando o acesso direto aos atributos. Para consultar ou modificar essas informações, são utilizados getters, setters ou propriedades. Também são aplicadas verificações para evitar o armazenamento de valores incorretos.

Herança: As classes Cachorro, Gato e Pássaro aproveitam os atributos e métodos definidos em Animal. Para inicializar as características herdadas, é utilizado o comando super().__init__().

Polimorfismo: O método emitir_som() está presente na classe principal e é redefinido nas classes derivadas. Dessa forma, cada tipo de animal apresenta uma resposta diferente ao executar a mesma função.

Como Executar o Projeto

O sistema pode ser iniciado pelo arquivo main.py, utilizando o ambiente de desenvolvimento PyCharm e a linguagem Python.
