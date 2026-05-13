> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuadrupleCLIPLoader/pt-BR.md)

O Carregador Quádruplo de CLIP, *QuadrupleCLIPLoader*, é um dos nós centrais do ComfyUI, adicionado inicialmente para suportar o modelo da versão HiDream I1. Se você perceber que este nó está faltando, tente atualizar o ComfyUI para a versão mais recente para garantir o suporte ao nó.

Ele requer 4 modelos CLIP, correspondentes aos parâmetros `clip_name1`, `clip_name2`, `clip_name3` e `clip_name4`, e fornecerá uma saída de modelo CLIP para os nós subsequentes.

Este nó detectará os modelos localizados na pasta `ComfyUI/models/text_encoders`,
 e também lerá modelos de caminhos adicionais configurados no arquivo *extra_model_paths.yaml*.
 Às vezes, após adicionar modelos, pode ser necessário **recarregar a interface do ComfyUI** para permitir que ele leia os arquivos de modelo na pasta correspondente.