> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLatent/pt-BR.md)

O nó LoadLatent carrega representações latentes previamente salvas de arquivos .latent no diretório de entrada. Ele lê os dados do tensor latente do arquivo e aplica quaisquer ajustes de escala necessários antes de retornar os dados latentes para uso em outros nós.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `latent` | STRING | Sim | Todos os arquivos .latent no diretório de entrada | Seleciona qual arquivo .latent carregar dentre os arquivos disponíveis no diretório de entrada |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `LATENT` | LATENT | Retorna os dados da representação latente carregados do arquivo selecionado |

---
**Source fingerprint (SHA-256):** `020185a6066263b75b2417411f07af54d31a2a3a056d650eacfff188dc2cb87e`
