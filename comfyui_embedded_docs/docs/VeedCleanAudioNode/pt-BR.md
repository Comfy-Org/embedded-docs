# VEED Clean Audio

Remova o ruído de fundo da fala com o VEED. Ele foi desenvolvido para fala em qualquer idioma: o ruído abaixo da voz é limpo, as pausas são limpas completamente, e músicas e efeitos sonoros são removidos, em vez de preservados. A saída é áudio mono de 48 kHz.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `audio` | Gravação de fala, com menos de 30 minutos. | AUDIO | Sim | Até 1799 segundos |
| `strength` | Quanto ruído é removido sob a fala. Valores menores mantêm mais tom ambiente atrás da voz; as pausas entre palavras são sempre totalmente limpas, e valores acima do padrão mudam pouco. (padrão: 0.874) | FLOAT | Sim | 0.0 a 1.0 (passo 0.001) |
| `loudness` | Se deve normalizar o volume da saída. `"normalize"` define a saída para `target_lufs`; `"keep input level"` mantém o nível como está. Selecionar uma opção revela seus parâmetros. (padrão: `"normalize"`) | DYNAMIC_COMBO | Sim | `"normalize"`<br>`"keep input level"` |
| `target_lufs` | Volume integrado da saída em LUFS. Os picos são limitados a -1.1 dBTP, então alvos altos param cedo (cerca de -15 LUFS para fala típica). Disponível quando `loudness` é `"normalize"` (padrão: -19.0). | FLOAT | Sim | -40.0 a -8.0 (passo 0.1) |

O nó para com um erro quando a gravação tem mais de 1799 segundos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `AUDIO` | A fala limpa como áudio mono de 48 kHz. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedCleanAudioNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c85949385109a5d320e52619e9df17c245b19f8f16cc1a0b69a37ae2e7bb5b6d`
