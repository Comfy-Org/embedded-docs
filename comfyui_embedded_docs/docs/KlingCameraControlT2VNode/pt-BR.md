> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControlT2VNode/pt-BR.md)

Nó de Controle de Câmera Kling para Texto para Vídeo transforma texto em vídeos cinematográficos com movimentos profissionais de câmera que simulam a cinematografia do mundo real. Este nó suporta o controle de ações de câmera virtual, incluindo zoom, rotação, panorâmica, inclinação e visão em primeira pessoa, mantendo o foco no seu texto original. A duração, o modo e o nome do modelo são codificados porque o controle de câmera é suportado apenas no modo profissional com o modelo kling-v1-5 na duração de 5 segundos.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `prompt` | STRING | Sim | - | Prompt de texto positivo |
| `negative_prompt` | STRING | Sim | - | Prompt de texto negativo |
| `cfg_scale` | FLOAT | Não | 0.0-1.0 | Controla o quão fielmente a saída segue o prompt (padrão: 0,75) |
| `aspect_ratio` | COMBO | Não | "16:9"<br>"9:16"<br>"1:1"<br>"21:9"<br>"3:4"<br>"4:3" | A proporção de aspecto para o vídeo gerado (padrão: "16:9") |
| `camera_control` | CAMERA_CONTROL | Não | - | Pode ser criado usando o nó Controles de Câmera Kling. Controla o movimento e a ação da câmera durante a geração do vídeo. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | VIDEO | O vídeo gerado com efeitos de controle de câmera |
| `video_id` | STRING | O identificador único para o vídeo gerado |
| `duration` | STRING | A duração do vídeo gerado |

---
**Source fingerprint (SHA-256):** `4ebdd6af31f9e5c0816c4bcba886179b3f7d2b5030ff4fa3ddad6df25c528af7`
