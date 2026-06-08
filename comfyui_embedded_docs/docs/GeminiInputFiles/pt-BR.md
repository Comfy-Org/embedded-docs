Carrega e formata arquivos de entrada para uso com a API Gemini. Este nó permite que usuários incluam arquivos de texto (.txt) e PDF (.pdf) como contexto de entrada para o modelo Gemini. Os arquivos são convertidos para o formato apropriado exigido pela API e podem ser encadeados para incluir múltiplos arquivos em uma única requisição.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `arquivo` | Arquivos de entrada para incluir como contexto para o modelo. Atualmente, aceita apenas arquivos de texto (.txt) e PDF (.pdf). Os arquivos devem ser menores que o limite máximo de tamanho de arquivo de entrada. | COMBO | Sim | Múltiplas opções disponíveis |
| `GEMINI_INPUT_FILES` | Um ou mais arquivos adicionais opcionais para agrupar junto com o arquivo carregado por este nó. Permite o encadeamento de arquivos de entrada para que uma única mensagem possa incluir múltiplos arquivos de entrada. | GEMINI_INPUT_FILES | Não | N/A |

**Nota:** O parâmetro `file` exibe apenas arquivos de texto (.txt) e PDF (.pdf) que sejam menores que o limite máximo de tamanho de arquivo de entrada. Os arquivos são automaticamente filtrados e ordenados por nome.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `GEMINI_INPUT_FILES` | Dados de arquivo formatados prontos para uso com nós Gemini LLM, contendo o conteúdo do arquivo carregado no formato apropriado da API. | GEMINI_INPUT_FILES |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiInputFiles/pt-BR.md)

---
**Source fingerprint (SHA-256):** `54da8696d144513efa9660fbc5ddbf5480da12eafe4d2791c8e81cd207ef8a52`
