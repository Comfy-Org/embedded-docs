# Corte de Vídeo

O nó Video Slice permite extrair um segmento específico de um vídeo. Você pode definir um tempo inicial e uma duração para cortar o vídeo, ou simplesmente pular os frames iniciais. Se a duração solicitada for maior que o vídeo restante, o nó pode retornar o que estiver disponível ou gerar um erro.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `video` | O vídeo de entrada a ser cortado. | VIDEO | Sim | - |
| `start_time` | Tempo inicial em segundos (padrão: 0.0). | FLOAT | Não | -1e5 a 1e5 |
| `duration` | Duração em segundos, ou 0 para duração ilimitada (padrão: 0.0). | FLOAT | Não | 0.0 e acima |
| `strict_duration` | Se True, quando a duração especificada não for possível, um erro será gerado (padrão: False). | BOOLEAN | Não | - |

Nota: Quando `duration` é 0, o nó corta do `start_time` até o final do vídeo. Se o segmento solicitado não puder ser criado — por exemplo, porque `start_time` está além do final do vídeo — o nó gera um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `video` | O segmento de vídeo extraído. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Video Slice/pt-BR.md)

---
**Source fingerprint (SHA-256):** `439b76528742c1fbe230eee9502e945847ae99a58a9bd81a7a7dc3b20e15d450`
