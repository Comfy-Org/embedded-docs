# Kling Extender Vídeo

O nó de Extensão de Vídeo Kling permite estender vídeos criados por outros nós Kling. Ele recebe um vídeo existente identificado pelo seu ID e gera conteúdo adicional com base nos seus prompts de texto. O nó funciona enviando sua solicitação de extensão para a API Kling e retornando o vídeo estendido junto com seu novo ID e duração.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt de texto positivo para orientar a extensão do vídeo | STRING | Não | - |
| `negative_prompt` | Prompt de texto negativo para elementos a serem evitados no vídeo estendido | STRING | Não | - |
| `cfg_scale` | Controla a força da orientação do prompt (padrão: 0.5) | FLOAT | Não | 0.0 - 1.0 |
| `video_id` | O ID do vídeo a ser estendido. Suporta vídeos gerados por operações de texto-para-vídeo, imagem-para-vídeo e extensão de vídeo anterior. A duração total após a extensão não pode exceder 3 minutos. | STRING | Sim | - |

**Observação:** O `video_id` deve referenciar um vídeo criado por outros nós Kling, e a duração total após a extensão não pode exceder 3 minutos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | O vídeo estendido gerado pela API Kling | VIDEO |
| `video_id` | O identificador único para o vídeo estendido | STRING |
| `duration` | A duração do vídeo estendido | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVideoExtendNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ecef4aedffe83bf384f2f9c3d8840f3fcab4b8c21e6e9afb36e177abb6f069fd`
