> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEDecode/pt-BR.md)

O nó **LTXV Audio VAE Decode** converte uma representação latente de áudio de volta em uma forma de onda de áudio. Ele utiliza um modelo especializado de Audio VAE para realizar esse processo de decodificação, produzindo uma saída de áudio com uma taxa de amostragem específica.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `samples` | LATENT | Sim | N/A | O latente a ser decodificado. |
| `audio_vae` | VAE | Sim | N/A | O modelo Audio VAE utilizado para decodificar o latente. |

**Observação:** Se o latente fornecido estiver aninhado (contiver múltiplos latentes), o nó usará automaticamente o último latente na sequência para a decodificação.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `Audio` | AUDIO | A forma de onda de áudio decodificada e sua taxa de amostragem associada. |
