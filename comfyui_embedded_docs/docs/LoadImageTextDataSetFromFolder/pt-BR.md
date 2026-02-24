> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageTextDataSetFromFolder/pt-BR.md)

Este nó carrega um conjunto de dados de imagens e suas legendas de texto correspondentes a partir de uma pasta especificada. Ele procura por arquivos de imagem e automaticamente busca arquivos `.txt` correspondentes com o mesmo nome base para usar como legendas. O nó também suporta uma estrutura de pastas específica onde subpastas podem ser nomeadas com um prefixo numérico (como `10_nome_da_pasta`) para indicar que as imagens dentro dela devem ser repetidas várias vezes na saída.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `folder` | COMBO | Sim | *Carregado dinamicamente de `folder_paths.get_input_subfolders()`* | A pasta da qual carregar as imagens. As opções disponíveis são os subdiretórios dentro do diretório de entrada do ComfyUI. |

**Observação:** O nó espera uma estrutura de arquivos específica. Para cada arquivo de imagem (`.png`, `.jpg`, `.jpeg`, `.webp`), ele procurará por um arquivo `.txt` com o mesmo nome para usar como legenda. Se um arquivo de legenda não for encontrado, uma string vazia será usada. O nó também suporta uma estrutura especial onde o nome de uma subpasta começa com um número e um sublinhado (ex.: `5_gatos`), o que fará com que todas as imagens dentro dessa subpasta sejam repetidas esse número de vezes na lista de saída final.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `images` | IMAGE | Uma lista de tensores de imagem carregados. |
| `texts` | STRING | Uma lista de legendas de texto correspondentes a cada imagem carregada. |
