# Carregar LoRA (Bypass) (Para depuração)

O nó LoraLoaderBypass aplica um LoRA (Low-Rank Adaptation) a um modelo de difusão e a um modelo CLIP em um modo especial de "bypass". Diferentemente de um carregador LoRA padrão, este método não modifica permanentemente os pesos do modelo base. Em vez disso, ele calcula o resultado adicionando a contribuição do LoRA à passagem direta normal do modelo, o que é útil para treinamento ou ao trabalhar com modelos que têm seus pesos descarregados.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo de difusão ao qual o LoRA será aplicado. | MODEL | Sim | - |
| `clip` | O modelo CLIP ao qual o LoRA será aplicado. | CLIP | Sim | - |
| `lora_name` | O nome do LoRA. Os arquivos LoRA disponíveis são carregados da pasta `loras`. | COMBO | Sim | Lista de arquivos LoRA disponíveis |
| `strength_model` | Com que intensidade modificar o modelo de difusão. Este valor pode ser negativo (padrão: 1.0). | FLOAT | Sim | -100.0 a 100.0 (passo: 0.01) |
| `strength_clip` | Com que intensidade modificar o modelo CLIP. Este valor pode ser negativo (padrão: 1.0). | FLOAT | Sim | -100.0 a 100.0 (passo: 0.01) |

**Nota:** Se tanto `strength_model` quanto `strength_clip` forem definidos como 0, o nó retorna as entradas `model` e `clip` originais e não modificadas, sem processamento.

**Nota:** O arquivo LoRA selecionado é armazenado em cache após ser carregado pela primeira vez. Ele só é lido novamente do disco quando um `lora_name` diferente é escolhido.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `MODEL` | O modelo de difusão modificado. | MODEL |
| `CLIP` | O modelo CLIP modificado. | CLIP |

**Nota:** Este nó está marcado como experimental.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypass/pt-BR.md)

---
**Source fingerprint (SHA-256):** `025f0638a6690a53b1a6c4548dac24fb7e7f26e04ff4b1c88d29b061430037a8`
