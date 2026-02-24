> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAudio/pt-BR.md)

O nó PreviewAudio gera um arquivo de prévia de áudio temporário que pode ser exibido na interface. Ele herda do SaveAudio, mas salva os arquivos em um diretório temporário com um prefixo de nome de arquivo aleatório. Isso permite que os usuários visualizem rapidamente as saídas de áudio sem criar arquivos permanentes.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Sim | - | Os dados de áudio para pré-visualização |
| `prompt` | PROMPT | Não | - | Parâmetro oculto para uso interno |
| `extra_pnginfo` | EXTRA_PNGINFO | Não | - | Parâmetro oculto para uso interno |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `ui` | UI | Exibe a prévia do áudio na interface |
