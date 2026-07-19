# LTXVSeparateAVLatent

O nó LTXVSeparateAVLatent recebe uma representação latente audiovisual combinada e a divide em duas partes distintas: uma para vídeo e outra para áudio. Ele separa as amostras e, se presente, as máscaras de ruído do latente de entrada, criando dois novos objetos latentes.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `av_latent` | A representação latente audiovisual combinada a ser separada. | LATENT | Sim | N/A |

**Nota:** O tensor `samples` do latente de entrada deve ter pelo menos dois elementos ao longo da primeira dimensão (dimensão do lote). O primeiro elemento é usado para o latente de vídeo, e o segundo elemento é usado para o latente de áudio. Se uma `noise_mask` estiver presente, ela é dividida da mesma forma.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `video_latent` | A representação latente contendo os dados de vídeo separados. | LATENT |
| `audio_latent` | A representação latente contendo os dados de áudio separados. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateAVLatent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `55bce5d768e7fe13f885cc32d34ecdac5cdcbb667b03743004866ea4b6d58d46`
