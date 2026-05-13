> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentImage/pt-BR.md)

O nó `EmptyLatentImage` foi projetado para gerar uma representação em espaço latente em branco com dimensões e tamanho de lote especificados. Este nó serve como uma etapa fundamental na geração ou manipulação de imagens no espaço latente, fornecendo um ponto de partida para processos posteriores de síntese ou modificação de imagens.

## Entradas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|-------------|-----------|
| `largura`   | `INT`       | Especifica a largura da imagem latente a ser gerada. Este parâmetro influencia diretamente as dimensões espaciais da representação latente resultante. |
| `altura`  | `INT`       | Determina a altura da imagem latente a ser gerada. Este parâmetro é crucial para definir as dimensões espaciais da representação no espaço latente. |
| `tamanho_do_lote` | `INT` | Controla o número de imagens latentes a serem geradas em um único lote. Isso permite a geração simultânea de múltiplas representações latentes, facilitando o processamento em lote. |

## Saídas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|-------------|-----------|
| `latent`  | `LATENT`    | A saída é um tensor representando um lote de imagens latentes em branco, servindo como base para geração ou manipulação adicional de imagens no espaço latente. |