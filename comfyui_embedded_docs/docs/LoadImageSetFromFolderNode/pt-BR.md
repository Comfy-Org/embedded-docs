> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageSetFromFolderNode/pt-BR.md)

O LoadImageSetFromFolderNode carrega múltiplas imagens de um diretório de pasta especificado para fins de treinamento. Ele detecta automaticamente formatos de imagem comuns e pode, opcionalmente, redimensionar as imagens usando diferentes métodos antes de retorná-las como um lote.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `folder` | STRING | Sim | Múltiplas opções disponíveis | A pasta da qual as imagens serão carregadas. |
| `resize_method` | STRING | Não | "None"<br>"Stretch"<br>"Crop"<br>"Pad" | O método a ser usado para redimensionar as imagens (padrão: "None"). |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | O lote de imagens carregadas como um único tensor. |
