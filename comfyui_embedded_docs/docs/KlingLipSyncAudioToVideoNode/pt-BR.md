> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncAudioToVideoNode/pt-BR.md)

O nó Kling Lip Sync Audio to Video sincroniza os movimentos da boca em um arquivo de vídeo para corresponder ao conteúdo de um arquivo de áudio. Este nó analisa os padrões vocais no áudio e ajusta os movimentos faciais no vídeo para criar uma sincronização labial realista. O processo requer tanto um vídeo contendo um rosto distinto quanto um arquivo de áudio com vocais claramente distinguíveis.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Sim | - | O arquivo de vídeo contendo um rosto a ser sincronizado labialmente |
| `audio` | AUDIO | Sim | - | O arquivo de áudio contendo os vocais para sincronizar com o vídeo |
| `voice_language` | COMBO | Não | `"en"`<br>`"zh"`<br>`"es"`<br>`"fr"`<br>`"de"`<br>`"it"`<br>`"pt"`<br>`"pl"`<br>`"tr"`<br>`"ru"`<br>`"nl"`<br>`"cs"`<br>`"ar"`<br>`"ja"`<br>`"hu"`<br>`"ko"` | O idioma da voz no arquivo de áudio (padrão: "en") |

**Restrições Importantes:**

- O arquivo de áudio não deve ser maior que 5MB
- O arquivo de vídeo não deve ser maior que 100MB
- As dimensões do vídeo devem estar entre 720px e 1920px de altura/largura
- A duração do vídeo deve estar entre 2 segundos e 10 segundos
- O áudio deve conter vocais claramente distinguíveis
- O vídeo deve conter um rosto distinto

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O vídeo processado com movimentos de boca sincronizados |
| `video_id` | STRING | O identificador único para o vídeo processado |
| `duration` | STRING | A duração do vídeo processado |
