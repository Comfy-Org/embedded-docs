> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioConcat/pt-BR.md)

O nó AudioConcat combina duas entradas de áudio juntando-as. Ele recebe duas entradas de áudio e as conecta na ordem que você especificar, posicionando o segundo áudio antes ou depois do primeiro. O nó gerencia automaticamente diferentes formatos de áudio convertendo áudio mono para estéreo e igualando as taxas de amostragem entre as duas entradas.

## Entradas

| Parâmetro | Tipo de Dados | Tipo de Entrada | Padrão | Intervalo | Descrição |
|-----------|-----------|------------|---------|-------|-------------|
| `audio1` | AUDIO | obrigatória | - | - | A primeira entrada de áudio a ser concatenada |
| `audio2` | AUDIO | obrigatória | - | - | A segunda entrada de áudio a ser concatenada |
| `direction` | COMBO | obrigatória | after | ['after', 'before'] | Se deve anexar o `audio2` depois ou antes do `audio1` |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `AUDIO` | AUDIO | O áudio combinado contendo ambos os arquivos de áudio de entrada unidos |
