> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypass/pt-BR.md)

O nó LoraLoaderBypass aplica uma LoRA (Adaptação de Baixo Posto) a um modelo de difusão e a um modelo CLIP em um modo especial de "desvio". Diferentemente de um carregador LoRA padrão, este método não modifica permanentemente os pesos do modelo base. Em vez disso, ele calcula a saída adicionando o efeito da LoRA à passagem direta normal do modelo, o que é útil para treinamento ou ao trabalhar com modelos que têm seus pesos descarregados.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `model` | MODEL | Sim | - | O modelo de difusão ao qual a LoRA será aplicada. |
| `clip` | CLIP | Sim | - | O modelo CLIP ao qual a LoRA será aplicada. |
| `lora_name` | COMBO | Sim | *Lista de arquivos LoRA disponíveis* | O nome do arquivo LoRA a ser aplicado. As opções são carregadas da pasta `loras`. |
| `strength_model` | FLOAT | Sim | -100,0 a 100,0 | O quão fortemente modificar o modelo de difusão. Este valor pode ser negativo (padrão: 1,0). |
| `strength_clip` | FLOAT | Sim | -100,0 a 100,0 | O quão fortemente modificar o modelo CLIP. Este valor pode ser negativo (padrão: 1,0). |

**Nota:** Se tanto `strength_model` quanto `strength_clip` forem definidos como 0, o nó retornará as entradas originais e não modificadas de `model` e `clip` sem processamento.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `MODEL` | MODEL | O modelo de difusão com a LoRA aplicada em modo de desvio. |
| `CLIP` | CLIP | O modelo CLIP com a LoRA aplicada em modo de desvio. |

---
**Source fingerprint (SHA-256):** `2642f4ed98457e5fd08e2103ffb9f2c02f11326590aadf0636fb7db51f484815`
