> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoaderSimple/pt-BR.md)

Este é um nó carregador de modelos que carrega arquivos de modelo de locais especificados e os decompõe em três componentes principais: o modelo principal, o codificador de texto e o codificador/decodificador de imagem.

Este nó detecta automaticamente todos os arquivos de modelo na pasta `ComfyUI/models/checkpoints`, bem como caminhos adicionais configurados no seu arquivo `extra_model_paths.yaml`.

1. **Compatibilidade do Modelo**: Certifique-se de que o modelo selecionado é compatível com seu fluxo de trabalho. Diferentes tipos de modelo (como SD1.5, SDXL, Flux, etc.) precisam ser emparelhados com amostradores e outros nós correspondentes.
2. **Gerenciamento de Arquivos**: Coloque os arquivos de modelo na pasta `ComfyUI/models/checkpoints`, ou configure outros caminhos através do arquivo `extra_model_paths.yaml`.
3. **Atualização da Interface**: Se novos arquivos de modelo forem adicionados enquanto o ComfyUI está em execução, você precisa atualizar o navegador (Ctrl+R) para ver os novos arquivos na lista suspensa.

## Entradas

| Parâmetro     | Tipo de Dado | Tipo de Entrada | Padrão | Intervalo | Descrição |
|---------------|--------------|-----------------|--------|-----------|-----------|
| `ckpt_name`   | STRING       | Widget          | null   | Todos os arquivos de modelo na pasta de checkpoints | Selecione o nome do arquivo de modelo de checkpoint para carregar, o que determina o modelo de IA usado para a geração de imagem subsequente |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `MODEL`       | MODEL        | O modelo de difusão principal usado para a geração de remoção de ruído de imagem, o componente central da criação de imagem por IA |
| `CLIP`        | CLIP         | O modelo usado para codificar prompts de texto, convertendo descrições de texto em informações que a IA pode entender |
| `VAE`         | VAE          | O modelo usado para codificação e decodificação de imagem, responsável pela conversão entre o espaço de pixels e o espaço latente |
