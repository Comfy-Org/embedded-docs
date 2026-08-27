# Carregar LoRA (Bypass) (Para depuração)

O nó LoraLoaderBypass aplica uma LoRA (Low-Rank Adaptation) a um modelo de difusão e a um modelo CLIP em um modo especial de "bypass". Diferentemente de um carregador de LoRA padrão, este método não modifica permanentemente os pesos do modelo base. Em vez disso, ele calcula a saída adicionando o efeito da LoRA à passagem direta normal do modelo, o que é útil para treinamento ou para trabalhar com modelos cujos pesos foram descarregados (offloaded).

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model` | O modelo de difusão ao qual a LoRA será aplicada. | MODEL | Sim | - |
| `clip` | O modelo CLIP ao qual a LoRA será aplicada. | CLIP | Sim | - |
| `lora_name` | O nome da LoRA. Os arquivos de LoRA disponíveis são carregados da pasta `loras`. | COMBO | Sim | Lista de arquivos LoRA disponíveis |
| `strength_model` | O quanto modificar o modelo de difusão. Este valor pode ser negativo (padrão: 1.0). | FLOAT | Sim | -100.0 a 100.0 (passo: 0.01) |
| `strength_clip` | O quanto modificar o modelo CLIP. Este valor pode ser negativo (padrão: 1.0). | FLOAT | Sim | -100.0 a 100.0 (passo: 0.01) |

**Nota:** Se ambos `strength_model` e `strength_clip` forem definidos como 0, o nó retorna as entradas `model` e `clip` originais, sem modificação, sem processamento.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `MODEL` | O modelo de difusão modificado. | MODEL |
| `CLIP` | O modelo CLIP modificado. | CLIP |

**Nota:** Este nó está marcado como experimental.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypass/pt-BR.md)

---
**Source fingerprint (SHA-256):** `025f0638a6690a53b1a6c4548dac24fb7e7f26e04ff4b1c88d29b061430037a8`
