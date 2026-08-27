# Reve Image Create

O nó Reve Image Create gera imagens a partir de descrições textuais usando o modelo Reve AI. Ele envia um prompt de texto para a API Reve e retorna a imagem gerada, com controles de proporção de aspecto e pós-processamento opcional, como upscaling e remoção de fundo. Este nó está obsoleto.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | Versão do modelo a ser usada para geração. | DYNAMIC_COMBO | Sim | `"reve-create@20250915"` |
| `prompt` | Descrição textual da imagem desejada. Máximo de 2560 caracteres. | STRING | Sim | 1 a 2560 caracteres |
| `upscale` | Aplicar upscale na imagem gerada. Pode adicionar custo extra. Padrão: "disabled". | DYNAMIC_COMBO | Não | `"disabled"`<br>`"enabled"` |
| `remove_background` | Remove o fundo da imagem gerada. Pode adicionar custo extra. Padrão: False. | BOOLEAN | Não | N/A |
| `seed` | O seed controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente do seed. Padrão: 0. | INT | Não | 0 a 2147483647 |

### Entradas do reve-create@20250915

Opções disponíveis quando `model` está definido como `"reve-create@20250915"`:

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `aspect_ratio` | Proporção de aspecto da imagem de saída. | COMBO | Sim | `"3:2"`<br>`"16:9"`<br>`"9:16"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `test_time_scaling` | Valores maiores produzem melhores imagens, mas custam mais créditos. Padrão: 1. Opção avançada. | INT | Não | 1 a 5 |

### Entradas de upscale

Opções disponíveis quando `upscale` está definido como `"enabled"`:

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `upscale_factor` | Fator de upscale (2x, 3x ou 4x). Padrão: 2. | INT | Não | 2 a 4 |

**Nota:** O parâmetro `seed` não garante saídas determinísticas. O parâmetro `upscale` controla se o upscaling é aplicado como uma etapa de pós-processamento e pode adicionar custo extra. O `prompt` deve conter entre 1 e 2560 caracteres.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `image` | A imagem gerada pelo modelo Reve com base no prompt de entrada. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageCreateNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `69178bc7d11e32ca179be5f598fbe60c4d41955b87e1c797e79cf224917a930c`
