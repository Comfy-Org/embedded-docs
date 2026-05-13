> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecordAudio/pt-BR.md)

O nó RecordAudio carrega arquivos de áudio que foram gravados ou selecionados através da interface de gravação de áudio. Ele processa o arquivo de áudio e o converte em um formato de forma de onda que pode ser utilizado por outros nós de processamento de áudio no fluxo de trabalho. O nó detecta automaticamente a taxa de amostragem e prepara os dados de áudio para manipulações posteriores.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `audio` | AUDIO_RECORD | Sim | N/A | A entrada de gravação de áudio proveniente da interface de gravação de áudio |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `AUDIO` | AUDIO | Os dados de áudio processados contendo informações de forma de onda e taxa de amostragem |

---
**Source fingerprint (SHA-256):** `3648f3c71f60f69e9ca117e25e9706187470866a1869ba9b8e5feceb42a7493a`
