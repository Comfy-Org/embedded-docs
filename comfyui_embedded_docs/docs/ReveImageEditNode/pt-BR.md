# Reve Image Edit

O nó Reve Image Edit modifica uma imagem existente com base em uma instrução de texto em linguagem natural. Ele envia a imagem de entrada e sua instrução para a API Reve, que retorna uma nova imagem com as edições solicitadas aplicadas.

## Entradas

O seletor `model` determina quais entradas específicas do modelo são exibidas. O seletor `upscale` controla se a entrada de fator de upscale está disponível.

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | A imagem a ser editada. | IMAGE | Sim | - |
| `edit_instruction` | Descrição em texto de como editar a imagem. Máximo de 2560 caracteres. | STRING | Sim | - |
| `model` | Versão do modelo a ser usada para edição. | DYNAMIC_COMBO | Sim | `"reve-edit@20250915"`<br>`"reve-edit-fast@20251030"` |
| `upscale` | Aplicar upscale à imagem gerada. Pode adicionar custo adicional. (padrão: "disabled") | DYNAMIC_COMBO | Não | `"disabled"`<br>`"enabled"` |
| `remove_background` | Remover o fundo da imagem gerada. Pode adicionar custo adicional. (padrão: False) | BOOLEAN | Não | `true`<br>`false` |
| `seed` | A seed controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da seed. (padrão: 0) | INT | Não | 0 a 2147483647 |

### Entradas do modelo (compartilhadas por `reve-edit@20250915` e `reve-edit-fast@20251030`)

Ambas as versões do modelo expõem as mesmas entradas específicas do modelo.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `aspect_ratio` | Proporção de aspecto da imagem de saída. Quando definido como "auto", a proporção de aspecto é determinada automaticamente. | COMBO | Não | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `test_time_scaling` | Opção avançada. Valores maiores produzem imagens melhores, mas custam mais créditos. (padrão: 1) | INT | Não | 1 a 5 |

### Entradas de upscale (quando `upscale` está definido como "enabled")

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `upscale.upscale_factor` | Fator de upscale (2x, 3x ou 4x). (padrão: 2) | INT | Não | 2 a 4 |

**Nota:**

- `upscale.upscale_factor` só se aplica quando `upscale` está definido como "enabled". O upscale e a remoção de fundo podem ser ativados juntos ou independentemente.
- `edit_instruction` não pode estar vazio e não pode exceder 2560 caracteres.
- Quando `model.aspect_ratio` está definido como "auto", nenhuma proporção de aspecto fixa é enviada à API e a proporção de aspecto é escolhida automaticamente.
- `model.test_time_scaling` só é enviado à API quando seu valor é maior que 1; o valor padrão de 1 mantém o comportamento padrão da API.
- Os resultados são não determinísticos independentemente do valor da seed; a seed apenas controla se o nó é executado novamente.
- Este nó está marcado como obsoleto.
- Custo aproximado em USD (de acordo com o selo de preço do nó): `$0.01001` para `reve-edit-fast@20251030`; `$0.0572` para `reve-edit@20250915` sem upscale; `$0.0686` com upscale de 2x, `$0.0819` com upscale de 3x e `$0.0991` com upscale de 4x.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A imagem editada gerada com base na instrução. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageEditNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4001f3ab4cc4e705c235f578e90e497bb30d22110ef69b16fb072a91a65d15df`
