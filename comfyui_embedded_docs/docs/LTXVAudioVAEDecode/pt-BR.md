# LTXV Decodificar Áudio VAE

O nó LTXV Audio VAE Decode converte uma representação latente de áudio de volta em uma forma de onda de áudio. Ele usa um modelo Audio VAE especializado para realizar esse processo de decodificação, produzindo uma saída de áudio com sua taxa de amostragem associada.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `amostras` | A representação latente a ser decodificada. | LATENT | Sim | N/A |
| `audio_vae` | O modelo Audio VAE usado para decodificar o latente. | VAE | Sim | N/A |

**Nota:** Se o latente fornecido estiver aninhado (contiver vários latentes), o nó usa automaticamente o último latente da sequência para a decodificação.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `Áudio` | A forma de onda de áudio decodificada e sua taxa de amostragem associada. A forma de onda é colocada no mesmo dispositivo do latente de entrada, e a taxa de amostragem é determinada pelo modelo Audio VAE. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEDecode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `fc94f3cb78ede86ada374444d613411cc9bb5849e5cdb8a24074babee50719b1`
