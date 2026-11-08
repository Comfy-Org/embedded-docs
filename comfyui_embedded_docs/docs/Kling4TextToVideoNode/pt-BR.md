# Kling 4.0 Texto para Vídeo

Gera um vídeo a partir de um prompt de texto com o modelo Kling 4.0, incluindo áudio. Este nó envia o prompt e as configurações de geração para a API do Kling, aguarda a conclusão da tarefa e retorna o vídeo finalizado. Use-o quando um clipe precisar ser criado apenas a partir de uma descrição, sem mídia de referência.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | Seletor de modelo. `"kling-4.0"` oferece suporte a até 1080p e 30 segundos; `"kling-4.0-flash"` é limitado a 720p e 20 segundos. Ao selecionar um modelo, as entradas correspondentes são exibidas abaixo. | DYNAMIC_COMBO | Sim | `"kling-4.0"`<br>`"kling-4.0-flash"` |

### Entradas do kling-4.0

Estas entradas aparecem quando `model` é definido como `"kling-4.0"`.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Descrição em texto do vídeo a ser gerado. Deve ter entre 1 e 26000 caracteres. | STRING | Sim | 1 a 26000 caracteres |
| `resolution` | Resolução do vídeo de saída. Padrão: `"720p"`. | COMBO | Sim | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Proporção do vídeo de saída. Padrão: `"16:9"`. | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"` |
| `duration` | Duração do vídeo gerado em segundos. Padrão: 5. | INT | Sim | 3 a 30 |
| `seed` | A semente controla se o nó deve ser executado novamente; os resultados não são determinísticos independentemente da semente. Padrão: 42. | INT | Sim | 0 a 2147483647 |

### Entradas do kling-4.0-flash

Estas entradas aparecem quando `model` é definido como `"kling-4.0-flash"`.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Descrição em texto do vídeo a ser gerado. Deve ter entre 1 e 26000 caracteres. | STRING | Sim | 1 a 26000 caracteres |
| `resolution` | Resolução do vídeo de saída. O Flash renderiza somente em 720p. Padrão: `"720p"`. | COMBO | Sim | `"720p"` |
| `aspect_ratio` | Proporção do vídeo de saída. Padrão: `"16:9"`. | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"` |
| `duration` | Duração do vídeo gerado em segundos. Padrão: 5. | INT | Sim | 3 a 20 |
| `seed` | A semente controla se o nó deve ser executado novamente; os resultados não são determinísticos independentemente da semente. Padrão: 42. | INT | Sim | 0 a 2147483647 |

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `video` | O vídeo gerado, baixado do provedor após a conclusão da tarefa. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4TextToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3e37f976f48488c3accb4efb0d876d12c316796023eb9c28b9209cb2188249e2`
