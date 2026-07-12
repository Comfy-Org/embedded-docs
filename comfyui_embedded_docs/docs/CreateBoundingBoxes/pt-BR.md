# Criar Caixas Delimitadoras

Este nó fornece uma interface de tela para desenhar caixas delimitadoras ao redor de objetos ou regiões de texto em uma imagem. Ele gera as coordenadas das caixas delimitadoras no espaço de pixels, dados de elementos estruturados compatíveis com a formatação de prompt do Ideogram e uma imagem de pré-visualização mostrando as caixas desenhadas com rótulos e paletas de cores.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|--------------|-------------|-----------|
| `fundo` | Imagem opcional usada como fundo na tela e na pré-visualização. | IMAGE | Não | - |
| `largura` | Largura da tela e da grade de pixels para as caixas delimitadoras (padrão: 1024). | INT | Sim | 64 a 16384 (passo: 16) |
| `altura` | Altura da tela e da grade de pixels para as caixas delimitadoras (padrão: 1024). | INT | Sim | 64 a 16384 (passo: 16) |
| `estado_do_editor` | Desenhe caixas delimitadoras e defina o tipo, texto, descrição e paleta de cores de cada caixa. Comece com o elemento de fundo primeiro e o de primeiro plano por último. | BOUNDING_BOXES | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `preview` | Uma imagem RGB mostrando a tela com todas as caixas delimitadoras renderizadas, incluindo rótulos, amostras da paleta de cores e texto descritivo. | IMAGE |
| `bboxes` | Uma lista de caixas delimitadoras em coordenadas de pixels, com cada caixa contendo valores de x, y, largura e altura. | BOUNDING_BOX |
| `elements` | Uma matriz estruturada de objetos de elemento, cada um contendo tipo, coordenadas da caixa delimitadora (normalizadas de 0 a 1000), texto (para tipo texto), descrição e paleta de cores. | ARRAY |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateBoundingBoxes/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a63939f13edc6c6507590a390dcd6d0a3321febb5831baab1655d9952228612c`
