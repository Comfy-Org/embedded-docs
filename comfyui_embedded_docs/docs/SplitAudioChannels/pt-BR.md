> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitAudioChannels/pt-BR.md)

O nó SplitAudioChannels separa um áudio estéreo em canais individuais esquerdo e direito. Ele recebe uma entrada de áudio estéreo com dois canais e gera dois fluxos de áudio separados, um para o canal esquerdo e outro para o canal direito.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Sim | - | A entrada de áudio estéreo a ser separada em canais |

**Observação:** O áudio de entrada deve ter exatamente dois canais (estéreo). O nó gerará um erro se o áudio de entrada tiver apenas um canal.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `left` | AUDIO | O áudio do canal esquerdo separado |
| `right` | AUDIO | O áudio do canal direito separado |
