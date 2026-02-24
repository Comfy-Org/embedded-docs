> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyImage/pt-BR.md)

## Descrição da Função

O nó EmptyImage é utilizado para criar imagens em branco com dimensões e cores especificadas. Ele pode gerar imagens de fundo com cores sólidas, comumente usadas como pontos de partida ou imagens de fundo para fluxos de trabalho de processamento de imagem.

## Princípio de Funcionamento

Assim como um pintor prepara uma tela em branco antes de começar a criar, o nó EmptyImage fornece a você uma "tela digital". Você pode especificar o tamanho da tela (largura e altura), escolher a cor de base da tela e até mesmo preparar várias telas com as mesmas especificações de uma só vez. Este nó funciona como uma loja de materiais artísticos inteligente, capaz de criar telas padronizadas que atendem perfeitamente aos seus requisitos de tamanho e cor.

## Entradas

| Nome do Parâmetro | Tipo de Dados | Descrição |
|----------------|-----------|-------------|
| `width` | INT | Define a largura da imagem gerada (em pixels), determinando as dimensões horizontais da tela |
| `height` | INT | Define a altura da imagem gerada (em pixels), determinando as dimensões verticais da tela |
| `batch_size` | INT | O número de imagens a serem geradas de uma vez, usado para a criação em lote de imagens com as mesmas especificações |
| `color` | INT | A cor de fundo da imagem. Você pode inserir configurações de cor hexadecimal, que serão automaticamente convertidas para decimal |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `image` | IMAGE | O tensor da imagem em branco gerada, formatado como [batch_size, altura, largura, 3], contendo os três canais de cor RGB |

## Valores de Referência de Cores Comuns

Como a entrada de cor atual para este nó não é amigável ao usuário, com todos os valores de cor sendo convertidos para decimal, aqui estão alguns valores de cor comuns que podem ser usados diretamente para aplicação rápida.

| Nome da Cor | Valor Hexadecimal |
|------------|-------------------|
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
| Cinza Claro | 0xC0C0C0       |
| Azul Marinho | 0x000080       |
| Verde Escuro | 0x008000       |
| Vermelho Escuro | 0x800000   |
| Dourado    | 0xFFD700         |
| Prata      | 0xC0C0C0         |
| Bege       | 0xF5F5DC         |
