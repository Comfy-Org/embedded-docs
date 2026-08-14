# LTXVDualCFGGuider

Este nó cria um objeto de amostragem guiada (orientador CFG) para modelos LTXV-AV. Ele aplica uma escala de orientação separada para a parte de vídeo e para a parte de áudio do latente empacotado, permitindo controlar a influência do condicionamento em cada modalidade de forma independente. Se as duas escalas forem iguais, ou se o latente não contiver componentes separados de vídeo e áudio, uma única escala geral será usada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo a ser usado durante a amostragem. | MODEL | Sim | - |
| `positive` | Condicionamento positivo para orientar a geração em direção ao desejado. | CONDITIONING | Sim | - |
| `negative` | Condicionamento negativo para afastar a geração do que não é desejado. | CONDITIONING | Sim | - |
| `video_cfg` | Intensidade da orientação aplicada à modalidade de vídeo do latente (padrão: 3.0). | FLOAT | Sim | 0.0 a 100.0 |
| `audio_cfg` | Intensidade da orientação aplicada à modalidade de áudio do latente (padrão: 7.0). | FLOAT | Sim | 0.0 a 100.0 |

Nota: Quando `video_cfg` e `audio_cfg` têm o mesmo valor, o orientador usa esse valor como uma única escala de CFG para todo o latente. Se o latente não for um latente LTXV-AV empacotado, apenas o valor de `video_cfg` é usado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `guider` | O orientador CFG configurado, para ser passado a um nó de amostragem. | GUIDER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVDualCFGGuider/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8b5ea32d0e73ab4f9b9f053ac7513d621fcc047e1ff468b6d0b5dd2aa3ff791a`
