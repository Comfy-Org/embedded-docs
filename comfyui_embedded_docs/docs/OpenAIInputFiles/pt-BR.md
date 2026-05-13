> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIInputFiles/pt-BR.md)

Carrega e formata arquivos de entrada para a API OpenAI. Este nó prepara arquivos de texto (.txt) e PDF (.pdf) para serem incluídos como entradas de contexto para o Nó de Chat OpenAI. Os arquivos serão lidos pelo modelo OpenAI ao gerar uma resposta. Vários nós de Arquivos de Entrada OpenAI podem ser encadeados para incluir vários arquivos em uma única mensagem.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `arquivo` | COMBO | Sim | Várias opções disponíveis (todos os arquivos .txt e .pdf no diretório de entrada com menos de 32MB) | Arquivos de entrada a serem incluídos como contexto para o modelo. Aceita apenas arquivos de texto (.txt) e PDF (.pdf) por enquanto. Os arquivos devem ser menores que 32MB. |
| `OPENAI_INPUT_FILES` | OPENAI_INPUT_FILES | Não | N/D | Um arquivo(s) adicional(is) opcional(is) para agrupar com o arquivo carregado deste nó. Permite o encadeamento de arquivos de entrada para que uma única mensagem possa incluir vários arquivos de entrada. |

**Restrições de Arquivo:**

- Apenas arquivos .txt e .pdf são suportados
- Tamanho máximo do arquivo: 32MB
- Os arquivos são carregados do diretório de entrada do ComfyUI

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `OPENAI_INPUT_FILES` | OPENAI_INPUT_FILES | Arquivos de entrada formatados prontos para serem usados como contexto para chamadas da API OpenAI. |

---
**Source fingerprint (SHA-256):** `e5e92f6628072da9af787867e38c89dde3db853b7289ef6c607a066cd04c1cc9`
