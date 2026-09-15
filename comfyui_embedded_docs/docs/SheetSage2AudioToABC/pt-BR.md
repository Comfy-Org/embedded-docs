# SheetSage2 Áudio para ABC

Este nó transcreve melodias vocais e instrumentais de música para notação ABC, um formato baseado em texto para escrever partituras musicais. Ele analisa o áudio conectado e retorna a notação resultante como texto, que pode então ser alimentada no nó YuE2 Generate Music usando o modo correspondente.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `audio_encoder` | O modelo codificador de áudio usado para analisar o áudio e produzir a notação ABC. | AUDIO_ENCODER | Sim | - |
| `audio` | O áudio musical a ser transcrito para notação ABC. | AUDIO | Sim | - |
| `mode` | Controla o que é transcrito. "full" gera melodia e acordes; "melody" gera apenas a melodia, recomendado para covers. | COMBO | Sim | `"melody"`<br>`"full"` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `abc` | A música transcrita em notação ABC, retornada como uma lista de strings. Conecte isto ao nó YuE2 Generate Music e use o modo correspondente. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SheetSage2AudioToABC/pt-BR.md)

---
**Source fingerprint (SHA-256):** `612d18dedd09b64210087c340b8f304ace8cd7b30b1a6e8e8ba7c749b355a497`
