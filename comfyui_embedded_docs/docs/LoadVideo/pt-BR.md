> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideo/pt-BR.md)

O nó Load Video carrega arquivos de vídeo do diretório de entrada e os disponibiliza para processamento no fluxo de trabalho. Ele lê arquivos de vídeo da pasta de entrada designada e os emite como dados de vídeo que podem ser conectados a outros nós de processamento de vídeo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `file` | STRING | Sim | Múltiplas opções disponíveis | O arquivo de vídeo a ser carregado do diretório de entrada |

**Observação:** As opções disponíveis para o parâmetro `file` são preenchidas dinamicamente a partir dos arquivos de vídeo presentes no diretório de entrada. Apenas arquivos de vídeo com tipos de conteúdo suportados são exibidos.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `video` | VIDEO | Os dados de vídeo carregados que podem ser passados para outros nós de processamento de vídeo |
