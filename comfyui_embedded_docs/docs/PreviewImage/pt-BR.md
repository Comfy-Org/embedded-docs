> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewImage/pt-BR.md)

O nó PreviewImage é projetado para criar imagens de visualização temporárias. Ele gera automaticamente um nome de arquivo temporário único para cada imagem, comprime a imagem para um nível especificado e a salva em um diretório temporário. Essa funcionalidade é particularmente útil para gerar visualizações de imagens durante o processamento sem afetar os arquivos originais.

## Entradas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `images`  | `IMAGE`     | A entrada 'images' especifica as imagens a serem processadas e salvas como imagens de visualização temporárias. Esta é a entrada principal do nó, determinando quais imagens passarão pelo processo de geração de visualização. |

## Saídas

O nó não possui tipos de saída.
