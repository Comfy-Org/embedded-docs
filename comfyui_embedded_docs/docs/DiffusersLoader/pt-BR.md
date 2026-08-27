# Carregador Diffusers

O nó DiffusersLoader carrega modelos pré-treinados salvos no formato diffusers. Ele pesquisa as pastas `diffusers` configuradas em busca de diretórios que contenham um arquivo `model_index.json`, permite que você selecione um e o carrega como os componentes MODEL, CLIP e VAE usados no pipeline. Este nó está obsoleto, mas permanece disponível para compatibilidade com modelos diffusers do Hugging Face.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `caminho_do_modelo` | O caminho para o diretório do modelo diffusers a ser carregado. O nó verifica automaticamente as pastas diffusers configuradas em busca de modelos válidos e lista as opções disponíveis. | COMBO | Sim | Múltiplas opções disponíveis<br>(preenchidas automaticamente a partir das pastas diffusers) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-----------|-------------|-----------|
| `MODEL` | O componente de modelo carregado do formato diffusers. | MODEL |
| `CLIP` | O componente de modelo CLIP carregado do formato diffusers. | CLIP |
| `VAE` | O componente de VAE (Autoencoder Variacional) carregado do formato diffusers. | VAE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffusersLoader/pt-BR.md)

---
**Source fingerprint (SHA-256):** `75238342d05eac7528f981a2d4544accb6053891cd078a77751cc838054225d4`
