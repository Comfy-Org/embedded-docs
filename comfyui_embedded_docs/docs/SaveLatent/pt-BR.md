> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLatent/pt-BR.md)

O nó SaveLatent salva tensores latentes em disco como arquivos para uso posterior ou compartilhamento. Ele recebe amostras latentes e as salva no diretório de saída com metadados opcionais, incluindo informações do prompt. O nó gerencia automaticamente a nomenclatura e organização dos arquivos, preservando a estrutura dos dados latentes.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `amostras` | LATENT | Sim | - | As amostras latentes a serem salvas em disco |
| `prefixo_do_arquivo` | STRING | Não | - | O prefixo para o nome do arquivo de saída (padrão: "latents/ComfyUI") |
| `prompt` | PROMPT | Não | - | Informações do prompt a serem incluídas nos metadados (parâmetro oculto) |
| `extra_pnginfo` | EXTRA_PNGINFO | Não | - | Informações PNG adicionais a serem incluídas nos metadados (parâmetro oculto) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `ui` | UI | Fornece informações de localização do arquivo para o latente salvo na interface do ComfyUI |

---
**Source fingerprint (SHA-256):** `dc7fd101c8dd93e2bcc39de64e0c39abe8e056c9e5932587fc6ce80e2fd143e8`
