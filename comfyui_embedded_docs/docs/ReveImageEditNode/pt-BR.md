# Reve Image Edit

O nó Reve Image Edit permite modificar uma imagem existente com base em uma descrição textual. Ele usa a API Reve para interpretar suas instruções e aplicar as alterações solicitadas à imagem fornecida.

## Entradas

### Entradas Comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | A imagem a ser editada. | IMAGE | Sim | - |
| `edit_instruction` | Descrição textual de como editar a imagem. Máximo de 2560 caracteres. (padrão: "") | STRING | Sim | 1 a 2560 caracteres |
| `model` | Versão do modelo a ser usada para edição. | DYNAMIC_COMBO | Sim | `"reve-edit@20250915"`<br>`"reve-edit-fast@20251030"` |
| `upscale` | Ampliar a imagem gerada. Pode adicionar custo extra. (padrão: "disabled") | DYNAMIC_COMBO | Não | `"disabled"`<br>`"enabled"` |
| `remove_background` | Remover o fundo da imagem gerada. Pode adicionar custo extra. (padrão: false) | BOOLEAN | Não | `true`<br>`false` |
| `seed` | O seed controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente do seed. (padrão: 0) | INT | Não | 0 a 2147483647 |

### Entradas do Modelo

Compartilhadas pelos modelos `reve-edit@20250915` e `reve-edit-fast@20251030`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model.aspect_ratio` | Proporção de aspecto da imagem de saída. Quando definida como `"auto"`, a proporção é determinada automaticamente. (padrão: "auto") | COMBO | Não | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `model.test_time_scaling` | Valores maiores produzem imagens melhores, mas custam mais créditos. (padrão: 1) | INT | Não | 1 a 5 |

### Entradas de Upscale

Exibidas quando `upscale` está definido como `"enabled"`.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `upscale.upscale_factor` | Fator de ampliação (2x, 3x ou 4x). (padrão: 2) | INT | Não | 2 a 4 |

**Observação:** O parâmetro `upscale.upscale_factor` só aparece quando `upscale` está definido como `"enabled"`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A imagem editada gerada com base na instrução. | IMAGE |

**Observação:** Este nó está marcado como obsoleto.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageEditNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4001f3ab4cc4e705c235f578e90e497bb30d22110ef69b16fb072a91a65d15df`
