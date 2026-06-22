# CLIPTextEncodeSDXL

Este nó foi projetado para codificar entrada de texto usando um modelo CLIP especificamente personalizado para a arquitetura SDXL. Ele utiliza um sistema de codificação dupla (CLIP-L e CLIP-G) para processar descrições textuais, resultando em uma geração de imagens mais precisa.

## Entradas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `clip` | Instância do modelo CLIP usada para codificação de texto. | CLIP |
| `largura` | Especifica a largura da imagem em pixels, padrão 1024. | INT |
| `altura` | Especifica a altura da imagem em pixels, padrão 1024. | INT |
| `recorte_largura` | Largura da área de corte em pixels, padrão 0. | INT |
| `recorte_altura` | Altura da área de corte em pixels, padrão 0. | INT |
| `largura_alvo` | Largura alvo para a imagem de saída, padrão 1024. | INT |
| `altura_alvo` | Altura alvo para a imagem de saída, padrão 1024. | INT |
| `texto_g` | Descrição textual global para a descrição geral da cena. | STRING |
| `texto_l` | Descrição textual local para a descrição de detalhes. | STRING |

## Saídas

| Parâmetro | Descrição | Tipo de Dados |
| --- | --- | --- |
| `CONDITIONING` | Contém o texto codificado e as informações condicionais necessárias para a geração da imagem. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSDXL/pt-BR.md)
