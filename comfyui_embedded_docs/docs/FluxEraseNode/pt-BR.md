# Flux Apagar Imagem

Remove o objeto mascarado de uma imagem e reconstrói o fundo. Pinte a máscara sobre o que deseja apagar, e o nó preenche a área com conteúdo de fundo plausível.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `imagem` | A imagem de entrada para processar | IMAGE | Sim | - |
| `máscara` | Áreas brancas são removidas; áreas pretas são preservadas | MASK | Sim | - |
| `dilatar_pixels` | Expande os limites da máscara para garantir uma cobertura limpa das bordas do objeto (padrão: 10) | INT | Sim | 0 a 25 |
| `semente` | A semente aleatória usada para criar o ruído (padrão: 0) | INT | Não | 0 a 2147483647 |

**Nota:** A imagem de entrada deve ter pelo menos 256x256 pixels em ambas as dimensões. A máscara é redimensionada automaticamente para corresponder às dimensões da imagem, e o canal alfa da imagem é removido antes do processamento.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `IMAGE` | A imagem resultante com o objeto mascarado removido e o fundo reconstruído | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxEraseNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `124be59b9829aa9f865d7ec76cd68f7978e2010cd3a84f25742a1c17f2d70b76`
