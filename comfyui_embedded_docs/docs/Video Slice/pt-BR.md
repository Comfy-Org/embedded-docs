> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Video Slice/pt-BR.md)

O nó Video Slice permite extrair um segmento específico de um vídeo. Você pode definir um tempo inicial e uma duração para cortar o vídeo, ou simplesmente pular os quadros iniciais. Se a duração solicitada for maior que o restante do vídeo, o nó pode retornar o que estiver disponível ou gerar um erro.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `video` | VIDEO | Sim | - | O vídeo de entrada a ser cortado. |
| `start_time` | FLOAT | Não | -1e5 a 1e5 | Tempo inicial em segundos (padrão: 0,0). |
| `duration` | FLOAT | Não | 0,0 e acima | Duração em segundos, ou 0 para duração ilimitada (padrão: 0,0). |
| `strict_duration` | BOOLEAN | Não | - | Se Verdadeiro, quando a duração especificada não for possível, um erro será gerado (padrão: Falso). |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `video` | VIDEO | O segmento de vídeo cortado. |

---
**Source fingerprint (SHA-256):** `5e3e3e69931a25183eb01b7b87ec12cbf9f5a748781993dcbeec7a6d5f7260c1`
