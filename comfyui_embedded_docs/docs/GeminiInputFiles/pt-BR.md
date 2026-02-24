> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiInputFiles/pt-BR.md)

Carrega e formata arquivos de entrada para uso com a API Gemini. Este nó permite que os usuários incluam arquivos de texto (.txt) e PDF (.pdf) como contexto de entrada para o modelo Gemini. Os arquivos são convertidos para o formato apropriado exigido pela API e podem ser encadeados para incluir múltiplos arquivos em uma única requisição.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `file` | COMBO | Sim | Múltiplas opções disponíveis | Arquivos de entrada para incluir como contexto para o modelo. Atualmente, aceita apenas arquivos de texto (.txt) e PDF (.pdf). Os arquivos devem ser menores que o limite máximo de tamanho de arquivo de entrada. |
| `GEMINI_INPUT_FILES` | GEMINI_INPUT_FILES | Não | N/A | Um ou mais arquivos adicionais opcionais para agrupar com o arquivo carregado por este nó. Permite o encadeamento de arquivos de entrada para que uma única mensagem possa incluir múltiplos arquivos. |

**Observação:** O parâmetro `file` exibe apenas arquivos de texto (.txt) e PDF (.pdf) que são menores que o limite máximo de tamanho de arquivo de entrada. Os arquivos são automaticamente filtrados e ordenados por nome.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `GEMINI_INPUT_FILES` | GEMINI_INPUT_FILES | Dados do arquivo formatados e prontos para uso com os nós LLM do Gemini, contendo o conteúdo do arquivo carregado no formato apropriado para a API. |
