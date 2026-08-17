# Reve Image Create

O nó Reve Image Create gera imagens a partir de descrições textuais usando o modelo Reve AI. Ele envia um prompt de texto para a API da Reve e retorna a imagem gerada. Você pode controlar a proporção de aspecto da imagem e aplicar efeitos opcionais de pós-processamento, como upscaling e remoção de fundo. Este nó está obsoleto.

## Entradas

### Entradas Comuns

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|--------------|-------------|-----------|
| `model` | Versão do modelo a ser usada para geração. Selecionar este modelo expõe as configurações `aspect_ratio` e `test_time_scaling`. | DYNAMIC_COMBO | Sim | `"reve-create@20250915"` |
| `prompt` | Descrição textual da imagem desejada. Máximo de 2560 caracteres. Padrão: vazio. | STRING | Sim | N/A |
| `seed` | A semente controla se o nó deve ser executado novamente; os resultados não são determinísticos independentemente da semente. Padrão: 0. | INT | Não | 0 a 2147483647 |
| `upscale` | Aplica upscaling na imagem gerada. Pode adicionar custo adicional. Quando definido como `enabled`, a configuração `upscale_factor` aparece. Padrão: `disabled`. | DYNAMIC_COMBO | Não | `"disabled"`<br>`"enabled"` |
| `remove_background` | Remove o fundo da imagem gerada. Pode adicionar custo adicional. Padrão: false. | BOOLEAN | Não | true<br>false |

### Entradas de reve-create@20250915

Estas configurações aparecem quando `model` está definido como `"reve-create@20250915"`.

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|--------------|-------------|-----------|
| `aspect_ratio` | Proporção de aspecto da imagem de saída. | COMBO | Sim | `"3:2"`<br>`"16:9"`<br>`"9:16"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `test_time_scaling` | Valores mais altos produzem imagens melhores, mas custam mais créditos. Padrão: 1. | INT | Não | 1 a 5 |

### Entradas de Upscale

Estas configurações aparecem quando `upscale` está definido como `"enabled"`.

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|--------------|-------------|-----------|
| `upscale_factor` | Fator de upscaling (2x, 3x ou 4x). Padrão: 2. | INT | Não | 2 a 4 (passo 1) |

**Nota:** O parâmetro `seed` não garante saídas determinísticas. O parâmetro `upscale` controla se o upscaling é aplicado como etapa de pós-processamento.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-------------|--------------|
| `image` | A imagem gerada pelo modelo Reve com base no prompt de entrada. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageCreateNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `69178bc7d11e32ca179be5f598fbe60c4d41955b87e1c797e79cf224917a930c`
