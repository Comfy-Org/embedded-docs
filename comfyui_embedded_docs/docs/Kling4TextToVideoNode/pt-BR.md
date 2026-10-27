# Kling 4.0 Text to Video

Gera um vídeo a partir de um prompt de texto com o modelo Kling 4.0, incluindo áudio. Este nó envia o prompt e as configurações de geração para a API do Kling, aguarda a conclusão da tarefa e retorna o vídeo finalizado. Use-o quando um clipe precisar ser criado apenas a partir de uma descrição, sem mídia de referência.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `model` | Seletor de modelo. Apenas `"kling-4.0"` está disponível; selecioná-lo revela as entradas abaixo. | DYNAMIC_COMBO | Sim | `"kling-4.0"` |

### Entradas do kling-4.0

Estas entradas aparecem quando `model` está definido como `"kling-4.0"`.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-----------|---------------|-------------|-----------|
| `prompt` | Descrição textual do vídeo a ser gerado. Deve ter entre 1 e 26000 caracteres. | STRING | Sim | 1 a 26000 caracteres |
| `resolution` | Resolução do vídeo de saída. Padrão: `"720p"`. | COMBO | Sim | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Proporção do vídeo de saída. Padrão: `"16:9"`. | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"` |
| `duration` | Duração do vídeo gerado em segundos. Padrão: 5. | INT | Sim | 3 a 30 |
| `seed` | A seed controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da seed. Padrão: 42. | INT | Sim | 0 a 2147483647 |

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|---------------|-----------|---------------|
| `video` | O vídeo gerado, baixado do provedor assim que a tarefa for concluída. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4TextToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3835dcb7d83d843ea7f6c5dc691b48759d9c3e7a7baeead3d0f92817e73d6079`
