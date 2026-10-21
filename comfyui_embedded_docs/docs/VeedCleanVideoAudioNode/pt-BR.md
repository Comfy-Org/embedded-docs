# VEED Clean Audio (in Video)

Remova o ruído de fundo da fala em um vídeo com o VEED. Apenas a trilha sonora muda: ela é substituída pela fala limpa em mono de 48 kHz, enquanto a imagem, a resolução e a taxa de quadros permanecem como estão. Ele foi criado para fala em qualquer idioma, e músicas e efeitos sonoros são removidos em vez de preservados.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `video` | Vídeo com uma trilha sonora de fala, com menos de 30 minutos. O vídeo deve ter uma faixa de áudio. | VIDEO | Sim | Até 1799 segundos |
| `strength` | Quanto ruído é removido sob a fala. Valores menores mantêm mais tom ambiente atrás da voz; as pausas entre palavras são sempre totalmente limpas, e valores acima do padrão alteram pouco. (padrão: 0.874) | FLOAT | Sim | 0.0 a 1.0 (passo 0.001) |
| `loudness` | Se a sonoridade da fala deve ser normalizada. `"normalize"` a define como `target_lufs`; `"keep input level"` mantém o nível como está. Selecionar uma opção revela seus parâmetros. (padrão: `"normalize"`) | DYNAMIC_COMBO | Sim | `"normalize"`<br>`"keep input level"` |
| `target_lufs` | Sonoridade integrada da fala limpa em LUFS. Os picos são limitados a -1.1 dBTP, então alvos altos param cedo (cerca de -15 LUFS para fala típica). Disponível quando `loudness` é `"normalize"` (padrão: -19.0). | FLOAT | Sim | -40.0 a -8.0 (passo 0.1) |

O nó para com erro quando o clipe tem mais de 1799 segundos e quando o vídeo não tem faixa de áudio.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `VIDEO` | O vídeo de entrada com sua trilha sonora substituída pela fala limpa. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedCleanVideoAudioNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b8ff533f3ce45691cccd3449596252b0216178fdef0e7e728ccccbc9a8712217`
