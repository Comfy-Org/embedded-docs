> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSDXL/pt-BR.md)

Este nó foi projetado para codificar entrada de texto usando um modelo CLIP especificamente personalizado para a arquitetura SDXL. Ele utiliza um sistema de codificador duplo (CLIP-L e CLIP-G) para processar descrições de texto, resultando em uma geração de imagem mais precisa.

## Entradas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-----------|-------------|
| `clip` | CLIP | Instância do modelo CLIP usada para a codificação de texto. |
| `width` | INT | Especifica a largura da imagem em pixels, padrão 1024. |
| `height` | INT | Especifica a altura da imagem em pixels, padrão 1024. |
| `crop_w` | INT | Largura da área de recorte em pixels, padrão 0. |
| `crop_h` | INT | Altura da área de recorte em pixels, padrão 0. |
| `target_width` | INT | Largura alvo para a imagem de saída, padrão 1024. |
| `target_height` | INT | Altura alvo para a imagem de saída, padrão 1024. |
| `text_g` | STRING | Descrição de texto global para a descrição geral da cena. |
| `text_l` | STRING | Descrição de texto local para detalhamento. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Contém o texto codificado e as informações condicionais necessárias para a geração da imagem. |
