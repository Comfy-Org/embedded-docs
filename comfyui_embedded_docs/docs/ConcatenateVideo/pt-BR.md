# ConcatenateVideo

Concatena vários segmentos de vídeo em um único vídeo, preservando a ordem em que são conectados. Entradas codificadas compatíveis são combinadas sem serem decodificadas, e uma faixa de áudio separada opcional pode ser fornecida para substituir o áudio original.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `videos` | Segmentos de vídeo a concatenar na ordem de entrada. Conecte de 1 a 100 vídeos; cada vídeo aparece como um slot de entrada separado rotulado como `video_1`, `video_2`, etc. | VIDEO | Sim | 1 a 100 segmentos |
| `codec` | Codec usado para codificar tensores de vídeo. O modo `"auto"` usa H.264; vídeos já codificados compatíveis permanecem inalterados. Padrão: `"auto"` | COMBO | Sim | `"auto"`<br>Outras opções são definidas pelos tipos de codec de vídeo disponíveis. |
| `complete_audio` | Trilha sonora completa opcional para o vídeo concatenado. Substitui o áudio carregado pelos vídeos de entrada. | AUDIO | Não | N/A |

**Observação:** A entrada `videos` aceita entre 1 e 100 segmentos de vídeo. Se `complete_audio` for fornecido, ele substitui o áudio de todos os vídeos de entrada. Quando `codec` está definido como `"auto"`, entradas codificadas compatíveis são concatenadas sem decodificação.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `VIDEO` | O vídeo concatenado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConcatenateVideo/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f591aecb83754127e1c86ed0488548f9e7d99f3559c95a1c86c55fa5d430713d`
