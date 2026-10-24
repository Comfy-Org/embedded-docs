# Bria Guided Remove Background

Este nó remove o fundo de uma imagem com a Bria, mantendo o que o prompt descreve. Os pixels originais retornam em resolução total com um novo canal alfa, em vez de serem renderizados novamente, então detalhes finos e bordas são preservados. Um prompt que não corresponde a nada retorna uma imagem totalmente transparente. Para um recorte simples sem orientação, o Bria Remove Image Background custa menos.

## Entradas

O seletor `moderation` revela opções adicionais de moderação quando definido como `"true"`.

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | A imagem a ser recortada. | IMAGE | Sim | - |
| `prompt` | O que manter e, opcionalmente, o que descartar ou restringir, como 'a pessoa com o tapete e a planta', 'a mulher na mesa dela sem o abajur' ou 'apenas a cadeira'. Não deve estar vazio. Se nada corresponder ao prompt, o resultado será totalmente transparente. Padrão: `""` (string vazia). | STRING | Sim | 1 caractere ou mais |
| `moderation` | Configurações de moderação. Quando definido como `"true"`, os sinalizadores de moderação visual abaixo ficam disponíveis. | DYNAMIC_COMBO | Sim | `"false"`<br>`"true"` |

### Entradas de moderação "true"

Esses parâmetros aparecem apenas quando `moderation` está definido como `"true"`. A opção `"false"` não adiciona entradas adicionais.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | Ativa a moderação de conteúdo na imagem de entrada. Padrão: `False`. | BOOLEAN | Não | True / False |
| `visual_output_moderation` | Ativa a moderação de conteúdo na imagem gerada. Padrão: `False`. | BOOLEAN | Não | True / False |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A imagem recortada: os pixels originais com um novo canal alfa. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaGuidedRemoveBackground/pt-BR.md)

---
**Source fingerprint (SHA-256):** `210fa214a0d0d8ad19a15ea4f6baa9f13499bc4c3767e270f19f2a08d67e25ac`
