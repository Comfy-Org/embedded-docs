> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSave/pt-BR.md)

O nó ModelSave salva modelos treinados ou modificados no armazenamento do seu computador. Ele recebe um modelo como entrada e o grava em um arquivo com o nome especificado por você. Isso permite que você preserve seu trabalho e reutilize modelos em projetos futuros.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sim | - | O modelo a ser salvo no disco |
| `filename_prefix` | STRING | Sim | - | O prefixo do nome do arquivo e do caminho para o arquivo do modelo salvo (padrão: "diffusion_models/ComfyUI") |
| `prompt` | PROMPT | Não | - | Informações do prompt do fluxo de trabalho (fornecido automaticamente) |
| `extra_pnginfo` | EXTRA_PNGINFO | Não | - | Metadados adicionais do fluxo de trabalho (fornecido automaticamente) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| *Nenhuma* | - | Este nó não retorna nenhum valor de saída |
