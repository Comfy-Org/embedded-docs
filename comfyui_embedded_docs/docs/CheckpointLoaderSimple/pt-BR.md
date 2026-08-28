# Carregar Checkpoint

Carrega um arquivo de checkpoint de modelo de difusão e o decompõe em três componentes principais: o modelo principal usado para remover o ruído de latentes, o codificador de texto CLIP e o codificador/decodificador de imagem VAE. Este nó detecta automaticamente todos os arquivos de modelo na pasta `ComfyUI/models/checkpoints` e em quaisquer caminhos adicionais configurados no seu arquivo `extra_model_paths.yaml`.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `nome_ckpt` | O nome do checkpoint (modelo) a ser carregado. Selecione o nome do arquivo do modelo checkpoint, que determina o modelo de IA usado para a geração subsequente de imagens. | COMBO | Sim | Todos os arquivos de modelo na pasta de checkpoints |

**Nota:** Se novos arquivos de modelo forem adicionados enquanto o ComfyUI estiver em execução, você precisa atualizar o navegador (Ctrl+R) para ver os novos arquivos na lista suspensa.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `MODEL` | O modelo usado para remover o ruído de latentes. Este é o modelo de difusão principal usado para geração de imagens. | MODEL |
| `CLIP` | O modelo CLIP usado para codificar prompts de texto, convertendo descrições textuais em informações que a IA pode entender. | CLIP |
| `VAE` | O modelo VAE usado para codificar e decodificar imagens de e para o espaço latente. | VAE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoaderSimple/pt-BR.md)

---
**Source fingerprint (SHA-256):** `db99a8ba83a586491463df0d4e99ba5f77d4511c6d8337a721d76edd3450f310`
