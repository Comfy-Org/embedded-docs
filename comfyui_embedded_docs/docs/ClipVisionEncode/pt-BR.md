O nó `CLIP Vision Encode` é um nó de codificação de imagem no ComfyUI, utilizado para converter imagens de entrada em vetores de características visuais por meio do modelo CLIP Vision. Este nó é uma ponte importante entre a compreensão de imagens e texto, sendo amplamente utilizado em diversos fluxos de trabalho de geração e processamento de imagens com IA.

**Funcionalidade do Nó**

- **Extração de características da imagem**: Converte imagens de entrada em vetores de características de alta dimensão
- **Integração multimodal**: Fornece a base para o processamento conjunto de imagens e texto
- **Geração condicional**: Fornece condições visuais para geração condicional baseada em imagens

## Entradas

| Nome do Parâmetro | Descrição | Tipo de Dado |
| --- | --- | --- |
| `clip_vision` | Modelo de visão CLIP, geralmente carregado através do nó CLIPVisionLoader | CLIP_VISION |
| `imagem` | A imagem de entrada a ser codificada | IMAGE |
| `recorte` | Método de corte da imagem, opções: center (corte centralizado), none (sem corte) | Dropdown |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| CLIP_VISION_OUTPUT | Características visuais codificadas | CLIP_VISION_OUTPUT |

Este objeto de saída contém:

- `last_hidden_state`: O último estado oculto
- `image_embeds`: Vetor de incorporação da imagem
- `penultimate_hidden_states`: O penúltimo estado oculto
- `mm_projected`: Resultado da projeção multimodal (se disponível)

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPVisionEncode/pt-BR.md)
