> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStepLatentAudio/pt-BR.md)

Esta documentação foi gerada por IA. Se encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStepLatentAudio/en.md)

O nó EmptyAceStepLatentAudio cria amostras de áudio latente vazias com uma duração específica. Ele gera um lote de latentes de áudio silenciosos preenchidos com zeros, onde o comprimento é calculado com base nos segundos de entrada e nos parâmetros de processamento de áudio. Este nó é útil para inicializar fluxos de trabalho de processamento de áudio que exigem representações latentes.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `seconds` | FLOAT | Sim | 1.0 - 1000.0 | A duração do áudio em segundos (padrão: 120.0) |
| `batch_size` | INT | Sim | 1 - 4096 | O número de imagens latentes no lote (padrão: 1) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | LATENT | Retorna amostras de áudio latente vazias com zeros. A saída contém um tensor `samples` e um campo `type` definido como "audio". |

---
**Source fingerprint (SHA-256):** `79fcfb3cb26db8a2ef4480455a44255e0d1a16f122a762d7608a78b2330cc637`
