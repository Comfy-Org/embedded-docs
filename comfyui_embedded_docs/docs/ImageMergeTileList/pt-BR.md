# Mesclar Lista de Blocos em Imagem

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageMergeTileList/en.md)

Este nó recebe uma lista de blocos de imagem e os mescla de volta em uma única imagem maior. Ele foi projetado para reconstruir uma imagem que foi previamente dividida em uma grade de blocos sobrepostos, usando uma técnica de mesclagem ponderada para criar um resultado final contínuo e sem emendas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `image_list` | Uma lista de blocos de imagem a serem mesclados. O primeiro bloco da lista é usado para determinar as dimensões do bloco e o tipo de dados para todo o processo. | IMAGE | Sim | N/A |
| `final_width` | A largura da imagem mesclada final em pixels (padrão: 1024). | INT | Sim | 64 - 32768 |
| `final_height` | A altura da imagem mesclada final em pixels (padrão: 1024). | INT | Sim | 64 - 32768 |
| `overlap` | A quantidade de sobreposição entre blocos adjacentes em pixels. Um valor maior que 0 permite um efeito de mesclagem suave nas junções dos blocos (padrão: 128). | INT | Sim | 0 - 4096 |

**Nota:** A `image_list` é uma lista de entrada dinâmica. O nó processará os blocos na ordem em que forem fornecidos, até a quantidade necessária para preencher a grade definida por `final_width`, `final_height` e as dimensões do primeiro bloco. Se a lista contiver mais blocos do que o necessário, os blocos extras serão ignorados.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `image` | A imagem mesclada final, reconstruída a partir dos blocos de entrada. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageMergeTileList/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f8f770ca2e9806d2feb55bb1dfe2c26b09d7a3506caf664990d8536ec5660c92`
