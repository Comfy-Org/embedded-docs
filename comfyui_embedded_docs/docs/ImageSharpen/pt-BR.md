# Aumentar Nitidez da Imagem

O nó **ImageSharpen** melhora a nitidez de uma imagem acentuando suas bordas e detalhes. Ele aplica um filtro de nitidez à imagem, que pode ser ajustado em intensidade e raio, fazendo com que a imagem pareça mais definida e nítida.

## Entradas

| Campo | Descrição | Tipo de Dados |
| --- | --- | --- |
| `imagem` | A imagem de entrada a ser nitidada. Este parâmetro é crucial, pois determina a imagem base na qual o efeito de nitidez será aplicado. | `IMAGE` |
| `raio de nitidez` | Define o raio do efeito de nitidez. Um raio maior significa que mais pixels ao redor da borda serão afetados, resultando em um efeito de nitidez mais pronunciado. | `INT` |
| `sigma` | Controla a dispersão do efeito de nitidez. Um valor de sigma mais alto resulta em uma transição mais suave nas bordas, enquanto um sigma mais baixo torna a nitidez mais localizada. | `FLOAT` |
| `alfa` | Ajusta a intensidade do efeito de nitidez. Valores de alpha mais altos resultam em um efeito de nitidez mais forte. | `FLOAT` |

## Saídas

| Campo | Descrição | Tipo de Dados |
| --- | --- | --- |
| `imagem` | A imagem nitidada, com bordas e detalhes realçados, pronta para processamento ou exibição adicional. | `IMAGE` |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageSharpen/pt-BR.md)
