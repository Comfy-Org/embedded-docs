> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Video Slice/pt-BR.md)

O nó Video Slice permite extrair um segmento específico de um vídeo. Você pode definir um horário de início e uma duração para cortar o vídeo, ou simplesmente pular os quadros iniciais. Se a duração solicitada for maior que o restante do vídeo, o nó pode retornar o que estiver disponível ou gerar um erro.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Sim | - | O vídeo de entrada a ser cortado. |
| `start_time` | FLOAT | Não | -1e5 a 1e5 | O horário de início em segundos a partir do qual o corte deve começar. Um valor negativo pulará quadros do início do vídeo. (padrão: 0.0) |
| `duration` | FLOAT | Não | 0.0 e acima | O comprimento do corte em segundos. Um valor de 0.0 significa que o nó retornará todo o vídeo do horário de início até o final. (padrão: 0.0) |
| `strict_duration` | BOOLEAN | Não | - | Se definido como Verdadeiro, o nó gerará um erro se a duração solicitada não puder ser atendida (por exemplo, se o corte ultrapassar o final do vídeo). Se Falso, ele retornará o vídeo disponível até o final. (padrão: Falso) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `video` | VIDEO | O segmento de vídeo cortado. |