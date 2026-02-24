> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTextToVideoNode/pt-BR.md)

Gera vídeos com base no prompt e no tamanho de saída. Este nó cria conteúdo de vídeo usando descrições textuais e vários parâmetros de geração, produzindo a saída de vídeo por meio da API PixVerse.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sim | - | Prompt para a geração do vídeo (padrão: "") |
| `aspect_ratio` | COMBO | Sim | Opções de PixverseAspectRatio | Proporção de aspecto para o vídeo gerado |
| `quality` | COMBO | Sim | Opções de PixverseQuality | Configuração de qualidade do vídeo (padrão: PixverseQuality.res_540p) |
| `duration_seconds` | COMBO | Sim | Opções de PixverseDuration | Duração do vídeo gerado em segundos |
| `motion_mode` | COMBO | Sim | Opções de PixverseMotionMode | Estilo de movimento para a geração do vídeo |
| `seed` | INT | Sim | 0 a 2147483647 | Semente para a geração do vídeo (padrão: 0) |
| `negative_prompt` | STRING | Não | - | Uma descrição textual opcional de elementos indesejados na imagem (padrão: "") |
| `pixverse_template` | CUSTOM | Não | - | Um modelo opcional para influenciar o estilo da geração, criado pelo nó PixVerse Template |

**Observação:** Ao usar a qualidade 1080p, o modo de movimento é automaticamente definido como normal e a duração é limitada a 5 segundos. Para durações diferentes de 5 segundos, o modo de movimento também é automaticamente definido como normal.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O arquivo de vídeo gerado |
