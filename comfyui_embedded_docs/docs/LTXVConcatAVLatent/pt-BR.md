> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConcatAVLatent/pt-BR.md)

O nó LTXVConcatAVLatent combina uma representação latente de vídeo e uma representação latente de áudio em uma única saída latente concatenada. Ele mescla os tensores `samples` de ambas as entradas e, se presentes, seus tensores `noise_mask` também, preparando-os para processamento adicional em um pipeline de geração de vídeo.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `video_latent` | LATENT | Sim | | A representação latente dos dados de vídeo. |
| `audio_latent` | LATENT | Sim | | A representação latente dos dados de áudio. |

**Observação:** Os tensores `samples` das entradas `video_latent` e `audio_latent` são concatenados. Se qualquer uma das entradas contiver um `noise_mask`, ele será usado; se uma estiver faltando, uma máscara de valores 1 (com o mesmo formato do `samples` correspondente) será criada para ela. As máscaras resultantes também são então concatenadas.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `latent` | LATENT | Um único dicionário latente contendo os `samples` concatenados e, se aplicável, o `noise_mask` concatenado das entradas de vídeo e áudio. |
