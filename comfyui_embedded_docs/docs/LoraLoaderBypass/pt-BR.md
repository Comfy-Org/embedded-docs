# Carregar LoRA (Bypass) (Para depuração)

O nó LoraLoaderBypass aplica uma LoRA (Adaptação de Baixo Posto) a um modelo de difusão e a um modelo CLIP em um modo de bypass especial. Diferente de um carregador de LoRA padrão, ele não modifica permanentemente os pesos do modelo base. Em vez disso, ele adiciona o efeito da LoRA à passagem direta normal do modelo, o que é útil para treinamento ou ao trabalhar com modelos que têm seus pesos descarregados.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model` | O modelo de difusão ao qual a LoRA será aplicada. | MODEL | Sim | N/A |
| `clip` | O modelo CLIP ao qual a LoRA será aplicada. | CLIP | Sim | N/A |
| `lora_name` | O nome do arquivo LoRA a ser aplicado. As opções são carregadas da pasta `loras`. | COMBO | Sim | Lista de arquivos LoRA disponíveis |
| `strength_model` | A intensidade com que o modelo de difusão será modificado. Este valor pode ser negativo (padrão: 1.0). | FLOAT | Sim | -100.0 a 100.0 |
| `strength_clip` | A intensidade com que o modelo CLIP será modificado. Este valor pode ser negativo (padrão: 1.0). | FLOAT | Sim | -100.0 a 100.0 |

**Nota:** Se tanto `strength_model` quanto `strength_clip` forem definidos como 0, o nó retorna as entradas originais e não modificadas `model` e `clip`, sem processamento.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `MODEL` | O modelo de difusão com a LoRA aplicada em modo de bypass. | MODEL |
| `CLIP` | O modelo CLIP com a LoRA aplicada em modo de bypass. | CLIP |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypass/pt-BR.md)

---
**Source fingerprint (SHA-256):** `025f0638a6690a53b1a6c4548dac24fb7e7f26e04ff4b1c88d29b061430037a8`
