> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncode/pt-BR.md)

`CLIP Text Encode (CLIPTextEncode)` atua como um tradutor, convertendo suas descrições de texto em um formato que a IA pode entender. Isso ajuda a IA a interpretar sua entrada e gerar a imagem desejada.

Pense nisso como se estivesse se comunicando com um artista que fala um idioma diferente. O modelo CLIP, treinado em vastos pares de imagem-texto, preenche essa lacuna convertendo suas descrições em "instruções" que o modelo de IA pode seguir.

## Entradas

| Parâmetro | Tipo de Dados | Método de Entrada | Padrão | Intervalo | Descrição |
|-----------|-----------|--------------|---------|--------|-------------|
| text | STRING | Entrada de Texto | Vazio | Qualquer texto | Insira a descrição (prompt) para a imagem que deseja criar. Suporta entrada de múltiplas linhas para descrições detalhadas. |
| clip | CLIP | Seleção de Modelo | Nenhum | Modelos CLIP carregados | Selecione o modelo CLIP a ser usado ao traduzir sua descrição em instruções para o modelo de IA. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| CONDITIONING | CONDITIONING | As "instruções" processadas da sua descrição que orientam o modelo de IA ao gerar uma imagem. |

## Recursos do Prompt

### Modelos de Embedding

Modelos de embedding permitem que você aplique efeitos ou estilos artísticos específicos. Os formatos suportados incluem `.safetensors`, `.pt` e `.bin`. Para usar um modelo de embedding:

1. Coloque o arquivo na pasta `ComfyUI/models/embeddings`.
2. Referencie-o em seu texto usando `embedding:nome_do_modelo`.

Exemplo: Se você tiver um modelo chamado `EasyNegative.pt` em sua pasta `ComfyUI/models/embeddings`, então pode usá-lo assim:

```
worst quality, embedding:EasyNegative, bad quality
```

**IMPORTANTE**: Ao usar modelos de embedding, verifique se o nome do arquivo corresponde e é compatível com a arquitetura do seu modelo. Por exemplo, um embedding projetado para SD1.5 não funcionará corretamente para um modelo SDXL.

### Ajuste de Peso do Prompt

Você pode ajustar a importância de certas partes da sua descrição usando parênteses. Por exemplo:

- `(beautiful:1.2)` aumenta o peso de "beautiful".
- `(beautiful:0.8)` diminui o peso de "beautiful".
- Parênteses simples `(beautiful)` aplicarão um peso padrão de 1.1.

Você pode usar os atalhos de teclado `ctrl + seta para cima/baixo` para ajustar pesos rapidamente. O tamanho do passo de ajuste de peso pode ser modificado nas configurações.

Se você quiser incluir parênteses literais em seu prompt sem alterar o peso, pode escapar deles usando uma barra invertida, por exemplo: `\(palavra\)`.

### Prompts Dinâmicos/Wildcard

Use `{}` para criar prompts dinâmicos. Por exemplo, `{dia|noite|manhã}` selecionará aleatoriamente uma opção cada vez que o prompt for processado.

Se você quiser incluir chaves literais em seu prompt sem acionar o comportamento dinâmico, pode escapar delas usando uma barra invertida, por exemplo: `\{palavra\}`.

### Comentários em Prompts

Você pode adicionar comentários que são excluídos do prompt usando:

- `//` para comentar uma única linha.
- `/* */` para comentar uma seção ou múltiplas linhas.

Exemplo:

```
// esta linha é excluída do prompt.
uma paisagem bonita, /* esta parte é ignorada */ alta qualidade
```
