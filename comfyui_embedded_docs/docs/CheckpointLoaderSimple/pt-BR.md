> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoaderSimple/pt-BR.md)

## Visão Geral

Carrega um arquivo de checkpoint de modelo de difusão e o decompõe em três componentes principais: o modelo principal usado para remoção de ruído de latentes, o codificador de texto CLIP e o codificador/decodificador de imagem VAE. Este nó detecta automaticamente todos os arquivos de modelo na pasta `ComfyUI/models/checkpoints` e quaisquer caminhos adicionais configurados no seu arquivo `extra_model_paths.yaml`.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `nome_ckpt` | STRING | Sim | Todos os arquivos de modelo na pasta checkpoints | O nome do checkpoint (modelo) a ser carregado. Selecione o nome do arquivo do checkpoint, que determina o modelo de IA usado para a geração de imagem subsequente. |

**Observação:** Se novos arquivos de modelo forem adicionados enquanto o ComfyUI estiver em execução, você precisará atualizar o navegador (Ctrl+R) para ver os novos arquivos na lista suspensa.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `MODEL` | MODEL | O modelo usado para remoção de ruído de latentes. Este é o modelo de difusão principal usado para geração de imagens. |
| `CLIP` | CLIP | O modelo CLIP usado para codificar prompts de texto, convertendo descrições textuais em informações que a IA pode entender. |
| `VAE` | VAE | O modelo VAE usado para codificar e decodificar imagens para e do espaço latente. |

---
**Source fingerprint (SHA-256):** `2fd8866ae659f8080f46c16d3a9864fa563d2090815d897ea2f42ba8d66d9b39`
