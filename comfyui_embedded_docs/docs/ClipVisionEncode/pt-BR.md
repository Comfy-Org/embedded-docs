> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPVisionEncode/pt-BR.md)

O nó `CLIP Vision Encode` é um nó de codificação de imagem no ComfyUI, usado para converter imagens de entrada em vetores de características visuais por meio do modelo CLIP Vision. Este nó é uma ponte importante que conecta a compreensão de imagem e texto, sendo amplamente utilizado em vários fluxos de trabalho de geração e processamento de imagens de IA.

**Funcionalidade do Nó**

- **Extração de características da imagem**: Converte imagens de entrada em vetores de características de alta dimensão
- **Ponte multimodal**: Fornece uma base para o processamento conjunto de imagens e texto
- **Geração condicional**: Fornece condições visuais para geração condicional baseada em imagem

## Entradas

| Nome do Parâmetro | Tipo de Dados | Descrição                                                      |
| -------------- | -----------  | --------------------------------------------------------------- |
| `clip_vision`  | CLIP_VISION  | Modelo de visão CLIP, geralmente carregado via o nó CLIPVisionLoader |
| `image`        | IMAGE        | A imagem de entrada a ser codificada                                   |
| `crop`         | Dropdown     | Método de recorte da imagem, opções: center (recorte central), none (sem recorte) |

## Saídas

| Nome da Saída         | Tipo de Dados           | Descrição                |
| ------------------- | ------------------ | -------------------------- |
| CLIP_VISION_OUTPUT  | CLIP_VISION_OUTPUT | Características visuais codificadas    |

Este objeto de saída contém:

- `last_hidden_state`: O último estado oculto
- `image_embeds`: Vetor de incorporação da imagem
- `penultimate_hidden_states`: O penúltimo estado oculto
- `mm_projected`: Resultado da projeção multimodal (se disponível)
