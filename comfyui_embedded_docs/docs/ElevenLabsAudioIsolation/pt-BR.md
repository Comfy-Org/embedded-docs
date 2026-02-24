> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsAudioIsolation/pt-BR.md)

O nó ElevenLabs Voice Isolation remove ruídos de fundo de um arquivo de áudio, isolando os vocais ou a fala. Ele envia o áudio para a API da ElevenLabs para processamento e retorna o áudio limpo.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Sim | | Áudio a ser processado para remoção de ruído de fundo. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `audio` | AUDIO | O áudio processado com o ruído de fundo removido. |
