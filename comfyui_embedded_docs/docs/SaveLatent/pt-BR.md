# SalvarLatent

O nó SaveLatent salva tensores latentes em disco como arquivos para uso posterior ou compartilhamento. Ele recebe amostras latentes e as salva no diretório de saída com metadados opcionais, incluindo informações do prompt. O nó gerencia automaticamente a nomenclatura e organização dos arquivos, preservando a estrutura dos dados latentes.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `amostras` | As amostras latentes a serem salvas em disco | LATENT | Sim | - |
| `prefixo_do_arquivo` | O prefixo para o nome do arquivo de saída (padrão: "latents/ComfyUI") | STRING | Não | - |
| `prompt` | Informações do prompt a serem incluídas nos metadados (parâmetro oculto) | PROMPT | Não | - |
| `extra_pnginfo` | Informações PNG adicionais a serem incluídas nos metadados (parâmetro oculto) | EXTRA_PNGINFO | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `ui` | Fornece informações de localização do arquivo para o latente salvo na interface do ComfyUI | UI |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLatent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `dc7fd101c8dd93e2bcc39de64e0c39abe8e056c9e5932587fc6ce80e2fd143e8`
