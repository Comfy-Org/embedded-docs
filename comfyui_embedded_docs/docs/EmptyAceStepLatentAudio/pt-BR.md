# Áudio Latente AceStep Vazio

Esta documentação foi gerada por IA. Se encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStepLatentAudio/en.md)

O nó EmptyAceStepLatentAudio cria amostras de áudio latente vazias com uma duração específica. Ele gera um lote de latentes de áudio silenciosos preenchidos com zeros, onde o comprimento é calculado com base nos segundos de entrada e nos parâmetros de processamento de áudio. Este nó é útil para inicializar fluxos de trabalho de processamento de áudio que exigem representações latentes.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `segundos` | A duração do áudio em segundos (padrão: 120.0) | FLOAT | Sim | 1.0 - 1000.0 |
| `tamanho_do_lote` | O número de imagens latentes no lote (padrão: 1) | INT | Sim | 1 - 4096 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | Retorna amostras de áudio latente vazias com zeros. A saída contém um tensor `samples` e um campo `type` definido como "audio". | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStepLatentAudio/pt-BR.md)

---
**Source fingerprint (SHA-256):** `79fcfb3cb26db8a2ef4480455a44255e0d1a16f122a762d7608a78b2330cc637`
