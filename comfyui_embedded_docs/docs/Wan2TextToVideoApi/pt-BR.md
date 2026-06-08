Este nó gera um vídeo a partir de uma descrição textual usando o modelo Wan 2.7. Ele envia sua solicitação para uma API externa, que processa o prompt e retorna um arquivo de vídeo. Opcionalmente, você pode fornecer um clipe de áudio para influenciar o movimento e o ritmo do vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo específico a ser usado para a geração de vídeo. | COMBO | Sim | `"wan2.7-t2v"` |
| `model.prompt` | Uma descrição dos elementos e características visuais que você deseja no vídeo. Suporta inglês e chinês. | STRING | Sim | - |
| `model.negative_prompt` | Uma descrição de elementos ou características que você deseja evitar no vídeo gerado. | STRING | Não | - |
| `model.resolution` | A resolução do vídeo de saída. | COMBO | Sim | `"720P"`<br>`"1080P"` |
| `model.ratio` | A proporção de aspecto do vídeo de saída. | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `model.duration` | A duração do vídeo em segundos (padrão: 5). | INT | Sim | 2 a 15 |
| `áudio` | Um arquivo de áudio para orientar a geração do vídeo, como para sincronização labial ou movimento combinando com a batida. Se não fornecido, o modelo gerará música de fundo ou efeitos sonoros correspondentes. A duração do áudio deve estar entre 1,5 e 60 segundos. | AUDIO | Não | - |
| `semente` | Um número usado para controlar a aleatoriedade da geração, garantindo resultados reproduzíveis (padrão: 0). | INT | Não | 0 a 2147483647 |
| `estender_prompt` | Quando ativado, o prompt será aprimorado com assistência de IA (padrão: Verdadeiro). | BOOLEAN | Não | - |
| `marca_d'água` | Quando ativado, uma marca d'água gerada por IA será adicionada ao resultado (padrão: Falso). | BOOLEAN | Não | - |

**Observação:** O parâmetro `audio` é opcional. Se fornecido, sua duração deve estar entre 1,5 e 60 segundos. Se omitido, o modelo gerará áudio automaticamente.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2TextToVideoApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ce8a2f4e53b2bce879f143c66f6078fd81c6308e2822cb486b1cf8e178a6f58c`
