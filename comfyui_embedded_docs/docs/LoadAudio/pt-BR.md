> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadAudio/pt-BR.md)

O nó LoadAudio carrega arquivos de áudio do diretório de entrada e os converte em um formato que pode ser processado por outros nós de áudio no ComfyUI. Ele lê os arquivos de áudio e extrai tanto os dados da forma de onda quanto a taxa de amostragem, disponibilizando-os para tarefas subsequentes de processamento de áudio.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Sim | Todos os arquivos de áudio/vídeo suportados no diretório de entrada | O arquivo de áudio a ser carregado do diretório de entrada |

**Observação:** O nó aceita apenas arquivos de áudio e vídeo que estão presentes no diretório de entrada do ComfyUI. O arquivo deve existir e estar acessível para que o carregamento seja bem-sucedido.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `AUDIO` | AUDIO | Dados de áudio contendo informações da forma de onda e da taxa de amostragem |
