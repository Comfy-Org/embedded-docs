> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTransitionVideoNode/pt-BR.md)

Gera vídeos com base em prompt e output_size. Este nó cria vídeos de transição entre duas imagens de entrada usando a API PixVerse, permitindo que você especifique a qualidade do vídeo, duração, estilo de movimento e parâmetros de geração.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `first_frame` | IMAGE | Sim | - | A imagem inicial para a transição de vídeo |
| `last_frame` | IMAGE | Sim | - | A imagem final para a transição de vídeo |
| `prompt` | STRING | Sim | - | Prompt para a geração do vídeo (padrão: string vazia) |
| `quality` | COMBO | Sim | Opções de qualidade disponíveis na enumeração PixverseQuality<br>Padrão: res_540p | Configuração da qualidade do vídeo |
| `duration_seconds` | COMBO | Sim | Opções de duração disponíveis na enumeração PixverseDuration | Duração do vídeo em segundos |
| `motion_mode` | COMBO | Sim | Opções de modo de movimento disponíveis na enumeração PixverseMotionMode | Estilo de movimento para a transição |
| `seed` | INT | Sim | 0 a 2147483647 | Semente para geração de vídeo (padrão: 0) |
| `negative_prompt` | STRING | Não | - | Uma descrição textual opcional de elementos indesejados em uma imagem (padrão: string vazia) |

**Observação:** Ao usar a qualidade 1080p, o modo de movimento é automaticamente definido como normal e a duração é limitada a 5 segundos. Para durações diferentes de 5 segundos, o modo de movimento também é automaticamente definido como normal.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O vídeo de transição gerado |
