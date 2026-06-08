O nó Pika Text2Video v2.2 envia um prompt de texto para a API Pika versão 2.2 para gerar um vídeo. Ele converte sua descrição textual em um vídeo usando o serviço de geração de vídeo por IA da Pika. O nó permite personalizar vários aspectos do processo de geração de vídeo, incluindo proporção de aspecto, duração e resolução.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt_text` | A descrição textual principal que descreve o que você deseja gerar no vídeo | STRING | Sim | - |
| `negative_prompt` | Texto descrevendo o que você não deseja que apareça no vídeo gerado | STRING | Sim | - |
| `seed` | Um número que controla a aleatoriedade da geração para resultados reproduzíveis | INT | Sim | - |
| `resolution` | A configuração de resolução para o vídeo de saída | STRING | Sim | - |
| `duration` | A duração do vídeo em segundos | INT | Sim | - |
| `aspect_ratio` | Proporção de aspecto (largura / altura) (padrão: 1,7777777777777777) | FLOAT | Não | 0,4 - 2,5 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O arquivo de vídeo gerado retornado pela API Pika | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaTextToVideoNode2_2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b4287519f5d4cc4a1077a58fb13aa99697e3be038a0b382c4b4c9b0e53a0d8a8`
