# ClipTextEncode

Codifica um prompt de texto usando um modelo CLIP em um embedding que pode ser usado para guiar o modelo de difusão na geração de imagens específicas.

O `CLIP Text Encode (CLIPTextEncode)` atua como um tradutor, convertendo suas descrições de texto em um formato que a IA consegue entender. Isso ajuda a IA a interpretar sua entrada e gerar a imagem desejada.

Pense nisso como se comunicar com um artista que fala um idioma diferente. O modelo CLIP, treinado em vastos pares de imagem-texto, preenche essa lacuna convertendo suas descrições em "instruções" que o modelo de IA pode seguir.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `texto` | O texto a ser codificado. Suporta entrada multilinha e prompts dinâmicos. | STRING | Sim | Qualquer texto |
| `clip` | O modelo CLIP usado para codificar o texto. | CLIP | Sim | Modelos CLIP carregados |

Observação: Se a entrada `clip` for None (por exemplo, quando ela vem de um carregador de checkpoint cujo checkpoint não contém um modelo CLIP ou codificador de texto válido), o nó gera um erro.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `CONDITIONING` | Um condicionamento contendo o texto incorporado usado para guiar o modelo de difusão. | CONDITIONING |

## Recursos do prompt

### Modelos de embedding

Modelos de embedding permitem aplicar efeitos artísticos ou estilos específicos. Os formatos compatíveis incluem `.safetensors`, `.pt` e `.bin`. Para usar um modelo de embedding:

1. Coloque o arquivo na pasta `ComfyUI/models/embeddings`.
2. Referencie-o no seu texto usando `embedding:model_name`.

Exemplo: Se você tiver um modelo chamado `EasyNegative.pt` na sua pasta `ComfyUI/models/embeddings`, então você pode usá-lo assim:

```
worst quality, embedding:EasyNegative, bad quality
```

**IMPORTANTE**: Ao usar modelos de embedding, verifique se o nome do arquivo corresponde e é compatível com a arquitetura do seu modelo. Por exemplo, um embedding projetado para SD1.5 não funcionará corretamente para um modelo SDXL.

### Ajuste de peso do prompt

Você pode ajustar a importância de certas partes da sua descrição usando parênteses. Por exemplo:

- `(beautiful:1.2)` aumenta o peso de "beautiful".
- `(beautiful:0.8)` diminui o peso de "beautiful".
- Parênteses simples `(beautiful)` aplicarão um peso padrão de 1.1.

Você pode usar os atalhos de teclado `ctrl + up/down arrow` para ajustar os pesos rapidamente. O tamanho do passo de ajuste de peso pode ser modificado nas configurações.

Se você quiser incluir parênteses literais no seu prompt sem alterar o peso, você pode escapá-los usando uma barra invertida, por exemplo, `\(word\)`.

### Prompts curinga/dinâmicos

Use `{}` para criar prompts dinâmicos. Por exemplo, `{day|night|morning}` selecionará aleatoriamente uma opção sempre que o prompt for processado.

Se você quiser incluir chaves literais no seu prompt sem acionar o comportamento dinâmico, você pode escapá-las usando uma barra invertida, por exemplo, `\{word\}`.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipTextEncode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ace7988df7aaa3ac26419b16a9bd8908a327da6e82c21c2b2704af091d2e76e7`
