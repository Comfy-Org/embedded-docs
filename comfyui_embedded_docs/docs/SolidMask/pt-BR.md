> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SolidMask/pt-BR.md)

O nó SolidMask gera uma máscara uniforme com um valor especificado em toda a sua área. Ele foi projetado para criar máscaras com dimensões e intensidade específicas, úteis em várias tarefas de processamento de imagem e mascaramento.

## Entradas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|-------------|-------------|
| `value`   | FLOAT       | Especifica o valor de intensidade da máscara, afetando sua aparência geral e utilidade em operações subsequentes. |
| `width`   | INT         | Determina a largura da máscara gerada, influenciando diretamente seu tamanho e proporção. |
| `height`  | INT         | Define a altura da máscara gerada, afetando seu tamanho e proporção. |

## Saídas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|-------------|-------------|
| `mask`    | MASK        | Emite uma máscara uniforme com as dimensões e o valor especificados. |
