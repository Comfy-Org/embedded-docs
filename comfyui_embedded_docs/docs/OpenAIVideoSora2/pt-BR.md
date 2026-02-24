> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIVideoSora2/pt-BR.md)

O nó OpenAIVideoSora2 gera vídeos utilizando os modelos Sora da OpenAI. Ele cria conteúdo de vídeo com base em prompts de texto e imagens de entrada opcionais, retornando o vídeo gerado. O nó suporta diferentes durações e resoluções de vídeo, dependendo do modelo selecionado.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sim | "sora-2"<br>"sora-2-pro" | O modelo OpenAI Sora a ser usado para a geração de vídeo (padrão: "sora-2") |
| `prompt` | STRING | Sim | - | Texto orientador; pode estar vazio se uma imagem de entrada estiver presente (padrão: vazio) |
| `size` | COMBO | Sim | "720x1280"<br>"1280x720"<br>"1024x1792"<br>"1792x1024" | A resolução para o vídeo gerado (padrão: "1280x720") |
| `duration` | COMBO | Sim | 4<br>8<br>12 | A duração do vídeo gerado em segundos (padrão: 8) |
| `image` | IMAGE | Não | - | Imagem de entrada opcional para a geração de vídeo |
| `seed` | INT | Não | 0 a 2147483647 | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente (padrão: 0) |

**Restrições e Limitações:**

- O modelo "sora-2" suporta apenas as resoluções "720x1280" e "1280x720"
- Apenas uma imagem de entrada é suportada ao usar o parâmetro `image`
- Os resultados são não determinísticos, independentemente do valor da semente

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | VIDEO | A saída do vídeo gerado |
