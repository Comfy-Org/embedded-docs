# Kling Imagem para Vídeo (Controle de Câmera)

Este documento foi gerado por IA. Caso encontre erros ou tenha sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControlI2VNode/en.md)

O nó de Controle de Câmera do Kling Image to Video transforma imagens estáticas em vídeos cinematográficos com movimentos profissionais de câmera. Este nó especializado de imagem para vídeo permite controlar ações virtuais de câmera, incluindo zoom, rotação, panorâmica, inclinação e visão em primeira pessoa, mantendo o foco na imagem original. O controle de câmera atualmente é suportado apenas no modo pro com o modelo kling-v1-5 com duração de 5 segundos.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `quadro_inicial` | Imagem de Referência - URL ou string codificada em Base64, não pode exceder 10MB, resolução mínima de 300x300px, proporção entre 1:2.5 e 2.5:1. O Base64 não deve incluir o prefixo data:image. | IMAGE | Sim | - |
| `prompt` | Prompt de texto positivo descrevendo o conteúdo desejado do vídeo | STRING | Sim | - |
| `prompt_negativo` | Prompt de texto negativo descrevendo o que evitar no vídeo gerado | STRING | Sim | - |
| `cfg_scale` | Controla a intensidade da orientação do texto. Valores mais altos fazem com que a saída siga mais fielmente o prompt (padrão: 0.75) | FLOAT | Não | 0.0 a 1.0 |
| `proporcao` | A proporção de aspecto do vídeo gerado (padrão: "16:9") | COMBO | Não | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `controle_de_camera` | Pode ser criado usando o nó de Controles de Câmera Kling. Controla o movimento e a ação da câmera durante a geração do vídeo. | CAMERA_CONTROL | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | A saída do vídeo gerado | VIDEO |
| `video_id` | Identificador único para o vídeo gerado | STRING |
| `duration` | Duração do vídeo gerado | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControlI2VNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a2965975cd484768298f4c7e504423f782ea032dfb5ef304579715be9c27cb79`
