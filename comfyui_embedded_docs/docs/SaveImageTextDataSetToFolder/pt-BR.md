# Salvar Conjunto de Imagens e Textos na Pasta

O nó Salvar Imagem e Dataset de Texto em Pasta salva uma lista de imagens e suas respectivas legendas de texto em uma pasta especificada dentro do diretório de saída do ComfyUI. Para cada imagem salva como arquivo PNG, um arquivo de texto correspondente com o mesmo nome base é criado para armazenar sua legenda. Isso é útil para criar conjuntos de dados organizados de imagens geradas e suas descrições.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `imagens` | Lista de imagens a serem salvas. | IMAGE | Sim | - |
| `textos` | Lista de legendas de texto a serem salvas. | STRING | Sim | - |
| `nome_da_pasta` | Nome da pasta para salvar as imagens (dentro do diretório de saída). (padrão: "dataset") | STRING | Não | - |
| `prefixo_do_arquivo` | Prefixo para os nomes dos arquivos de imagem salvos. (padrão: "image") | STRING | Não | - |

**Observação:** As entradas `images` e `texts` são listas. O nó espera que o número de legendas de texto corresponda ao número de imagens fornecidas. Cada legenda será salva em um arquivo `.txt` correspondente à sua imagem emparelhada.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| - | Este nó não possui saídas. Ele salva arquivos diretamente no sistema de arquivos. | - |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageTextDataSetToFolder/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0c76f623e97b1502c850e0a59dc9edd7c241bcd823f5e32a8dcdd8b8160d2e44`
