# Recraft Ampliação Nítida de Imagem

Este nó redimensiona uma imagem de forma síncrona usando a ferramenta "crisp upscale". Ele melhora uma imagem raster fornecida ao aumentar sua resolução, tornando a imagem mais nítida e limpa. Quando um lote de imagens é fornecido, cada imagem é processada independentemente e os resultados redimensionados são retornados como um lote.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | A imagem de entrada a ser redimensionada. Aceita um lote de imagens; cada imagem é processada independentemente. | IMAGE | Sim | — |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A imagem redimensionada com resolução e clareza aprimoradas. Retorna um lote de imagens se um lote foi fornecido como entrada. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftCrispUpscaleNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7a60c563504df7a81ce5d50e989bc4a8853f4bb30805a014c9fb567d8ec83e33`
