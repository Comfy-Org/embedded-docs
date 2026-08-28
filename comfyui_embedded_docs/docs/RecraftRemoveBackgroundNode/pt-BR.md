# Recraft Remover Fundo

Este nó remove o fundo de imagens usando o serviço da API Recraft. Ele processa cada imagem do lote de entrada e retorna tanto as imagens processadas com fundos transparentes quanto as máscaras alfa correspondentes, que indicam as áreas de fundo removidas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `imagem` | A(s) imagem(ns) de entrada para processamento de remoção de fundo. Cada imagem do lote é processada individualmente. | IMAGE | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | Imagens processadas com fundos transparentes (formato RGBA) | IMAGE |
| `mask` | Máscaras de canal alfa indicando as áreas de fundo removidas, no formato B,H,W | MASK |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftRemoveBackgroundNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `702dfdf2751d5ca33f23e10c0968496887514a21da7a0c42e3636a0ed4e82311`
