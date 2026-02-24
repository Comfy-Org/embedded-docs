> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRANode/pt-BR.md)

O nó SaveLoRA salva modelos LoRA (Low-Rank Adaptation) no seu diretório de saída. Ele recebe um modelo LoRA como entrada e cria um arquivo safetensors com um nome de arquivo gerado automaticamente. Você pode personalizar o prefixo do nome do arquivo e, opcionalmente, incluir a contagem de etapas de treinamento no nome do arquivo para uma melhor organização.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `lora` | LORA_MODEL | Sim | - | O modelo LoRA a ser salvo. Não use o modelo com camadas LoRA. |
| `prefix` | STRING | Sim | - | O prefixo a ser usado para o arquivo LoRA salvo (padrão: "loras/ComfyUI_trained_lora"). |
| `steps` | INT | Não | - | Opcional: O número de etapas para as quais o LoRA foi treinado, usado para nomear o arquivo salvo. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| *Nenhuma* | - | Este nó não retorna nenhuma saída, mas salva o modelo LoRA no diretório de saída. |
