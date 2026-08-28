# Obter Parâmetros IC-LoRA

Este nó lê os metadados de um modelo carregado com LoRA para extrair parâmetros IC-LoRA, como o fator de redução de escala de referência. Ele gera esses parâmetros como um objeto estruturado que pode ser conectado ao nó LTXVAddGuide quando uma LoRA exige tratamento especial dos guias.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `iclora_model` | Saída direta de um LoRA Loader para o IC-LoRA específico do qual extrair os metadados. | MODEL | Sim | N/A |

Observação: Se os metadados da LoRA estiverem ausentes ou não contiverem uma entrada `reference_downscale_factor`, o nó gera um valor padrão de 1. Quando presente, o fator é arredondado e definido com um mínimo de 1.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `iclora_parameters` | Parâmetros IC-LoRA extraídos dos metadados da LoRA (por exemplo, `reference_downscale_factor`). Conecte ao LTXVAddGuide se a LoRA exigir tratamento especial dos guias. | IC_LORA_PARAMETERS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetICLoRAParameters/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5f6becad0c7673b8cde1e099bd7ba5be7106da958b8967f8e693ba2a704baaef`
