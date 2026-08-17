# ChromaRadianceOptions

O nó **ChromaRadianceOptions** permite configurar opções avançadas para o modelo Chroma Radiance. Ele encapsula um modelo existente e aplica opções específicas durante o processo de denoising com base nos valores de sigma, permitindo controle refinado sobre o tamanho do tile NeRF e outros parâmetros relacionados à radiância.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `model` | O modelo ao qual aplicar as opções do Chroma Radiance. | MODEL | Sim | - |
| `preserve_wrapper` | Quando ativado, delega para um wrapper de função de modelo existente, se houver. Geralmente deve permanecer ativado. (padrão: True) | BOOLEAN | Não | - |
| `start_sigma` | Primeiro sigma em que essas opções estarão em vigor. (padrão: 1.0) | FLOAT | Não | 0.0 a 1.0 |
| `end_sigma` | Último sigma em que essas opções estarão em vigor. (padrão: 0.0) | FLOAT | Não | 0.0 a 1.0 |
| `nerf_tile_size` | Permite substituir o tamanho padrão do tile NeRF. -1 significa usar o padrão (32). 0 significa usar o modo sem tiles (pode exigir muita VRAM). (padrão: -1) | INT | Não | -1 ou acima |
| `force_sequential_txt_ids` | Força o uso de IDs sequenciais de tokens de texto em vez de zeros. Deve ser usado para checkpoints de 2026-05-22 a 2026-06-01 treinados dessa forma, mas que não contêm a chave `__sequential__` no state dict. (padrão: False) | BOOLEAN | Não | - |

**Nota:** As opções do Chroma Radiance só entram em vigor quando o valor atual de sigma estiver entre `end_sigma` e `start_sigma` (inclusive). O parâmetro `nerf_tile_size` só é aplicado quando definido com valores 0 ou maiores. O parâmetro `force_sequential_txt_ids` só é aplicado quando definido como True.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-----------|---------------|
| `model` | O modelo modificado com as opções do Chroma Radiance aplicadas. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ChromaRadianceOptions/pt-BR.md)

---
**Source fingerprint (SHA-256):** `761f1946fe1fd77158e97f6f34d002e2445cc00e008741f8c37cde5673900409`
