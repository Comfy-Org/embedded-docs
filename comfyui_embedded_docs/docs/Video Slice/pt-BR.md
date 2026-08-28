# Corte de Vídeo

O nó Video Slice permite extrair um segmento específico de um vídeo. Você pode definir um tempo de início e uma duração para cortar o vídeo, ou simplesmente pular os primeiros quadros. Se a duração solicitada for maior que o restante do vídeo, o nó pode retornar o que estiver disponível ou gerar um erro.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `vídeo` | O vídeo de entrada a ser recortado. | VIDEO | Sim | - |
| `início` | Tempo de início em segundos (padrão: 0.0). | FLOAT | Sim | -1e5 a 1e5 |
| `duração` | Duração em segundos, ou 0 para duração ilimitada (padrão: 0.0). | FLOAT | Sim | 0.0 e acima |
| `duração_estrita` | Se True, quando a duração especificada não for possível, um erro será gerado (padrão: False). | BOOLEAN | Sim | - |

**Nota:** Se o vídeo não puder ser recortado para o `start_time` e `duration` fornecidos, o nó gera um erro. Quando `strict_duration` é False, o nó retorna a parte disponível do vídeo quando a duração solicitada excede a duração restante; quando True, gera um erro em vez disso.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `video` | O segmento de vídeo cortado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Video Slice/pt-BR.md)

---
**Source fingerprint (SHA-256):** `439b76528742c1fbe230eee9502e945847ae99a58a9bd81a7a7dc3b20e15d450`
