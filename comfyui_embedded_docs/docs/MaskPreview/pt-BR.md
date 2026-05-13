> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskPreview/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskPreview/en.md)

O nó MaskPreview salva dados de máscara como uma imagem de pré-visualização no diretório de saída do ComfyUI, permitindo que você inspecione visualmente os dados da máscara durante a execução do fluxo de trabalho. Ele converte a máscara de entrada em um formato adequado para exibição de imagem e a salva com um prefixo de nome de arquivo configurável.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `mask` | MASK | Sim | - | Os dados da máscara a serem pré-visualizados e salvos como imagem |
| `filename_prefix` | STRING | Não | - | Prefixo para o nome do arquivo de saída (padrão: "ComfyUI") |
| `prompt` | PROMPT | Não | - | Informações do prompt para metadados (fornecido automaticamente) |
| `extra_pnginfo` | EXTRA_PNGINFO | Não | - | Informações PNG adicionais para metadados (fornecido automaticamente) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `ui` | DICT | Contém as informações da imagem de pré-visualização e metadados para exibição na interface do usuário |

---
**Source fingerprint (SHA-256):** `9f64adf4a0130368618fc1ca3655192686815ab10b4153f9552ef23149928e3f`
