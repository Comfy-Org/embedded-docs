> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTemplateNode/pt-BR.md)

O nó PixVerse Template permite que você selecione entre os modelos disponíveis para a geração de vídeos do PixVerse. Ele converte o nome do modelo selecionado no ID de modelo correspondente que a API do PixVerse requer para a criação de vídeos.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `template` | STRING | Sim | Múltiplas opções disponíveis | O modelo a ser usado para a geração de vídeo do PixVerse. As opções disponíveis correspondem a modelos predefinidos no sistema PixVerse. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `pixverse_template` | INT | O ID do modelo correspondente ao nome do modelo selecionado, que pode ser usado por outros nós do PixVerse para geração de vídeo. |
