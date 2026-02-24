> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageSetNode/pt-BR.md)

O LoadImageSetNode carrega múltiplas imagens do diretório de entrada para fins de processamento em lote e treinamento. Ele suporta vários formatos de imagem e pode, opcionalmente, redimensionar as imagens usando diferentes métodos. Este nó processa todas as imagens selecionadas como um lote e as retorna como um único tensor.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Sim | Múltiplos arquivos de imagem | Selecione múltiplas imagens do diretório de entrada. Suporta formatos PNG, JPG, JPEG, WEBP, BMP, GIF, JPE, APNG, TIF e TIFF. Permite a seleção em lote de imagens. |
| `resize_method` | STRING | Não | "None"<br>"Stretch"<br>"Crop"<br>"Pad" | Método opcional para redimensionar as imagens carregadas (padrão: "None"). Escolha "None" para manter os tamanhos originais, "Stretch" para forçar o redimensionamento, "Crop" para manter a proporção cortando a imagem, ou "Pad" para manter a proporção adicionando preenchimento. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | Um tensor contendo todas as imagens carregadas como um lote para processamento posterior. |
