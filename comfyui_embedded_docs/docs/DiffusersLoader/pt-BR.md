# Carregador Diffusers

O nó DiffusersLoader carrega modelos pré-treinados no formato diffusers. Ele busca diretórios válidos de modelos diffusers que contenham um arquivo `model_index.json` e os carrega como componentes MODEL, CLIP e VAE para uso no pipeline. Este nó faz parte da categoria de carregadores obsoletos e fornece compatibilidade com modelos diffusers do Hugging Face.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `caminho_do_modelo` | O caminho para o diretório do modelo diffusers a ser carregado. O nó verifica automaticamente se há modelos diffusers válidos nas pastas diffusers configuradas e lista as opções disponíveis. | STRING | Sim | Múltiplas opções disponíveis<br>(preenchidas automaticamente a partir das pastas diffusers) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `MODEL` | O componente de modelo carregado do formato diffusers | MODEL |
| `CLIP` | O componente de modelo CLIP carregado do formato diffusers | CLIP |
| `VAE` | O componente VAE (Autoencoder Variacional) carregado do formato diffusers | VAE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffusersLoader/pt-BR.md)

---
**Source fingerprint (SHA-256):** `59be9923ed76d4859d5f7217a802c43297cb5af3d895eb6713edea97a32c3db2`
