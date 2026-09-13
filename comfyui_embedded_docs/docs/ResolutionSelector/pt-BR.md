# Seletor de Resolução

O nó Resolution Selector calcula a largura e a altura em pixels com base em uma proporção de aspecto escolhida e uma resolução total desejada em megapixels. Ele é útil para gerar dimensões consistentes para outros nós, como o nó Empty Latent Image.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `aspect_ratio` | A proporção de aspecto para as dimensões de saída (padrão: `"1:1 (Square)"`). | COMBO | Sim | `"1:1 (Square)"`<br>`"2:3 (Portrait Photo)"`<br>`"3:2 (Photo)"`<br>`"3:4 (Portrait Standard)"`<br>`"4:3 (Standard)"`<br>`"9:16 (Portrait Widescreen)"`<br>`"16:9 (Widescreen)"`<br>`"21:9 (Ultrawide)"` |
| `megapixels` | Total desejado de megapixels. 1.0 MP ≈ 1024x1024 para formato quadrado (padrão: 1.0). | FLOAT | Sim | 0.1 - 16.0 (step: 0.1) |
| `preview` | Pré-visualização ao vivo da resolução de saída calculada. Este widget somente leitura é atualizado automaticamente e não aceita entrada do usuário. | RESOLUTION_PREVIEW | Não | N/A |
| `multiple` | Múltiplo mais próximo do resultado para definir a resolução selecionada (padrão: 8). | INT | Não | 8 - 128 (step: 4) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `width` | Largura calculada em pixels multiplicada pelo múltiplo selecionado. | INT |
| `height` | Altura calculada em pixels multiplicada pelo múltiplo selecionado. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionSelector/pt-BR.md)

---
**Source fingerprint (SHA-256):** `dd4c7f977ed69a873a48da4b01c5c8f0b6563cfd743740235fc0ad5762579697`
