> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEDecode/pt-BR.md)

O nó LTXV Audio VAE Decode converte uma representação latente de áudio de volta para uma forma de onda de áudio. Ele utiliza um modelo especializado de Audio VAE para realizar esse processo de decodificação, produzindo uma saída de áudio com uma taxa de amostragem específica.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `samples` | LATENT | Sim | N/A | O latente a ser decodificado. |
| `audio_vae` | VAE | Sim | N/A | O modelo Audio VAE usado para decodificar o latente. |

**Nota:** Se o latente fornecido for aninhado (contiver múltiplos latentes), o nó usará automaticamente o último latente da sequência para a decodificação.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `Audio` | AUDIO | A forma de onda de áudio decodificada e sua taxa de amostragem associada. A forma de onda é um tensor movido para o mesmo dispositivo do latente de entrada, e a taxa de amostragem é determinada pelo modelo Audio VAE. |

---
**Source fingerprint (SHA-256):** `e9df1da8ca0424cfc7ce97951e65154df845d98c3b73f76725fa657d851a3a07`
