# Kling 4.0 Texto para Vídeo

Gera um vídeo a partir de um prompt de texto com o modelo Kling 4.0, incluindo áudio. Este nó envia o prompt e as configurações de geração para a API do Kling, aguarda a conclusão da tarefa e retorna o vídeo finalizado. Use-o quando for necessário criar um clipe apenas a partir de uma descrição, sem mídia de referência.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Seletor de modelo. `"kling-4.0"` suporta até 4K HDR e 30 segundos; `"kling-4.0-flash"` é limitado a 720p e 20 segundos. Selecionar um modelo revela as entradas correspondentes abaixo. | DYNAMIC_COMBO | Sim | `"kling-4.0"`<br>`"kling-4.0-flash"` |

### Entradas do kling-4.0

Essas entradas aparecem quando `model` está definido como `"kling-4.0"`.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Descrição em texto do vídeo a ser gerado. Deve ter entre 1 e 26000 caracteres. | STRING | Sim | 1 a 26000 caracteres |
| `resolution` | Resolução do vídeo de saída; uma opção com `HDR` no nome retorna um vídeo HDR. Padrão: `"720p"`. | COMBO | Sim | `"720p"`<br>`"1080p"`<br>`"4k"`<br>`"1080p HDR"`<br>`"4k HDR"` |
| `aspect_ratio` | Proporção de aspecto do vídeo de saída. Padrão: `"16:9"`. | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Duração do vídeo gerado em segundos. Padrão: 5. | INT | Sim | 3 a 30 |
| `seed` | A seed controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da seed. Padrão: 42. | INT | Sim | 0 a 2147483647 |

### Entradas do kling-4.0-flash

Essas entradas aparecem quando `model` está definido como `"kling-4.0-flash"`.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Descrição em texto do vídeo a ser gerado. Deve ter entre 1 e 26000 caracteres. | STRING | Sim | 1 a 26000 caracteres |
| `resolution` | Resolução do vídeo de saída. O Flash renderiza apenas em 720p. Padrão: `"720p"`. | COMBO | Sim | `"720p"` |
| `aspect_ratio` | Proporção de aspecto do vídeo de saída. Padrão: `"16:9"`. | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Duração do vídeo gerado em segundos. Padrão: 5. | INT | Sim | 3 a 20 |
| `seed` | A seed controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da seed. Padrão: 42. | INT | Sim | 0 a 2147483647 |

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `video` | O vídeo gerado, baixado do provedor depois que a tarefa for concluída. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4TextToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7a5d99aa6f5fdb923ce9e2c89f64e92d46fad14d28002a033ddedc24c7d27894`
