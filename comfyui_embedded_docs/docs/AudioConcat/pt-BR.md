Esta documentação foi gerada por IA. Se encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioConcat/en.md)

O nó AudioConcat combina duas entradas de áudio unindo-as. Ele recebe duas entradas de áudio e as conecta na ordem especificada, colocando o segundo áudio antes ou depois do primeiro. O nó lida automaticamente com diferentes formatos de áudio, convertendo áudio mono para estéreo e equalizando as taxas de amostragem entre as duas entradas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `audio1` | A primeira entrada de áudio a ser concatenada | AUDIO | Sim | - |
| `audio2` | A segunda entrada de áudio a ser concatenada | AUDIO | Sim | - |
| `direção` | Se deve anexar audio2 após ou antes de audio1 (padrão: "after") | COMBO | Sim | `"after"`<br>`"before"` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `AUDIO` | O áudio combinado contendo ambos os arquivos de áudio de entrada unidos | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioConcat/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b54046e29761cf27bc5b1c065dac87846613afc0b5cbb296632628bf7d4527b7`
