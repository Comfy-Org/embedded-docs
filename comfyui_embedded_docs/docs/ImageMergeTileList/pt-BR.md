> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageMergeTileList/pt-BR.md)

Esta documentação foi gerada por IA. Se encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageMergeTileList/en.md)

Este nó recebe uma lista de blocos de imagem e os mescla novamente em uma única imagem maior. Ele foi projetado para reconstruir uma imagem que foi previamente dividida em uma grade de blocos sobrepostos, utilizando uma técnica de mesclagem ponderada para criar um resultado final contínuo.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `image_list` | IMAGE | Sim | N/A | Uma lista de blocos de imagem a serem mesclados. O primeiro bloco da lista é usado para determinar as dimensões do bloco e o tipo de dados para todo o processo. |
| `final_width` | INT | Não | 64 - 32768 | A largura da imagem mesclada final em pixels (padrão: 1024). |
| `final_height` | INT | Não | 64 - 32768 | A altura da imagem mesclada final em pixels (padrão: 1024). |
| `overlap` | INT | Não | 0 - 4096 | A quantidade de sobreposição entre blocos adjacentes em pixels. Um valor maior que 0 permite um efeito de mesclagem suave nas bordas dos blocos (padrão: 128). |

**Nota:** A `image_list` é uma lista de entrada dinâmica. O nó processará os blocos na ordem em que são fornecidos, até o número necessário para preencher a grade definida pela `final_width`, `final_height` e as dimensões do primeiro bloco. Se a lista contiver mais blocos do que o necessário, os blocos extras serão ignorados.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `image` | IMAGE | A imagem mesclada final, reconstruída a partir dos blocos de entrada. |