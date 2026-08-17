# Carregador Diffusers

O nó DiffusersLoader está obsoleto. Ele carrega modelos pré-treinados salvos no formato diffusers do Hugging Face e retorna os três componentes padrão necessários para o pipeline: MODEL, CLIP e VAE. O nó varre automaticamente as pastas de diffusers configuradas em busca de diretórios de modelo válidos (pastas que contenham um arquivo `model_index.json`) e permite que você escolha qual carregar.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model_path` | O caminho para o diretório do modelo diffusers a ser carregado. O nó verifica as pastas de diffusers configuradas e lista todos os diretórios que contenham um arquivo `model_index.json`. | COMBO | Sim | Preenchido automaticamente a partir das pastas de diffusers configuradas (todo subdiretório que contenha um arquivo `model_index.json`) |

Nota: o caminho selecionado é validado em relação à lista de modelos descobertos. O carregamento falha com um erro se o caminho não estiver mais na lista ou se o diretório do modelo não puder ser encontrado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `MODEL` | O componente de modelo carregado a partir do formato diffusers | MODEL |
| `CLIP` | O componente de modelo de codificação de texto CLIP carregado a partir do formato diffusers | CLIP |
| `VAE` | O componente VAE (Autoencoder Variacional) carregado a partir do formato diffusers | VAE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffusersLoader/pt-BR.md)

---
**Source fingerprint (SHA-256):** `75238342d05eac7528f981a2d4544accb6053891cd078a77751cc838054225d4`
