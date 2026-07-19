# Carregar Conjunto de Dados de Imagem e Texto da Pasta

Este nó carrega um conjunto de dados de imagens e suas respectivas legendas de texto a partir de uma pasta especificada. Ele busca arquivos de imagem e automaticamente procura por arquivos `.txt` correspondentes com o mesmo nome base para usar como legendas. O nó também suporta uma estrutura de pastas específica onde subpastas podem ser nomeadas com um prefixo numérico (como `10_nome_da_pasta`) para indicar que as imagens dentro delas devem ser repetidas várias vezes na saída.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `pasta` | A pasta de onde carregar as imagens. As opções disponíveis são os subdiretórios dentro do diretório de entrada do ComfyUI. | COMBO | Sim | *Carregado dinamicamente de `folder_paths.get_input_subfolders()`* |

**Observação:** O nó espera uma estrutura de arquivos específica. Para cada arquivo de imagem (`.png`, `.jpg`, `.jpeg`, `.webp`), ele procurará um arquivo `.txt` com o mesmo nome para usar como legenda. Se um arquivo de legenda não for encontrado, uma string vazia é usada. O nó também suporta uma estrutura especial onde o nome de uma subpasta começa com um número e um sublinhado (por exemplo, `5_gatos`), o que fará com que todas as imagens dentro dessa subpasta sejam repetidas aquele número de vezes na lista final de saída.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `images` | Uma lista de tensores de imagem carregados. | IMAGE |
| `texts` | Uma lista de legendas de texto correspondentes a cada imagem carregada. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageTextDataSetFromFolder/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e176f35118f08ea397c63f5b6f347d9cdb3dc1a08db7ad7a5cc8255e1526e6ca`
