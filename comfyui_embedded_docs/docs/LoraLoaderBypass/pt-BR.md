# Carregar LoRA (Bypass) (Para depuração)

O nó LoraLoaderBypass aplica uma LoRA (Adaptação de Baixo Posto) a um modelo de difusão e a um modelo CLIP em um modo especial de "desvio". Diferentemente de um carregador LoRA padrão, este método não modifica permanentemente os pesos do modelo base. Em vez disso, ele calcula a saída adicionando o efeito da LoRA à passagem direta normal do modelo, o que é útil para treinamento ou ao trabalhar com modelos que têm seus pesos descarregados.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model` | O modelo de difusão ao qual a LoRA será aplicada. | MODEL | Sim | - |
| `clip` | O modelo CLIP ao qual a LoRA será aplicada. | CLIP | Sim | - |
| `lora_name` | O nome do arquivo LoRA a ser aplicado. As opções são carregadas da pasta `loras`. | COMBO | Sim | *Lista de arquivos LoRA disponíveis* |
| `strength_model` | O quão fortemente modificar o modelo de difusão. Este valor pode ser negativo (padrão: 1,0). | FLOAT | Sim | -100,0 a 100,0 |
| `strength_clip` | O quão fortemente modificar o modelo CLIP. Este valor pode ser negativo (padrão: 1,0). | FLOAT | Sim | -100,0 a 100,0 |

**Nota:** Se tanto `strength_model` quanto `strength_clip` forem definidos como 0, o nó retornará as entradas originais e não modificadas de `model` e `clip` sem processamento.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `MODEL` | O modelo de difusão com a LoRA aplicada em modo de desvio. | MODEL |
| `CLIP` | O modelo CLIP com a LoRA aplicada em modo de desvio. | CLIP |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypass/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2642f4ed98457e5fd08e2103ffb9f2c02f11326590aadf0636fb7db51f484815`
