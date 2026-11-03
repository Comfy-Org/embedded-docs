# Sonilo Music 1.5

O nó Sonilo Music 1.5 gera uma música completa com vocais cantados a partir de um prompt de texto. Descreva o gênero, o clima, os instrumentos e os vocais e, opcionalmente, forneça suas próprias letras; o nó envia a solicitação ao serviço Sonilo e retorna a faixa finalizada como áudio. Use-o quando precisar de uma música completa em vez de um clipe instrumental.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `prompt` | Descrição da música: gênero, clima, instrumentos e vocais. Para definir as palavras você mesmo, adicione um bloco `Lyrics:` com as tags `[Verse]` e `[Chorus]`; sem ele, o modelo escreve suas próprias letras. Deve ter de 1 a 2000 caracteres após remover espaços em branco. | STRING | Sim | 1 a 2000 caracteres |
| `duration` | `auto` ajusta a duração da música às letras. `custom` usa o valor de `seconds`, cortando letras que não se encaixam e repetindo as curtas. | DYNAMIC_COMBO | Sim | `"auto"`<br>`"custom"` |
| `seed` | A seed controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da seed (padrão: 42). | INT | Sim | 0 a 18446744073709551615 |

### Parâmetros de duração personalizada (quando `duration` é `"custom"`)

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `seconds` | Duração da música gerada em segundos (padrão: 60). | INT | Sim | 10 a 360 |

**Observação:** A entrada `prompt` é obrigatória e não pode estar vazia. O nó valida que ela contém pelo menos 1 caractere após remover espaços em branco e no máximo 2000.

**Observação:** O uso é cobrado a $0.0032175 por segundo da duração solicitada, e o indicador de preço acompanha `duration.seconds` quando `custom` está selecionado.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `audio` | A música gerada, incluindo vocais, como um arquivo de áudio. | AUDIO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloMusic15/pt-BR.md)

---
**Source fingerprint (SHA-256):** `65ccf74ccdfa7a710d8c7bd9871e666d79ceadc7304644fe0101956832ca6024`
