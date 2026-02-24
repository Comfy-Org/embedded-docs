> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScale/pt-BR.md)

O nó ImageScale é projetado para redimensionar imagens para dimensões específicas, oferecendo uma seleção de métodos de ampliação e a capacidade de recortar a imagem redimensionada. Ele abstrai a complexidade da ampliação e do recorte de imagens, fornecendo uma interface direta para modificar as dimensões da imagem de acordo com parâmetros definidos pelo usuário.

## Entradas

| Parâmetro       | Tipo de Dado | Descrição                                                                           |
|-----------------|-------------|---------------------------------------------------------------------------------------|
| `image`         | `IMAGE`     | A imagem de entrada a ser ampliada. Este parâmetro é central para a operação do nó, servindo como o dado primário sobre o qual as transformações de redimensionamento são aplicadas. A qualidade e as dimensões da imagem de saída são diretamente influenciadas pelas propriedades da imagem original. |
| `upscale_method`| COMBO[STRING] | Especifica o método usado para ampliar a imagem. A escolha do método pode afetar a qualidade e as características da imagem ampliada, influenciando a fidelidade visual e possíveis artefatos na saída redimensionada. |
| `width`         | `INT`       | A largura alvo para a imagem ampliada. Este parâmetro influencia diretamente as dimensões da imagem de saída, determinando a escala horizontal da operação de redimensionamento. |
| `height`        | `INT`       | A altura alvo para a imagem ampliada. Este parâmetro influencia diretamente as dimensões da imagem de saída, determinando a escala vertical da operação de redimensionamento. |
| `crop`          | COMBO[STRING] | Determina se e como a imagem ampliada deve ser recortada, oferecendo opções para desabilitar o recorte ou para recorte central. Isso afeta a composição final da imagem, potencialmente removendo bordas para se ajustar às dimensões especificadas. |

## Saídas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|-------------|-------------|
| `image`   | `IMAGE`     | A imagem ampliada (e opcionalmente recortada), pronta para processamento adicional ou visualização. |
