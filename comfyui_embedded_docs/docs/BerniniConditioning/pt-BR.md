# BerniniConditioning

O nó BerniniConditioning prepara dados de condicionamento de vídeo e imagem para o modelo Wan2.2-A14B. Ele codifica vídeos fonte, vídeos de referência e imagens de referência usando o VAE fornecido, em seguida os anexa aos dados de condicionamento para tarefas de geração em contexto.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `positive` | Dados de condicionamento positivo | CONDITIONING | Sim | - |
| `negative` | Dados de condicionamento negativo | CONDITIONING | Sim | - |
| `vae` | Modelo VAE usado para codificar entradas de vídeo e imagem | VAE | Sim | - |
| `width` | Largura do latente de saída (padrão: 832) | INT | Sim | 16 a 8192 (passo: 16) |
| `height` | Altura do latente de saída (padrão: 480) | INT | Sim | 16 a 8192 (passo: 16) |
| `length` | Número de quadros no latente de saída (padrão: 81) | INT | Sim | 1 a 8192 (passo: 4) |
| `batch_size` | Número de vídeos a serem gerados em um único lote (padrão: 1) | INT | Sim | 1 a 4096 |
| `source_video` | Vídeo fonte para editar ou reestilizar (v2v, rv2v). Redimensionado para largura/altura e cortado para o comprimento especificado. | IMAGE | Não | - |
| `reference_video` | Vídeo a ser inserido no vídeo fonte (ads2v). | IMAGE | Não | - |
| `reference_images` | Imagens de referência injetadas como tokens em contexto (r2v, rv2v). Até 8 imagens podem ser fornecidas. | IMAGE | Não | 0 a 8 imagens |
| `ref_max_size` | Tamanho máximo para a borda longa do vídeo de referência e imagens de referência. Redimensionado com proporção preservada e ajustado para 16px (padrão: 848). | INT | Não | 16 a 8192 (passo: 16) |

**Observação:** A tarefa é inferida a partir de quais entradas estão conectadas:
- Nenhuma entrada conectada → texto-para-vídeo (t2v)
- Apenas `source_video` → vídeo-para-vídeo (v2v)
- `source_video` + `reference_images` → edição de vídeo guiada por referência (rv2v)
- Apenas `reference_images` → referência-para-vídeo (r2v)
- `source_video` + `reference_video` → inserir imagem/vídeo em vídeo (ads2v)

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|-------------|-------------|-----------|
| `positive` | Condicionamento positivo com latentes de contexto anexados | CONDITIONING |
| `negative` | Condicionamento negativo com latentes de contexto anexados | CONDITIONING |
| `latent` | Tensor latente vazio com dimensões correspondentes à largura, altura, comprimento e tamanho do lote especificados | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BerniniConditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3535bbe9a1ae007dc579242b44787ab315479a820eb0da680eab9b870ab60699`
