# ChromaRadianceOptions

O nó ChromaRadianceOptions permite configurar definições avançadas para o modelo Chroma Radiance. Ele anexa um wrapper a um modelo existente e aplica as opções selecionadas durante o processo de denoising somente quando o valor de sigma atual estiver dentro do intervalo configurado, dando controle sobre o tamanho de tile do NeRF e o tratamento de IDs de tokens de texto.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo ao qual aplicar as opções do Chroma Radiance | MODEL | Sim | - |
| `preserve_wrapper` | Quando habilitado, delegará a um wrapper de função de modelo existente, se houver. Em geral, deve ser deixado habilitado. (padrão: True) | BOOLEAN | Não | - |
| `start_sigma` | Primeiro sigma em que estas opções entrarão em vigor. (padrão: 1.0) | FLOAT | Não | 0.0 a 1.0 |
| `end_sigma` | Último sigma em que estas opções entrarão em vigor. (padrão: 0.0) | FLOAT | Não | 0.0 a 1.0 |
| `nerf_tile_size` | Permite substituir o tamanho de tile padrão do NeRF. -1 significa usar o padrão (32). 0 significa usar o modo sem tiling (pode exigir muita VRAM). (padrão: -1) | INT | Não | -1 and above |
| `force_sequential_txt_ids` | Força o uso de IDs de tokens de texto sequenciais em vez de zeros. Deve ser usado para checkpoints de 2026-05-22 a 2026-06-01 que são treinados dessa forma, mas não contêm a chave __sequential__ no state dict. (padrão: False) | BOOLEAN | Não | - |

**Observação:** As opções do Chroma Radiance só entram em vigor quando o valor de sigma atual estiver entre `end_sigma` e `start_sigma` (inclusive). A opção `nerf_tile_size` só é aplicada quando definida como 0 ou um valor maior (um valor de -1 usa o tamanho de tile padrão de 32 e não armazena nenhuma substituição). A opção `force_sequential_txt_ids` só é aplicada quando definida como True. Quando `nerf_tile_size` for -1 e `force_sequential_txt_ids` for False, nenhuma opção é configurada e o modelo é retornado inalterado, sem qualquer wrapper aplicado.

**Observação:** Todas as entradas além de `model` são opções avançadas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `model` | O modelo com as opções do Chroma Radiance aplicadas, ou o modelo inalterado se nenhuma opção estiver ativa | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ChromaRadianceOptions/pt-BR.md)

---
**Source fingerprint (SHA-256):** `761f1946fe1fd77158e97f6f34d002e2445cc00e008741f8c37cde5673900409`
