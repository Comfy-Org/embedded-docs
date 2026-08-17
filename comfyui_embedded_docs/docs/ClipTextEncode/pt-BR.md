# Codificação de Texto CLIP (Prompt)

`CLIP Text Encode (CLIPTextEncode)` atua como um tradutor, convertendo suas descrições em texto em um formato que a IA pode entender. Isso ajuda a IA a interpretar sua entrada e gerar a imagem desejada.

Pense nisso como se estivesse se comunicando com um artista que fala um idioma diferente. O modelo CLIP, treinado em vastos pares de imagem-texto, preenche essa lacuna ao converter suas descrições em "instruções" que o modelo de IA pode seguir.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `text` | O texto a ser codificado. Suporta entrada de múltiplas linhas e prompts dinâmicos. | STRING | Sim | Qualquer texto |
| `clip` | O modelo CLIP usado para codificar o texto. | CLIP | Sim | Modelos CLIP carregados |

**Nota**: A entrada `clip` deve ser um modelo CLIP válido. Se for `None`, o nó gera um erro. Isso normalmente acontece quando o checkpoint carregado por um nó carregador de checkpoint não contém um modelo CLIP ou codificador de texto válido.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `CONDITIONING` | Um condicionamento contendo o texto incorporado usado para guiar o modelo de difusão. | CONDITIONING |

## Recursos do Prompt

### Modelos de Embedding

Modelos de embedding permitem aplicar efeitos artísticos ou estilos específicos. Os formatos suportados incluem `.safetensors`, `.pt` e `.bin`. Para usar um modelo de embedding:

1. Coloque o arquivo na pasta `ComfyUI/models/embeddings`.
2. Faça referência a ele no seu texto usando `embedding:model_name`.

Exemplo: se você tiver um modelo chamado `EasyNegative.pt` na pasta `ComfyUI/models/embeddings`, poderá usá-lo assim:

```
worst quality, embedding:EasyNegative, bad quality
```

**IMPORTANTE**: Ao usar modelos de embedding, verifique se o nome do arquivo corresponde e é compatível com a arquitetura do seu modelo. Por exemplo, um embedding projetado para SD1.5 não funcionará corretamente em um modelo SDXL.

### Ajuste de Peso do Prompt

Você pode ajustar a importância de certas partes da sua descrição usando parênteses. Por exemplo:

- `(beautiful:1.2)` aumenta o peso de "beautiful".
- `(beautiful:0.8)` diminui o peso de "beautiful".
- Parênteses simples `(beautiful)` aplicam um peso padrão de 1.1.

Você pode usar os atalhos de teclado `ctrl + seta para cima/baixo` para ajustar os pesos rapidamente. O tamanho do passo do ajuste de peso pode ser modificado nas configurações.

Se você quiser incluir parênteses literais no seu prompt sem alterar o peso, pode escapá-los usando uma barra invertida, por exemplo, `\(word\)`.

### Curingas/Prompts Dinâmicos

Use `{}` para criar prompts dinâmicos. Por exemplo, `{day|night|morning}` selecionará aleatoriamente uma opção toda vez que o prompt for processado.

Se você quiser incluir chaves literais no seu prompt sem acionar o comportamento dinâmico, pode escapá-las usando uma barra invertida, por exemplo, `\{word\}`.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ace7988df7aaa3ac26419b16a9bd8908a327da6e82c21c2b2704af091d2e76e7`
