# Recraft Remover Fundo

Este nó remove o fundo de imagens usando o serviço da API Recraft. Ele processa cada imagem no lote de entrada e retorna tanto as imagens processadas com fundo transparente quanto as máscaras alfa correspondentes, que indicam as áreas de fundo removidas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `image` | A(s) imagem(ns) de entrada a serem processadas para remoção de fundo | IMAGE | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-------------|---------------|
| `image` | Imagens processadas com fundo transparente | IMAGE |
| `mask` | Máscaras alfa que indicam as áreas de fundo removidas | MASK |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftRemoveBackgroundNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `702dfdf2751d5ca33f23e10c0968496887514a21da7a0c42e3636a0ed4e82311`
