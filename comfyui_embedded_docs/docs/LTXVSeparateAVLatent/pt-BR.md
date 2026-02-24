> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateAVLatent/pt-BR.md)

O nó LTXVSeparateAVLatent recebe uma representação latente audiovisual combinada e a divide em duas partes distintas: uma para vídeo e outra para áudio. Ele separa as amostras e, se presente, as máscaras de ruído do latente de entrada, criando dois novos objetos latentes.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `av_latent` | LATENT | Sim | N/A | A representação latente audiovisual combinada a ser separada. |

**Observação:** Espera-se que o tensor `samples` do latente de entrada tenha pelo menos dois elementos ao longo da primeira dimensão (dimensão do lote). O primeiro elemento é usado para o latente de vídeo e o segundo elemento é usado para o latente de áudio. Se uma `noise_mask` estiver presente, ela é dividida da mesma maneira.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `video_latent` | LATENT | A representação latente contendo os dados de vídeo separados. |
| `audio_latent` | LATENT | A representação latente contendo os dados de áudio separados. |
