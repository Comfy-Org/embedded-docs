> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DeprecatedCheckpointLoader/pt-BR.md)

O nó CheckpointLoader foi projetado para operações de carregamento avançadas, especificamente para carregar checkpoints de modelo juntamente com suas configurações. Ele facilita a recuperação dos componentes do modelo necessários para inicializar e executar modelos generativos, incluindo configurações e checkpoints de diretórios especificados.

## Entradas

| Parâmetro | Tipo de Dados | Descrição |
|--------------|--------------|-------------|
| `config_name` | COMBO[STRING] | Especifica o nome do arquivo de configuração a ser utilizado. Isso é crucial para determinar os parâmetros e configurações do modelo, afetando seu comportamento e desempenho. |
| `ckpt_name` | COMBO[STRING] | Indica o nome do arquivo de checkpoint a ser carregado. Isso influencia diretamente o estado do modelo que está sendo inicializado, impactando seus pesos e vieses iniciais. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `model` | MODEL | Representa o modelo principal carregado a partir do checkpoint, pronto para operações adicionais ou inferência. |
| `clip` | CLIP | Fornece o componente do modelo CLIP, se disponível e solicitado, carregado a partir do checkpoint. |
| `vae` | VAE | Entrega o componente do modelo VAE, se disponível e solicitado, carregado a partir do checkpoint. |