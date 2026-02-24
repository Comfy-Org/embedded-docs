> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveVideo/pt-BR.md)

O nó SaveVideo salva o conteúdo de vídeo de entrada no diretório de saída do seu ComfyUI. Ele permite que você especifique o prefixo do nome do arquivo, o formato do vídeo e o codec para o arquivo salvo. O nó gerencia automaticamente a nomenclatura dos arquivos com incrementos de contador e pode incluir metadados do fluxo de trabalho no vídeo salvo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Sim | - | O vídeo a ser salvo. |
| `filename_prefix` | STRING | Não | - | O prefixo para o arquivo a ser salvo. Pode incluir informações de formatação como `%date:yyyy-MM-dd%` ou `%Empty Latent Image.width%` para incluir valores de outros nós (padrão: "video/ComfyUI"). |
| `format` | COMBO | Não | Múltiplas opções disponíveis | O formato para salvar o vídeo (padrão: "auto"). |
| `codec` | COMBO | Não | Múltiplas opções disponíveis | O codec a ser usado para o vídeo (padrão: "auto"). |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| *Nenhuma saída* | - | Este nó não retorna nenhum dado de saída. |
