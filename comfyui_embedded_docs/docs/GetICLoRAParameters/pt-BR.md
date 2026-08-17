# Obter Parâmetros IC-LoRA

## Visão Geral

Este nó extrai parâmetros IC-LoRA dos metadados de um modelo carregado com LoRA. Ele lê os metadados safetensors para encontrar valores como o fator de redução de escala de referência e os emite como um objeto de parâmetro estruturado, que pode ser conectado ao nó LTXVAddGuide para tratamento especial de guias. Se os metadados estiverem ausentes ou o fator de redução de escala de referência não puder ser lido, o valor assume o padrão de 1; quando encontrado, o valor é arredondado e limitado a um mínimo de 1.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `iclora_model` | Saída direta de um LoRA Loader para o IC-LoRA específico do qual extrair os metadados. | MODEL | Sim | N/A |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `iclora_parameters` | Parâmetros IC-LoRA extraídos dos metadados do LoRA (por exemplo, reference_downscale_factor). Conecte ao LTXVAddGuide se o LoRA exigir tratamento especial das guias. | IC_LORA_PARAMETERS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetICLoRAParameters/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5f6becad0c7673b8cde1e099bd7ba5be7106da958b8967f8e693ba2a704baaef`
