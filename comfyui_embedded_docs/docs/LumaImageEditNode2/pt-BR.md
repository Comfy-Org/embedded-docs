# Luma UNI-1 Image Edit

Este nó edita uma imagem existente usando um prompt de texto, com tecnologia do modelo Luma UNI-1. Ele recebe uma imagem de origem e uma descrição da alteração desejada e, em seguida, gera uma nova versão editada da imagem. Você pode escolher entre os modelos `uni-1` e `uni-1-max`, ajustar o estilo, ativar a pesquisa na web e, opcionalmente, fornecer até 8 imagens de referência.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo a ser usado para edição. Selecionar um modelo revela as opções específicas do modelo abaixo. | MODEL | Sim | `"uni-1"`<br>`"uni-1-max"` |
| `source` | Imagem de origem para editar. | IMAGE | Sim | - |
| `prompt` | Descrição da edição desejada. 1–6000 caracteres. Padrão: "" (string vazia; a solicitação é inválida até que pelo menos um caractere seja inserido). | STRING | Sim | 1 a 6000 caracteres |
| `seed` | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente. Padrão: 0. | INT | Sim | 0 a 2147483647 |

### Entradas de uni-1 e uni-1-max

Estas opções são compartilhadas pelos modelos `uni-1` e `uni-1-max`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `style` | Predefinição de estilo. `"auto"` escolhe com base no prompt; `"manga"` aplica uma estética de mangá/anime e exige proporção de tela retrato (2:3, 9:16, 1:2, 1:3). Padrão: `"auto"`. | STRING | Sim | `"auto"`<br>`"manga"` |
| `web_search` | Pesquisar na web por referências visuais antes de gerar. Padrão: false. | BOOLEAN | Sim | `true`<br>`false` |

### Entradas de referência

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image_ref` | Slot expansível: conecte até 8 imagens de referência (`image_1` a `image_8`) para orientação de estilo/conteúdo. Opcional. | IMAGE | Não | 0 a 8 imagens |

**Notas:**
- O `prompt` deve ter entre 1 e 6000 caracteres.
- As entradas `style`, `web_search` e `image_ref` aparecem quando `model` está definido como `"uni-1"` ou `"uni-1-max"`.
- Ambos os modelos suportam as mesmas opções específicas do modelo, incluindo até 8 imagens de referência.
- O estilo `"manga"` exige uma proporção de tela retrato (2:3, 9:16, 1:2 ou 1:3).
- Conectar mais de 8 imagens de referência gera um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A imagem editada gerada pelo modelo Luma UNI-1. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageEditNode2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `66f62bb2807759edb405c2caeeefe32c341920924e267c32449a620190b9a7ab`
