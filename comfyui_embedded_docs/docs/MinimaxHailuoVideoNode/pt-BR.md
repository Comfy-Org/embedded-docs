> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuoVideoNode/pt-BR.md)

Gera vídeos a partir de prompts de texto usando o modelo MiniMax Hailuo-02. Opcionalmente, você pode fornecer uma imagem inicial como primeiro quadro para criar um vídeo que continue a partir dessa imagem.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt_text` | STRING | Sim | - | Prompt de texto para orientar a geração do vídeo. |
| `seed` | INT | Não | 0 a 18446744073709551615 | A semente aleatória usada para criar o ruído (padrão: 0). |
| `first_frame_image` | IMAGE | Não | - | Imagem opcional para usar como primeiro quadro para gerar um vídeo. |
| `prompt_optimizer` | BOOLEAN | Não | - | Otimiza o prompt para melhorar a qualidade da geração quando necessário (padrão: Verdadeiro). |
| `duration` | COMBO | Não | `6`<br>`10` | A duração do vídeo de saída em segundos (padrão: 6). |
| `resolution` | COMBO | Não | `"768P"`<br>`"1080P"` | As dimensões de exibição do vídeo. 1080p é 1920x1080, 768p é 1366x768 (padrão: "768P"). |

**Observação:** Ao usar o modelo MiniMax-Hailuo-02 com resolução 1080P, a duração é limitada a 6 segundos.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | O arquivo de vídeo gerado. |
