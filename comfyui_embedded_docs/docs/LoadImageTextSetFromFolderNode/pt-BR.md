> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageTextSetFromFolderNode/pt-BR.md)

Carrega um lote de imagens e suas legendas de texto correspondentes de um diretório especificado para fins de treinamento. O nó busca automaticamente arquivos de imagem e seus arquivos de texto de legenda associados, processa as imagens de acordo com as configurações de redimensionamento especificadas e codifica as legendas usando o modelo CLIP fornecido.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `folder` | STRING | Sim | - | A pasta de onde carregar as imagens. |
| `clip` | CLIP | Sim | - | O modelo CLIP usado para codificar o texto. |
| `resize_method` | COMBO | Não | "None"<br>"Stretch"<br>"Crop"<br>"Pad" | O método usado para redimensionar as imagens (padrão: "None"). |
| `width` | INT | Não | -1 a 10000 | A largura para a qual redimensionar as imagens. -1 significa usar a largura original (padrão: -1). |
| `height` | INT | Não | -1 a 10000 | A altura para a qual redimensionar as imagens. -1 significa usar a altura original (padrão: -1). |

**Observação:** A entrada `clip` deve ser válida e não pode ser None. Se o modelo CLIP vier de um nó carregador de checkpoint, certifique-se de que o checkpoint contenha um modelo CLIP ou codificador de texto válido.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | O lote de imagens carregadas e processadas. |
| `CONDITIONING` | CONDITIONING | Os dados de condicionamento codificados a partir das legendas de texto. |
