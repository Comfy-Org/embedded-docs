# MiniMax Hailuo Vídeo

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `texto_prompt` | Prompt de texto para orientar a geração do vídeo. | STRING | Sim | - |
| `semente` | A semente aleatória usada para criar o ruído (padrão: 0). | INT | Não | 0 a 18446744073709551615 |
| `imagem_primeiro_quadro` | Imagem opcional para usar como primeiro quadro a fim de gerar um vídeo. | IMAGE | Não | - |
| `otimizador_de_prompt` | Otimiza o prompt para melhorar a qualidade da geração quando necessário (padrão: True). | BOOLEAN | Não | True<br>False |
| `duração` | A duração do vídeo de saída em segundos (padrão: 6). | COMBO | Não | 6<br>10 |
| `resolução` | As dimensões da exibição do vídeo. 1080p é 1920x1080, 768p é 1366x768 (padrão: "768P"). | COMBO | Não | "768P"<br>"1080P" |

**Observação:** Quando `resolution` estiver definido como "1080P", `duration` fica limitado a 6 segundos. Quando `first_frame_image` não for fornecido, `prompt_text` não deve estar vazio.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuoVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f371aae15cfbe7353236bc679c8a6d558703c5037e49ab7ddb9bdf5c50ef0995`
