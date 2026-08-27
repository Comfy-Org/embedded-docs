# Separar latente AV

O nó LTXVSeparateAVLatent divide um latente audiovisual combinado em dois latentes separados: um contendo os dados de vídeo e outro contendo os dados de áudio. Isso funciona com qualquer modelo audiovisual, como LTXV ou MiniMax H3. O tensor de amostras é dividido ao longo de sua primeira dimensão, com o primeiro elemento se tornando o latente de vídeo e o segundo elemento se tornando o latente de áudio; se uma máscara de ruído estiver presente, ela é dividida da mesma forma.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `av_latent` | A representação latente audiovisual combinada a ser dividida em latentes de vídeo e áudio. | LATENT | Sim | N/A |

**Nota:** Espera-se que o tensor `samples` do latente de entrada tenha pelo menos dois elementos ao longo da primeira dimensão (dimensão do lote). O primeiro elemento é usado para o latente de vídeo, e o segundo elemento é usado para o latente de áudio. Se um `noise_mask` estiver presente, ele é dividido da mesma forma.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `video_latent` | A representação latente contendo os dados de vídeo separados. | LATENT |
| `audio_latent` | A representação latente contendo os dados de áudio separados. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateAVLatent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `22ed38bbc1b5716cee380c35c50455810f79c273f51bbe6a535c9ae33192afe6`
