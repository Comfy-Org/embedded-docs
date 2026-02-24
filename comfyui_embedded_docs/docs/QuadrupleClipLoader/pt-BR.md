> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuadrupleCLIPLoader/pt-BR.md)

O Quadruple CLIP Loader, QuadrupleCLIPLoader, é um dos nós principais do ComfyUI, adicionado inicialmente para dar suporte ao modelo HiDream I1. Se você não encontrar este nó, tente atualizar o ComfyUI para a versão mais recente para garantir o suporte.

Ele requer 4 modelos CLIP, correspondentes aos parâmetros `clip_name1`, `clip_name2`, `clip_name3` e `clip_name4`, e fornecerá uma saída do modelo CLIP para os nós subsequentes.

Este nó detecta modelos localizados na pasta `ComfyUI/models/text_encoders` e também lê modelos de caminhos adicionais configurados no arquivo extra_model_paths.yaml. Às vezes, após adicionar modelos, pode ser necessário **recarregar a interface do ComfyUI** para permitir que ela leia os arquivos de modelo na pasta correspondente.
