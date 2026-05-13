> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTextToVideoNode/pt-BR.md)

Gera vídeos com base em um prompt de texto e vários parâmetros de geração. Este nó cria conteúdo de vídeo usando a API PixVerse, permitindo controle sobre proporção de aspecto, qualidade, duração, estilo de movimento e muito mais.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `prompt` | STRING | Sim | - | Prompt para a geração do vídeo (padrão: "") |
| `aspect_ratio` | COMBO | Sim | Opções do PixverseAspectRatio | Proporção de aspecto do vídeo gerado |
| `quality` | COMBO | Sim | Opções do PixverseQuality | Configuração de qualidade do vídeo (padrão: PixverseQuality.res_540p) |
| `duration_seconds` | COMBO | Sim | Opções do PixverseDuration | Duração do vídeo gerado em segundos |
| `motion_mode` | COMBO | Sim | Opções do PixverseMotionMode | Estilo de movimento para a geração do vídeo |
| `seed` | INT | Sim | 0 a 2147483647 | Semente para geração do vídeo (padrão: 0) |
| `negative_prompt` | STRING | Não | - | Uma descrição textual opcional de elementos indesejados em uma imagem (padrão: "") |
| `pixverse_template` | CUSTOM | Não | - | Um template opcional para influenciar o estilo da geração, criado pelo nó PixVerse Template |

**Observação:** Ao usar qualidade 1080p, o modo de movimento é automaticamente definido como normal e a duração é limitada a 5 segundos. Para durações diferentes de 5 segundos, o modo de movimento também é automaticamente definido como normal.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | VIDEO | O arquivo de vídeo gerado |

---
**Source fingerprint (SHA-256):** `ab9264668f48533cb139abfb322e9a6e425a2ad7280da103a7fe0a7704158762`
