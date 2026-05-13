> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConcatAVLatent/pt-BR.md)

O nó LTXVConcatAVLatent combina uma representação latente de vídeo e uma representação latente de áudio em uma única saída latente concatenada. Ele mescla os tensores `samples` de ambas as entradas e, se presentes, seus tensores `noise_mask`, preparando-os para processamento adicional em um pipeline de geração de vídeo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `video_latent` | LATENT | Sim | | A representação latente dos dados de vídeo. |
| `audio_latent` | LATENT | Sim | | A representação latente dos dados de áudio. |

**Nota:** Os tensores `samples` das entradas `video_latent` e `audio_latent` são concatenados. Se alguma das entradas contiver um `noise_mask`, ele será utilizado; se uma delas estiver ausente, uma máscara de uns (com a mesma forma dos `samples` correspondentes) é criada para ela. As máscaras resultantes são então também concatenadas.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `latent` | LATENT | Um único dicionário latente contendo os `samples` concatenados e, se aplicável, o `noise_mask` concatenado das entradas de vídeo e áudio. |

---
**Source fingerprint (SHA-256):** `322d6870f110fb1ef8b472cb49649cc9fff7865f4c7a83fbfd536f1fdfd694f8`
