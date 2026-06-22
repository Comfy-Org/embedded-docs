# Aumentar Resolução da Imagem

O nó ImageScale foi projetado para redimensionar imagens para dimensões específicas, oferecendo uma seleção de métodos de upscale e a capacidade de cortar a imagem redimensionada. Ele abstrai a complexidade do upscaling e corte de imagens, fornecendo uma interface direta para modificar as dimensões da imagem de acordo com parâmetros definidos pelo usuário.

## Entradas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `imagem` | A imagem de entrada a ser ampliada. Este parâmetro é central para a operação do nó, servindo como o dado principal sobre o qual as transformações de redimensionamento são aplicadas. A qualidade e as dimensões da imagem de saída são diretamente influenciadas pelas propriedades da imagem original. | `IMAGE` |
| `método de upscaling` | Especifica o método usado para ampliar a imagem. A escolha do método pode afetar a qualidade e as características da imagem ampliada, influenciando a fidelidade visual e possíveis artefatos na saída redimensionada. | COMBO[STRING] |
| `largura` | A largura desejada para a imagem ampliada. Este parâmetro influencia diretamente as dimensões da imagem de saída, determinando a escala horizontal da operação de redimensionamento. | `INT` |
| `altura` | A altura desejada para a imagem ampliada. Este parâmetro influencia diretamente as dimensões da imagem de saída, determinando a escala vertical da operação de redimensionamento. | `INT` |
| `cortar` | Determina se e como a imagem ampliada deve ser cortada, oferecendo opções para corte desativado ou corte centralizado. Isso afeta a composição final da imagem, potencialmente removendo bordas para se ajustar às dimensões especificadas. | COMBO[STRING] |

## Saídas

| Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `imagem` | A imagem ampliada (e opcionalmente cortada), pronta para processamento adicional ou visualização. | `IMAGE` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScale/pt-BR.md)
