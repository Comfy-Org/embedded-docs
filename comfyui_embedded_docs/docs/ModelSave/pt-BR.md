O nó ModelSave salva modelos treinados ou modificados no armazenamento do seu computador. Ele recebe um modelo como entrada e o grava em um arquivo com o nome de arquivo especificado por você. Isso permite preservar seu trabalho e reutilizar modelos em projetos futuros.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo a ser salvo em disco | MODEL | Sim | - |
| `prefixo_do_arquivo` | O prefixo do nome do arquivo e caminho para o arquivo do modelo salvo (padrão: "diffusion_models/ComfyUI") | STRING | Sim | - |
| `prompt` | Informações do prompt do fluxo de trabalho (fornecido automaticamente) | PROMPT | Não | - |
| `extra_pnginfo` | Metadados adicionais do fluxo de trabalho (fornecido automaticamente) | EXTRA_PNGINFO | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| *Nenhum* | Este nó não retorna nenhum valor de saída | - |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSave/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1dda8a6d85aa19b739c1fe3e6e7f816e05011044fc8b0b91b23fa303f71d8b19`
