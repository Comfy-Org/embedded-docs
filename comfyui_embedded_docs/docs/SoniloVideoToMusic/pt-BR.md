> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloVideoToMusic/pt-BR.md)

Gere música a partir de vídeo usando o modelo de IA da Sonilo. Este nó analisa o conteúdo de um vídeo de entrada e cria uma peça musical correspondente. Ele utiliza um serviço de IA externo para processar o vídeo e gerar o áudio.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `video` | VIDEO | Sim | - | Vídeo de entrada para gerar música. Duração máxima: 6 minutos. |
| `prompt` | STRING | Não | - | Texto opcional para orientar a geração musical. Deixe vazio para melhor qualidade — o modelo analisará completamente o conteúdo do vídeo. (padrão: string vazia) |
| `seed` | INT | Não | 0 a 18446744073709551615 | Semente para reprodutibilidade. Atualmente ignorada pelo serviço Sonilo, mas mantida para consistência do grafo. (padrão: 0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `audio` | AUDIO | A música gerada como um arquivo de áudio. |