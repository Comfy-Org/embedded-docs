> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRANode/pt-BR.md)

O nó SaveLoRA salva modelos LoRA (Low-Rank Adaptation) em seu diretório de saída. Ele recebe um modelo LoRA como entrada e cria um arquivo safetensors com um nome de arquivo gerado automaticamente. Você pode personalizar o prefixo do nome do arquivo e, opcionalmente, incluir a contagem de etapas de treinamento no nome do arquivo para melhor organização.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `lora` | LORA_MODEL | Sim | - | O modelo LoRA a ser salvo. Não use o modelo com camadas LoRA. |
| `prefix` | STRING | Sim | - | O prefixo a ser usado para o arquivo LoRA salvo (padrão: "loras/ComfyUI_trained_lora"). |
| `steps` | INT | Não | - | Opcional: O número de etapas em que o LoRA foi treinado, usado para nomear o arquivo salvo. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| *Nenhum* | - | Este nó não retorna nenhuma saída, mas salva o modelo LoRA no diretório de saída. |

---
**Source fingerprint (SHA-256):** `06a1067433aa4b720b51050b09fbad4870caf12c5e92f788d44ea022a39efef4`
