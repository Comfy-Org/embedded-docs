> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIInputFiles/pt-BR.md)

Carrega e formata arquivos de entrada para a API da OpenAI. Este nó prepara arquivos de texto e PDF para serem incluídos como entradas de contexto para o Nó de Chat da OpenAI. Os arquivos serão lidos pelo modelo da OpenAI ao gerar respostas. Vários nós de arquivos de entrada podem ser encadeados para incluir múltiplos arquivos em uma única mensagem.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `file` | COMBO | Sim | Múltiplas opções disponíveis | Arquivos de entrada para incluir como contexto para o modelo. Atualmente, aceita apenas arquivos de texto (.txt) e PDF (.pdf). Os arquivos devem ter menos de 32MB. |
| `OPENAI_INPUT_FILES` | OPENAI_INPUT_FILES | Não | N/A | Um(s) arquivo(s) adicional(is) opcional(is) para agrupar junto com o arquivo carregado por este nó. Permite o encadeamento de arquivos de entrada para que uma única mensagem possa incluir múltiplos arquivos. |

**Restrições de Arquivo:**

- Apenas arquivos .txt e .pdf são suportados
- Tamanho máximo do arquivo: 32MB
- Os arquivos são carregados do diretório de entrada

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `OPENAI_INPUT_FILES` | OPENAI_INPUT_FILES | Arquivos de entrada formatados e prontos para serem usados como contexto para chamadas da API da OpenAI. |
