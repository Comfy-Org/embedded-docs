# Separar latente AV

O nó LTXVSeparateAVLatent recebe uma representação latente audiovisual combinada e a divide em dois latents separados: um para vídeo e um para áudio. Ele funciona com qualquer modelo audiovisual, como LTXV ou MiniMax H3.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `av_latent` | A representação latente audiovisual combinada a ser separada. | LATENT | Sim | N/A |

**Observação:** O tensor `samples` do latent de entrada deve ter pelo menos dois elementos na primeira dimensão (dimensão do lote). O primeiro elemento é usado para o latent de vídeo, e o segundo elemento é usado para o latent de áudio. Se houver um `noise_mask`, ele é dividido da mesma forma.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `video_latent` | A representação latente contendo os dados de vídeo separados. | LATENT |
| `audio_latent` | A representação latente contendo os dados de áudio separados. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateAVLatent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `22ed38bbc1b5716cee380c35c50455810f79c273f51bbe6a535c9ae33192afe6`
