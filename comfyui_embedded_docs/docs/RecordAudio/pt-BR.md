> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecordAudio/pt-BR.md)

O nó RecordAudio carrega arquivos de áudio que foram gravados ou selecionados através da interface de gravação de áudio. Ele processa o arquivo de áudio e o converte para um formato de forma de onda que pode ser utilizado por outros nós de processamento de áudio no fluxo de trabalho. O nó detecta automaticamente a taxa de amostragem e prepara os dados de áudio para manipulação posterior.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO_RECORD | Sim | N/A | A entrada de gravação de áudio proveniente da interface de gravação de áudio |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `AUDIO` | AUDIO | Os dados de áudio processados, contendo informações da forma de onda e da taxa de amostragem |
