# SalvarLatent

O nó SaveLatent salva amostras latentes em disco como arquivos `.latent` para uso ou compartilhamento posterior. Ele grava os dados do tensor latente na pasta de saída usando o prefixo de nome especificado e incorpora metadados opcionais, como informações do prompt. O nó também retorna as amostras latentes originais inalteradas, permitindo que o fluxo de trabalho continue usando-as.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `samples` | As amostras latentes a serem salvas em disco | LATENT | Sim | - |
| `filename_prefix` | O prefixo usado para gerar o nome do arquivo de saída e o caminho da subpasta (padrão: "latents/ComfyUI") | STRING | Sim | - |
| `prompt` | Os dados do prompt do fluxo de trabalho, armazenados como metadados JSON no arquivo salvo (entrada oculta, fornecida automaticamente) | PROMPT | Não | - |
| `extra_pnginfo` | Metadados adicionais do fluxo de trabalho, armazenados como JSON no arquivo salvo (entrada oculta, fornecida automaticamente) | EXTRA_PNGINFO | Não | - |

Nota: Os metadados são gravados no arquivo `.latent` salvo, a menos que o ComfyUI seja iniciado com o argumento `--disable-metadata`. O arquivo salvo é nomeado usando o padrão `{filename}_{contador de 5 dígitos}_.latent`, por exemplo `ComfyUI_00001_.latent`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `samples` | As amostras latentes originais, retornadas inalteradas | LATENT |
| `ui` | Detalhes do local do arquivo (nome do arquivo, subpasta e tipo de saída) para o arquivo latente salvo | UI |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLatent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `137d52d589d93d8229940a8572621ab6eeb25a4e13ac05172e9f8609f1af038a`
