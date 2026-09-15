# LTXV Dual CFG Guider

Este nó cria um objeto de amostragem guiada (CFG guider) para modelos LTXV-AV. Ele aplica uma escala de orientação separada à parte de vídeo e à parte de áudio de um latente LTXV-AV empacotado, permitindo controlar a influência do condicionamento em cada modalidade independentemente. Se as duas escalas forem iguais, ou se o latente não contiver componentes separados de vídeo e áudio, uma única escala geral será usada em vez disso.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo a ser usado durante a amostragem. | MODEL | Sim | - |
| `positive` | Condicionamento positivo para orientar a geração em direção a ele. | CONDITIONING | Sim | - |
| `negative` | Condicionamento negativo para afastar a geração dele. | CONDITIONING | Sim | - |
| `video_cfg` | Força de orientação aplicada à modalidade de vídeo do latente (padrão: 3.0). | FLOAT | Sim | 0.0 a 100.0 |
| `audio_cfg` | Força de orientação aplicada à modalidade de áudio do latente (padrão: 7.0). | FLOAT | Sim | 0.0 a 100.0 |

Observação: Quando `video_cfg` e `audio_cfg` são iguais (ou muito próximos em valor), o guia usa esse valor como uma única escala CFG para todo o latente. Se o latente não for um latente LTXV-AV empacotado, apenas o valor de `video_cfg` será usado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `guider` | O guia CFG configurado a ser passado para um nó de amostragem. | GUIDER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVDualCFGGuider/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8b5ea32d0e73ab4f9b9f053ac7513d621fcc047e1ff468b6d0b5dd2aa3ff791a`
