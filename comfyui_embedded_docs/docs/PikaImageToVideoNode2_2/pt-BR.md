# PikaImageToVideoNode2_2

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaImageToVideoNode2_2/en.md)

O nó Pika Image to Video envia uma imagem e um prompt de texto para a API Pika versão 2.2 para gerar um vídeo. Ele converte sua imagem de entrada em formato de vídeo com base na descrição e nas configurações fornecidas. O nó gerencia a comunicação com a API e retorna o vídeo gerado como saída.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `image` | A imagem a ser convertida em vídeo | IMAGE | Sim | - |
| `prompt_text` | A descrição textual que orienta a geração do vídeo | STRING | Sim | - |
| `negative_prompt` | Texto descrevendo o que deve ser evitado no vídeo | STRING | Sim | - |
| `seed` | Valor de semente aleatória para resultados reproduzíveis | INT | Sim | - |
| `resolution` | Configuração de resolução do vídeo de saída | STRING | Sim | - |
| `duration` | Duração do vídeo gerado em segundos | INT | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O arquivo de vídeo gerado | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaImageToVideoNode2_2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `aaa8dc49b94f0fae2010a3b61a3fb41e212fa9d2946a934a1a7c651fdced81b3`
