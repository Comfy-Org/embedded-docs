# Kling Sincronização Labial de Vídeo com Áudio

O nó Kling Lip Sync Audio to Video sincroniza os movimentos da boca em um arquivo de vídeo para corresponder ao conteúdo de áudio de um arquivo de áudio. Este nó analisa os padrões vocais no áudio e ajusta os movimentos faciais no vídeo para criar uma sincronização labial realista. O processo exige tanto um vídeo contendo um rosto nítido quanto um arquivo de áudio com vocais claramente distinguíveis.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `video` | O arquivo de vídeo contendo um rosto a ser sincronizado labialmente | VIDEO | Sim | - |
| `audio` | O arquivo de áudio contendo vocais para sincronizar com o vídeo | AUDIO | Sim | - |
| `voice_language` | O idioma da voz no arquivo de áudio (padrão: "en") | COMBO | Sim | `"en"`<br>`"zh"`<br>`"es"`<br>`"fr"`<br>`"de"`<br>`"it"`<br>`"pt"`<br>`"pl"`<br>`"tr"`<br>`"ru"`<br>`"nl"`<br>`"cs"`<br>`"ar"`<br>`"ja"`<br>`"hu"`<br>`"ko"` |

**Restrições importantes:**

- O arquivo de áudio não deve ser maior que 5MB
- O arquivo de vídeo não deve ser maior que 100MB
- As dimensões do vídeo devem estar entre 720px e 1920px em altura/largura
- A duração do vídeo deve estar entre 2 segundos e 10 segundos
- O áudio deve conter vocais claramente distinguíveis
- O vídeo deve conter um rosto nítido

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | O vídeo processado com movimentos da boca sincronizados | VIDEO |
| `video_id` | O identificador exclusivo do vídeo processado | STRING |
| `duration` | A duração do vídeo processado | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncAudioToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2f88af3191ac4f9c5c9fa1aaa5b744a12620b66e55a1fe0ab16b8b3b61110128`
