> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVEmptyLatentAudio/pt-BR.md)

O nó LTXV Empty Latent Audio cria um lote de tensores latentes de áudio vazios (preenchidos com zeros). Ele usa a configuração de um modelo de VAE de Áudio fornecido para determinar as dimensões corretas para o espaço latente, como o número de canais e bins de frequência. Este latente vazio serve como ponto de partida para fluxos de trabalho de geração ou manipulação de áudio dentro do ComfyUI.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `frames_number` | INT | Sim | 1 a 1000 | Número de quadros. O valor padrão é 97. |
| `frame_rate` | INT | Sim | 1 a 1000 | Número de quadros por segundo. O valor padrão é 25. |
| `batch_size` | INT | Sim | 1 a 4096 | O número de amostras de áudio latente no lote. O valor padrão é 1. |
| `audio_vae` | VAE | Sim | N/A | O modelo de VAE de Áudio para obter a configuração. Este parâmetro é obrigatório. |

**Observação:** A entrada `audio_vae` é obrigatória. O nó gerará um erro se ela não for fornecida.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `Latent` | LATENT | Um tensor latente de áudio vazio com a estrutura (amostras, taxa_de_amostragem, tipo) configurada para corresponder ao VAE de Áudio de entrada. |
