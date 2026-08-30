# PixVerse Texto para Vídeo

Gera vídeos com base em um prompt de texto e diversos parâmetros de geração. Este nó cria conteúdo de vídeo usando a API PixVerse, permitindo controle sobre proporção de aspecto, qualidade, duração, estilo de movimento e muito mais.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt para a geração de vídeo (padrão: "") | STRING | Sim | - |
| `aspect_ratio` | Proporção de aspecto para o vídeo gerado | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `quality` | Configuração de qualidade do vídeo (padrão: "540p") | COMBO | Sim | `"540p"`<br>`"1080p"` |
| `duration_seconds` | Duração do vídeo gerado em segundos | COMBO | Sim | `"5"`<br>`"10"` |
| `motion_mode` | Estilo de movimento para a geração de vídeo | COMBO | Sim | `"normal"`<br>`"fast"` |
| `seed` | Semente para geração de vídeo (padrão: 0) | INT | Sim | 0 a 2147483647 |
| `negative_prompt` | Uma descrição textual opcional de elementos indesejados na imagem (padrão: "") | STRING | Não | - |
| `pixverse_template` | Um modelo (template) opcional para influenciar o estilo da geração, criado pelo nó PixVerse Template | CUSTOM | Não | - |

**Observação:** O `prompt` deve conter pelo menos 1 caractere. Ao usar qualidade 1080p, o modo de movimento é automaticamente definido como `normal` e a duração é limitada a 5 segundos. Para durações diferentes de 5 segundos, o modo de movimento também é automaticamente definido como `normal`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | O arquivo de vídeo gerado | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTextToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `cb95579dc6c9afa17455b0216ec46571ad2c0455606cf3b9c725ca512c45f938`
