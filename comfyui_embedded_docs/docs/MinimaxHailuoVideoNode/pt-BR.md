# MiniMax Hailuo Vídeo

Esta documentação foi gerada por IA. Caso encontre erros ou tenha sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuoVideoNode/en.md)

Gera vídeos a partir de prompts de texto usando o modelo MiniMax Hailuo-02. Opcionalmente, você pode fornecer uma imagem inicial como primeiro quadro para criar um vídeo que continua a partir dessa imagem.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `texto_prompt` | Prompt de texto para guiar a geração do vídeo. | STRING | Sim | - |
| `semente` | A semente aleatória usada para criar o ruído (padrão: 0). | INT | Não | 0 a 18446744073709551615 |
| `imagem_primeiro_quadro` | Imagem opcional para usar como primeiro quadro para gerar um vídeo. | IMAGE | Não | - |
| `otimizador_de_prompt` | Otimizar o prompt para melhorar a qualidade da geração quando necessário (padrão: True). | BOOLEAN | Não | - |
| `duração` | A duração do vídeo de saída em segundos (padrão: 6). | COMBO | Não | `6`<br>`10` |
| `resolução` | As dimensões da exibição do vídeo. 1080p é 1920x1080, 768p é 1366x768 (padrão: "768P"). | COMBO | Não | `"768P"`<br>`"1080P"` |

**Observação:** Ao usar o modelo MiniMax-Hailuo-02 com resolução 1080P, a duração é limitada a 6 segundos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuoVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5466b9cda979a30158b818743de0e0cf30eb3e27015d431eb04a370029250a4c`
