> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageSharpen/pt-BR.md)

O nó ImageSharpen melhora a nitidez de uma imagem ao acentuar suas bordas e detalhes. Ele aplica um filtro de nitidez à imagem, cuja intensidade e raio podem ser ajustados, fazendo com que a imagem pareça mais definida e nítida.

## Entradas

| Campo          | Tipo de Dados | Descrição                                                                                   |
|----------------|-------------|-----------------------------------------------------------------------------------------------|
| `image`        | `IMAGE`     | A imagem de entrada a ser nitidificada. Este parâmetro é crucial, pois determina a imagem base sobre a qual o efeito de nitidez será aplicado. |
| `sharpen_radius`| `INT`       | Define o raio do efeito de nitidez. Um raio maior significa que mais pixels ao redor da borda serão afetados, resultando em um efeito de nitidez mais pronunciado. |
| `sigma`        | `FLOAT`     | Controla a dispersão do efeito de nitidez. Um valor de sigma mais alto resulta em uma transição mais suave nas bordas, enquanto um sigma mais baixo torna a nitidez mais localizada. |
| `alpha`        | `FLOAT`     | Ajusta a intensidade do efeito de nitidez. Valores de alpha mais altos resultam em um efeito de nitidez mais forte. |

## Saídas

| Campo | Tipo de Dados | Descrição                                                              |
|-------|-------------|--------------------------------------------------------------------------|
| `image`| `IMAGE`     | A imagem nitidificada, com bordas e detalhes realçados, pronta para processamento adicional ou exibição. |
