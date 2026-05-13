> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemoveBackground/pt-BR.md)

# Visão Geral

O nó Remover Fundo utiliza um modelo de remoção de fundo para gerar uma máscara que separa o objeto principal do fundo de uma imagem de entrada. Ele recebe uma imagem e um modelo de remoção de fundo, produzindo uma máscara que destaca o objeto principal.

# Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `imagem` | IMAGE | Sim | N/A | Imagem de entrada da qual o fundo será removido |
| `modelo_remoção_fundo` | BACKGROUND_REMOVAL_MODEL | Sim | N/A | Modelo de remoção de fundo utilizado para gerar a máscara |

# Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `mask` | MASK | Máscara do objeto principal gerada, que destaca o sujeito principal da imagem de entrada |

---
**Source fingerprint (SHA-256):** `cd19134e6afed4d31096b613dd534eacad39afe7de2c8b74feab512bd5f09f66`
