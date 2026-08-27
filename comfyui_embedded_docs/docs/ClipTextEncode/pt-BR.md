# ClipTextEncode

`CLIP Text Encode (CLIPTextEncode)` atua como um tradutor, convertendo suas descrições textuais em um formato que a IA pode entender. Isso ajuda a IA a interpretar sua entrada e gerar a imagem desejada.

Pense nisso como se estivesse se comunicando com um artista que fala um idioma diferente. O modelo CLIP, treinado em vastos pares de imagem-texto, preenche essa lacuna convertendo suas descrições em "instruções" que o modelo de IA pode seguir.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `texto` | O texto a ser codificado. Suporta entrada de múltiplas linhas e prompts dinâmicos. | STRING | Sim | Qualquer texto |
| `clip` | O modelo CLIP usado para codificar o texto. | CLIP | Sim | Modelos CLIP carregados |

Nota: Se a entrada `clip` for None (por exemplo, quando vem de um carregador de checkpoint cujo checkpoint não contém um modelo CLIP ou codificador de texto válido), o nó gera um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `CONDITIONING` | Um condicionamento contendo o texto incorporado usado para guiar o modelo de difusão. | CONDITIONING |

## Recursos de Prompt

### Modelos de Embedding

Os modelos de embedding permitem aplicar efeitos artísticos ou estilos específicos. Os formatos suportados incluem `.safetensors`, `.pt` e `.bin`. Para usar um modelo de embedding:

1. Coloque o arquivo na pasta `ComfyUI/models/embeddings`.
2. Referencie-o no seu texto usando `embedding:model_name`.

Exemplo: Se você tiver um modelo chamado `EasyNegative.pt` na sua pasta `ComfyUI/models/embeddings`, poderá usá-lo assim:

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

Se você quiser incluir parênteses literais no seu prompt sem alterar o peso, pode escapá-los usando uma barra invertida, ex.: `\(word\)`.

### Prompts Dinâmicos/Curinga

Use `{}` para criar prompts dinâmicos. Por exemplo, `{day|night|morning}` selecionará aleatoriamente uma opção cada vez que o prompt for processado.

Se você quiser incluir chaves literais no seu prompt sem acionar o comportamento dinâmico, pode escapá-las usando uma barra invertida, ex.: `\{word\}`.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipTextEncode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ace7988df7aaa3ac26419b16a9bd8908a327da6e82c21c2b2704af091d2e76e7`
