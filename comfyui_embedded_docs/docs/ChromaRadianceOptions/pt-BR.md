O nó ChromaRadianceOptions permite configurar opções avançadas para o modelo Chroma Radiance. Ele encapsula um modelo existente e aplica opções específicas durante o processo de remoção de ruído com base nos valores sigma, permitindo um controle refinado sobre o tamanho do tile NeRF e outros parâmetros relacionados à radiância.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model` | O modelo ao qual aplicar as opções Chroma Radiance | MODEL | Sim | - |
| `preserve_wrapper` | Quando ativado, delega para um wrapper de função de modelo existente, se houver. Geralmente deve permanecer ativado. (padrão: True) | BOOLEAN | Não | - |
| `start_sigma` | Primeiro sigma no qual essas opções estarão em vigor. (padrão: 1.0) | FLOAT | Não | 0.0 a 1.0 |
| `end_sigma` | Último sigma no qual essas opções estarão em vigor. (padrão: 0.0) | FLOAT | Não | 0.0 a 1.0 |
| `nerf_tile_size` | Permite substituir o tamanho padrão do tile NeRF. -1 significa usar o padrão (32). 0 significa usar o modo sem tiles (pode exigir muita VRAM). (padrão: -1) | INT | Não | -1 e acima |

**Nota:** As opções Chroma Radiance só entram em vigor quando o valor sigma atual estiver entre `end_sigma` e `start_sigma` (inclusive). O parâmetro `nerf_tile_size` só é aplicado quando definido como 0 ou valores maiores.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model` | O modelo modificado com as opções Chroma Radiance aplicadas | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ChromaRadianceOptions/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b49a12e9aba59e4669c59e05a6aeff6d4ae5a4b656ca5b0de4bdf71291dca095`
