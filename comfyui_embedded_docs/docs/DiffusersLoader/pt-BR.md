> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffusersLoader/pt-BR.md)

O nó DiffusersLoader carrega modelos pré-treinados no formato diffusers. Ele busca diretórios válidos de modelos diffusers que contenham um arquivo `model_index.json` e os carrega como componentes MODEL, CLIP e VAE para uso no pipeline. Este nó faz parte da categoria de carregadores obsoletos e fornece compatibilidade com modelos diffusers do Hugging Face.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `model_path` | STRING | Sim | Múltiplas opções disponíveis<br>(preenchidas automaticamente a partir das pastas diffusers) | O caminho para o diretório do modelo diffusers a ser carregado. O nó verifica automaticamente se há modelos diffusers válidos nas pastas diffusers configuradas e lista as opções disponíveis. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `MODEL` | MODEL | O componente de modelo carregado do formato diffusers |
| `CLIP` | CLIP | O componente de modelo CLIP carregado do formato diffusers |
| `VAE` | VAE | O componente VAE (Autoencoder Variacional) carregado do formato diffusers |

---
**Source fingerprint (SHA-256):** `59be9923ed76d4859d5f7217a802c43297cb5af3d895eb6713edea97a32c3db2`
