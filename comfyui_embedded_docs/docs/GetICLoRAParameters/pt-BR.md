> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetICLoRAParameters/pt-BR.md)

Esta documentação foi gerada por IA. Se encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetICLoRAParameters/en.md)

## Visão Geral

Este nó extrai parâmetros IC-LoRA dos metadados de um modelo carregado com LoRA. Ele lê os metadados do safetensors para encontrar valores como o fator de redução de referência e os gera como um objeto de parâmetros estruturado, que pode ser conectado ao nó LTXVAddGuide para tratamento especial de guias.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|---------------|-------------|-----------|-----------|
| `iclora_model` | MODEL | Sim | N/A | Saída direta de um Carregador LoRA para o IC-LoRA específico do qual extrair os metadados. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `iclora_parameters` | IC_LORA_PARAMETERS | Parâmetros IC-LoRA extraídos dos metadados do LoRA (ex.: fator de redução de referência). Conecte ao LTXVAddGuide se o LoRA exigir tratamento especial das guias. |

---
**Source fingerprint (SHA-256):** `44673f0b06cb258014efd77f734c076865d59338ddf825598d85592f000aca50`
