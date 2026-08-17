# MiniMax Hailuo Vídeo

Gera vídeos a partir de prompts de texto usando o modelo MiniMax Hailuo-02. Você pode opcionalmente fornecer uma imagem inicial como o primeiro quadro para criar um vídeo que continua a partir dessa imagem.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt_text` | Prompt de texto para orientar a geração do vídeo. | STRING | Sim | - |
| `seed` | A semente aleatória usada para criar o ruído (padrão: 0). | INT | Não | 0 to 18446744073709551615 |
| `first_frame_image` | Imagem opcional para usar como o primeiro quadro para gerar um vídeo. | IMAGE | Não | - |
| `prompt_optimizer` | Otimiza o prompt para melhorar a qualidade da geração quando necessário (padrão: True). | BOOLEAN | Não | - |
| `duration` | A duração do vídeo de saída em segundos (padrão: 6). | COMBO | Não | `6`<br>`10` |
| `resolution` | As dimensões da exibição do vídeo. 1080p é 1920x1080, 768p é 1366x768 (padrão: "768P"). | COMBO | Não | `"768P"`<br>`"1080P"` |

**Notas:**
- `prompt_text` deve ser uma string não vazia quando nenhum `first_frame_image` for fornecido.
- Ao usar o modelo MiniMax-Hailuo-02 com resolução 1080P, a duração é limitada a 6 segundos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuoVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f371aae15cfbe7353236bc679c8a6d558703c5037e49ab7ddb9bdf5c50ef0995`
