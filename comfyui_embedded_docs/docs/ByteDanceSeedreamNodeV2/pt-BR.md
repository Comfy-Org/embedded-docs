> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNodeV2/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNodeV2/en.md)

## Visão Geral

Este nó gera ou edita imagens usando os modelos Seedream da ByteDance (versões 4.0, 4.5 e 5.0 Lite). Ele pode criar novas imagens a partir de um prompt de texto ou editar imagens existentes fornecendo imagens de referência, suportando resoluções de até 4K.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `prompt` | STRING | Sim | N/A | Prompt de texto para criar ou editar uma imagem. |
| `model` | COMBO | Sim | `"seedream 5.0 lite"`<br>`"seedream-4-5-251128"`<br>`"seedream-4-0-250828"` | A versão do modelo Seedream a ser usada para geração. Cada modelo possui diferentes capacidades e preços. |
| `seed` | INT | Não | 0 a 2147483647 | Semente a ser usada para geração (padrão: 0). |
| `watermark` | BOOLEAN | Não | Verdadeiro / Falso | Se deve adicionar uma marca d'água "gerado por IA" à imagem (padrão: Falso). |

### Parâmetros Específicos do Modelo

Ao selecionar um modelo, parâmetros adicionais ficam disponíveis:

- **Predefinição de Tamanho**: Um menu suspenso para selecionar uma resolução de imagem predefinida (ex.: "2048x2048", "1024x1024"). As predefinições disponíveis dependem do modelo selecionado.
- **Largura**: A largura da imagem gerada em pixels (padrão: 2048).
- **Altura**: A altura da imagem gerada em pixels (padrão: 2048).
- **Máximo de Imagens**: O número máximo de imagens a serem geradas (padrão: 1). Quando definido como 1, a geração sequencial de imagens é desativada.
- **Imagens de Referência**: Até 10 (para Seedream 4.0 e 4.5) ou 14 (para Seedream 5.0 Lite) imagens de referência para edição. As imagens devem ter uma proporção entre 1:3 e 3:1.
- **Falhar em Parcial**: Se ativado, o nó gerará um erro se nem todas as imagens solicitadas forem geradas com sucesso (padrão: Falso).

### Restrições de Resolução

- **Seedream 5.0 Lite e 4.5**: A resolução mínima é de 3,68 megapixels (ex.: 1920x1920).
- **Seedream 4.0**: A resolução mínima é de 0,92 megapixels (ex.: 960x960).
- **Todos os modelos**: A resolução máxima é de 16,78 megapixels (ex.: 4096x4096).

### Restrições de Quantidade de Imagens

- O número total de imagens de referência mais imagens geradas não pode exceder 15.
- Para Seedream 5.0 Lite, são suportadas no máximo 14 imagens de referência.
- Para Seedream 4.0 e 4.5, são suportadas no máximo 10 imagens de referência.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `image` | IMAGE | A imagem gerada ou editada como um tensor. Se múltiplas imagens foram solicitadas, elas são concatenadas em um único lote. |

---
**Source fingerprint (SHA-256):** `1ceccfdb773807a993c32af22703da155367b67865338c78f153a8ccb02dcc8f`
