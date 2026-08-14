# QwenImageEditApi

Este nó utiliza os modelos Qwen-Image 3.0 para editar ou combinar até 3 imagens de referência guiadas por um prompt de texto. Você fornece o prompt de texto e as imagens de referência, e o nó retorna o resultado gerado como uma ou mais imagens.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo a ser usado. Esta seleção também inclui o prompt de texto, até 3 entradas de imagens de referência e um prompt negativo opcional. | COMBO | Sim | "qwen-image-3.0-pro"<br>"qwen-image-3.0" |
| `size` | Resolução de saída. "match input" reutiliza o tamanho da primeira imagem de referência, "auto" permite que o modelo escolha um tamanho com a mesma proporção, "custom" define largura e altura explícitas. | COMBO | Sim | "match input"<br>"auto"<br>"custom" |
| `n` | Número de imagens a gerar, retornado como um lote. (padrão: 1) | INT | Não | 1 a 6 |
| `seed` | Semente usada para a geração. (padrão: 42) | INT | Não | 0 a 2147483647 |
| `prompt_extend` | Se deve aprimorar o prompt com assistência de IA. (padrão: True) | BOOLEAN | Não | True<br>False |
| `watermark` | Se deve adicionar uma marca d'água gerada por IA ao resultado. (padrão: False) | BOOLEAN | Não | True<br>False |

### Restrições

- O prompt de texto é obrigatório e deve conter pelo menos um caractere.
- Há suporte para no máximo 3 imagens de referência; um erro é gerado se mais forem fornecidas (uma entrada em lote conta uma vez por imagem).
- Quando `size` estiver definido como "custom", valores explícitos de largura e altura devem ser fornecidos e são validados.
- Quando `size` estiver definido como "match input", pelo menos uma imagem de referência é necessária porque as dimensões da primeira imagem de referência são usadas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| IMAGE | A imagem ou imagens geradas retornadas como um lote. Até `n` imagens são retornadas. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageEditApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `efa8d2b1a039a7b91789c0332b751a5f90ab8dad755ef0e25124d7d1c44d9abb`
