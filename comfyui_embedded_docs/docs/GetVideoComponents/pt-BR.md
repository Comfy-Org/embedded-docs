> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetVideoComponents/pt-BR.md)

O nó Get Video Components extrai todos os elementos principais de um arquivo de vídeo. Ele separa o vídeo em quadros individuais, extrai a faixa de áudio e fornece informações sobre a taxa de quadros do vídeo. Isso permite que você trabalhe com cada componente de forma independente para processamento ou análise posterior.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Sim | - | O vídeo do qual extrair os componentes. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `images` | IMAGE | Os quadros individuais extraídos do vídeo como imagens separadas. |
| `audio` | AUDIO | A faixa de áudio extraída do vídeo. |
| `fps` | FLOAT | A taxa de quadros do vídeo em quadros por segundo. |
