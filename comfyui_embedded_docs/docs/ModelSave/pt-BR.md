> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSave/pt-BR.md)

O nó ModelSave salva modelos treinados ou modificados no armazenamento do seu computador. Ele recebe um modelo como entrada e o grava em um arquivo com o nome de arquivo especificado por você. Isso permite preservar seu trabalho e reutilizar modelos em projetos futuros.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|-----------|----------|-------|-------------|
| `modelo` | MODEL | Sim | - | O modelo a ser salvo em disco |
| `prefixo_do_arquivo` | STRING | Sim | - | O prefixo do nome do arquivo e caminho para o arquivo do modelo salvo (padrão: "diffusion_models/ComfyUI") |
| `prompt` | PROMPT | Não | - | Informações do prompt do fluxo de trabalho (fornecido automaticamente) |
| `extra_pnginfo` | EXTRA_PNGINFO | Não | - | Metadados adicionais do fluxo de trabalho (fornecido automaticamente) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| *Nenhum* | - | Este nó não retorna nenhum valor de saída |

---
**Source fingerprint (SHA-256):** `1dda8a6d85aa19b739c1fe3e6e7f816e05011044fc8b0b91b23fa303f71d8b19`
