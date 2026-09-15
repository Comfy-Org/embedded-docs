# PixVerse Texto para Vídeo

Gera vídeos a partir de um prompt de texto usando a API PixVerse. O nó permite controlar a forma, a qualidade, a duração e o estilo de movimento do vídeo e, opcionalmente, aplicar um modelo de estilo salvo. Ele envia a solicitação, aguarda a conclusão da geração e retorna o vídeo finalizado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt para a geração do vídeo (padrão: "") | STRING | Sim | Deve conter pelo menos 1 caractere |
| `aspect_ratio` | Proporção de aspecto para o vídeo gerado | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `quality` | Configuração de qualidade do vídeo (padrão: "540p") | COMBO | Sim | `"540p"`<br>`"1080p"` |
| `duration_seconds` | Duração do vídeo gerado em segundos | COMBO | Sim | `"5"`<br>`"10"` |
| `motion_mode` | Estilo de movimento para a geração do vídeo | COMBO | Sim | `"normal"`<br>`"fast"` |
| `seed` | Semente para geração de vídeo (padrão: 0) | INT | Sim | 0 a 2147483647 |
| `negative_prompt` | Uma descrição de texto opcional de elementos indesejados em uma imagem (padrão: "") | STRING | Não | - |
| `pixverse_template` | Um template opcional para influenciar o estilo da geração, criado pelo nó PixVerse Template | CUSTOM | Não | - |

**Observação:** O `prompt` deve conter pelo menos 1 caractere. Quando a qualidade 1080p é selecionada, o modo de movimento é definido automaticamente como `normal` e a duração é limitada a 5 segundos. Para qualquer duração diferente de 5 segundos, o modo de movimento também é definido automaticamente como `normal`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | O arquivo de vídeo gerado | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTextToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `cb95579dc6c9afa17455b0216ec46571ad2c0455606cf3b9c725ca512c45f938`
