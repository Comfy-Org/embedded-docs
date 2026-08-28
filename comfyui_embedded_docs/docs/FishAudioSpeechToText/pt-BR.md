# FishAudioSpeechToText

Este nó transcreve áudio em texto usando o serviço de fala para texto Fish Audio. Ele detecta automaticamente o idioma do áudio e pode, opcionalmente, retornar segmentos com timestamps em nível de palavra como JSON.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `audio` | Áudio a ser transcrito. | AUDIO | Sim | — |
| `language` | Dica de idioma ISO 639-1 (ex.: 'en', 'zh'). O idioma é detectado automaticamente de qualquer forma. Padrão: "" (string vazia). | STRING | Não | Qualquer código de idioma ISO 639-1, ex.: `en`, `zh`; string vazia para detecção automática |
| `precise_timestamps` | Retorna segmentos com timestamps em nível de palavra. Padrão: false. | BOOLEAN | Não | true ou false |

Nota: O parâmetro `language` é apenas uma dica — o idioma é sempre detectado automaticamente a partir do áudio. Quando `precise_timestamps` é false (o padrão), timestamps em nível de palavra não são retornados; quando true, os segmentos de saída incluem timestamps em nível de palavra.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `text` | O texto transcrito. | STRING |
| `language_code` | O código de idioma ISO 639-1 detectado para o áudio. | STRING |
| `segments_json` | String JSON contendo os segmentos da transcrição. Inclui timestamps em nível de palavra quando `precise_timestamps` está habilitado. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FishAudioSpeechToText/pt-BR.md)

---
**Source fingerprint (SHA-256):** `eaf1c9a9d2b90ec962a408615cc417b552864354c3f272144b8e239b23961920`
