`CLIP Text Encode (CLIPTextEncode)` atua como um tradutor, convertendo suas descrições textuais em um formato que a IA pode compreender. Isso ajuda a IA a interpretar sua entrada e gerar a imagem desejada.

Pense nisso como se comunicar com um artista que fala um idioma diferente. O modelo CLIP, treinado em vastos pares de imagem-texto, preenche essa lacuna convertendo suas descrições em "instruções" que o modelo de IA pode seguir.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `texto` | O texto a ser codificado. Suporta entrada multilinha e prompts dinâmicos. | STRING | Sim | Qualquer texto |
| `clip` | O modelo CLIP usado para codificar o texto. | CLIP | Sim | Modelos CLIP carregados |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `CONDITIONING` | Um condicionamento contendo o texto incorporado usado para guiar o modelo de difusão. | CONDITIONING |

## Recursos de Prompt

### Modelos de Incorporação (Embedding)

Modelos de incorporação permitem aplicar efeitos artísticos ou estilos específicos. Os formatos suportados incluem `.safetensors`, `.pt` e `.bin`. Para usar um modelo de incorporação:

1. Coloque o arquivo na pasta `ComfyUI/models/embeddings`.
2. Faça referência a ele em seu texto usando `embedding:nome_do_modelo`.

Exemplo: Se você tem um modelo chamado `EasyNegative.pt` na sua pasta `ComfyUI/models/embeddings`, então pode usá-lo assim:

```
pior qualidade, embedding:EasyNegative, má qualidade
```

**IMPORTANTE**: Ao usar modelos de incorporação, verifique se o nome do arquivo corresponde e é compatível com a arquitetura do seu modelo. Por exemplo, uma incorporação projetada para SD1.5 não funcionará corretamente em um modelo SDXL.

### Ajuste de Peso do Prompt

Você pode ajustar a importância de certas partes da sua descrição usando parênteses. Por exemplo:

- `(bonito:1.2)` aumenta o peso de "bonito".
- `(bonito:0.8)` diminui o peso de "bonito".
- Parênteses simples `(bonito)` aplicarão um peso padrão de 1.1.

Você pode usar os atalhos de teclado `ctrl + seta para cima/baixo` para ajustar rapidamente os pesos. O tamanho do passo do ajuste de peso pode ser modificado nas configurações.

Se você quiser incluir parênteses literais em seu prompt sem alterar o peso, pode escapá-los usando uma barra invertida, ex.: `\(palavra\)`.

### Prompts Dinâmicos/Curinga (Wildcard)

Use `{}` para criar prompts dinâmicos. Por exemplo, `{dia|noite|manhã}` selecionará aleatoriamente uma opção cada vez que o prompt for processado.

Se você quiser incluir chaves literais em seu prompt sem acionar o comportamento dinâmico, pode escapá-las usando uma barra invertida, ex.: `\{palavra\}`.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncode/pt-BR.md)

---

**Source fingerprint (SHA-256):** `e8f286cdec879c529270e110ccf5959ed6df77737cfb5a8019379afac9266118`
