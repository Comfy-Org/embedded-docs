# Remover Fundo

O nó Remover Fundo utiliza um modelo de remoção de fundo para gerar uma máscara que separa o objeto principal do fundo de uma imagem de entrada. Ele recebe uma imagem e um modelo de remoção de fundo, produzindo uma máscara que destaca o objeto principal.

# Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `imagem` | Imagem de entrada da qual o fundo será removido | IMAGE | Sim | N/A |
| `modelo_remoção_fundo` | Modelo de remoção de fundo utilizado para gerar a máscara | BACKGROUND_REMOVAL_MODEL | Sim | N/A |

# Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `mask` | Máscara do objeto principal gerada, que destaca o sujeito principal da imagem de entrada | MASK |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemoveBackground/pt-BR.md)

---
**Source fingerprint (SHA-256):** `cd19134e6afed4d31096b613dd534eacad39afe7de2c8b74feab512bd5f09f66`
