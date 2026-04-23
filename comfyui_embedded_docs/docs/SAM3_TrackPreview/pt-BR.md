> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3_TrackPreview/pt-BR.md)

# Visão Geral

Este nó cria uma prévia em vídeo dos objetos rastreados, desenhando cada objeto rastreado com uma sobreposição de cor distinta e um rótulo numérico. Ele não gera nenhum tensor de imagem ou vídeo — em vez disso, salva o vídeo de prévia resultante diretamente em um arquivo temporário.

# Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `track_data` | TRACK_DATA | Sim | - | Os dados de rastreamento contendo máscaras empacotadas e informações de objetos de um nó de rastreamento SAM3. |
| `images` | IMAGE | Não | - | Imagens de entrada opcionais para usar como fundo da prévia. Se não fornecidas, um fundo preto é usado. |
| `opacity` | FLOAT | Não | 0.0 a 1.0 (passo: 0.05) | A opacidade da sobreposição de cor aplicada aos objetos rastreados (padrão: 0.5). |
| `fps` | FLOAT | Não | 1.0 a 120.0 (passo: 1.0) | A taxa de quadros do vídeo de saída (padrão: 24.0). |

# Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `ui` | PREVIEW_VIDEO | Um elemento de interface que exibe o vídeo de prévia gerado. Nenhum dado de tensor é retornado. |