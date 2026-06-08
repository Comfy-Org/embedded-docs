Gere música a partir de vídeo usando o modelo de IA da Sonilo. Este nó analisa o conteúdo de um vídeo de entrada e cria uma peça musical correspondente. Ele utiliza um serviço de IA externo para processar o vídeo e gerar o áudio.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `video` | Vídeo de entrada para gerar música. Duração máxima: 6 minutos. | VIDEO | Sim | - |
| `prompt` | Texto opcional para orientar a geração musical. Deixe vazio para melhor qualidade — o modelo analisará completamente o conteúdo do vídeo. (padrão: string vazia) | STRING | Não | - |
| `seed` | Semente para reprodutibilidade. Atualmente ignorada pelo serviço Sonilo, mas mantida para consistência do grafo. (padrão: 0) | INT | Não | 0 a 18446744073709551615 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `audio` | A música gerada como um arquivo de áudio. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloVideoToMusic/pt-BR.md)

---
**Source fingerprint (SHA-256):** `542fff1d8db8e48156bf9d1ff4690c91a7d71676332eef4708a6d36686abb31e`
