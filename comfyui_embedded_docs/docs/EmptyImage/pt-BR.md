> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyImage/pt-BR.md)

## Descrição da Função

O nó EmptyImage é utilizado para criar imagens em branco com dimensões e cores especificadas. Ele pode gerar imagens de fundo de cor sólida, comumente usadas como pontos de partida ou imagens de fundo para fluxos de trabalho de processamento de imagens.

## Princípio de Funcionamento

Assim como um pintor prepara uma tela em branco antes de começar a criar, o nó EmptyImage fornece uma "tela digital". Você pode especificar o tamanho da tela (largura e altura), escolher a cor base da tela e até mesmo preparar várias telas com as mesmas especificações de uma só vez. Este nó é como uma loja inteligente de materiais de arte que pode criar telas padronizadas que atendem perfeitamente às suas necessidades de tamanho e cor.

## Entradas

| Nome do Parâmetro | Tipo de Dado | Descrição |
|-------------------|--------------|-----------|
| `largura` | INT | Define a largura da imagem gerada (em pixels), determinando as dimensões horizontais da tela |
| `altura` | INT | Define a altura da imagem gerada (em pixels), determinando as dimensões verticais da tela |
| `tamanho_do_lote` | INT | O número de imagens a serem geradas de uma vez, usado para criação em lote de imagens com as mesmas especificações |
| `cor` | INT | A cor de fundo da imagem. Você pode inserir configurações de cor hexadecimal, que serão convertidas automaticamente para decimal |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `image` | IMAGE | O tensor da imagem em branco gerada, formatado como [batch_size, height, width, 3], contendo três canais de cor RGB |

## Valores de Referência de Cores Comuns

Como a entrada de cor atual deste nó não é amigável, com todos os valores de cor sendo convertidos para decimal, aqui estão alguns valores de cor comuns que podem ser usados diretamente para aplicação rápida.

| Nome da Cor | Valor Hexadecimal |
|-------------|-------------------|
| Preto      | 0x000000         |
| Branco     | 0xFFFFFF         |
| Vermelho   | 0xFF0000         |
| Verde      | 0x00FF00         |
| Azul       | 0x0000FF         |
| Amarelo    | 0xFFFF00         |
| Ciano      | 0x00FFFF         |
| Magenta    | 0xFF00FF         |
| Laranja    | 0xFF8000         |
| Roxo       | 0x8000FF         |
| Rosa       | 0xFF80C0         |
| Marrom     | 0x8B4513         |
| Cinza Escuro | 0x404040       |
| Cinza Claro | 0xC0C0C0        |
| Azul Marinho | 0x000080       |
| Verde Escuro | 0x008000       |
| Vermelho Escuro | 0x800000     |
| Dourado    | 0xFFD700         |
| Prata      | 0xC0C0C0         |
| Bege       | 0xF5F5DC         |