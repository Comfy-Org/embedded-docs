Gera vídeos com base em um prompt de texto e vários parâmetros de geração. Este nó cria conteúdo de vídeo usando a API PixVerse, permitindo controle sobre proporção de aspecto, qualidade, duração, estilo de movimento e muito mais.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt para a geração do vídeo (padrão: "") | STRING | Sim | - |
| `aspect_ratio` | Proporção de aspecto do vídeo gerado | COMBO | Sim | Opções do PixverseAspectRatio |
| `quality` | Configuração de qualidade do vídeo (padrão: PixverseQuality.res_540p) | COMBO | Sim | Opções do PixverseQuality |
| `duration_seconds` | Duração do vídeo gerado em segundos | COMBO | Sim | Opções do PixverseDuration |
| `motion_mode` | Estilo de movimento para a geração do vídeo | COMBO | Sim | Opções do PixverseMotionMode |
| `seed` | Semente para geração do vídeo (padrão: 0) | INT | Sim | 0 a 2147483647 |
| `negative_prompt` | Uma descrição textual opcional de elementos indesejados em uma imagem (padrão: "") | STRING | Não | - |
| `pixverse_template` | Um template opcional para influenciar o estilo da geração, criado pelo nó PixVerse Template | CUSTOM | Não | - |

**Observação:** Ao usar qualidade 1080p, o modo de movimento é automaticamente definido como normal e a duração é limitada a 5 segundos. Para durações diferentes de 5 segundos, o modo de movimento também é automaticamente definido como normal.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O arquivo de vídeo gerado | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTextToVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ab9264668f48533cb139abfb322e9a6e425a2ad7280da103a7fe0a7704158762`
