# Agendador Ideogram 4

O nó Agendador Ideogram 4 gera uma sequência de valores sigma (níveis de ruído) para o processo de amostragem por difusão, baseada no cronograma de referência do Ideogram 4. Ele cria um cronograma de ruído personalizado que se adapta às dimensões da imagem e permite ajustes finos por meio de parâmetros estatísticos.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-----------|--------------|-------------|-------|
| `passos` | O número de etapas de amostragem para gerar o cronograma (padrão: 20) | INT | Sim | 1 a 200 |
| `largura` | A largura da imagem em pixels (padrão: 1024) | INT | Sim | 256 a 8192 (passo: 16) |
| `altura` | A altura da imagem em pixels (padrão: 1024) | INT | Sim | 256 a 8192 (passo: 16) |
| `mu` | O parâmetro de média para a distribuição logit-normal, controlando o nível central de ruído (padrão: 0,0) | FLOAT | Sim | -10,0 a 10,0 (passo: 0,05) |
| `std` | O parâmetro de desvio padrão para a distribuição logit-normal, controlando a dispersão dos níveis de ruído (padrão: 1,75) | FLOAT | Sim | 0,1 a 5,0 (passo: 0,05) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `SIGMAS` | Um tensor de valores sigma representando o cronograma de ruído, com comprimento igual a `steps + 1`. Os valores diminuem de ruído alto para ruído baixo, com o valor final definido como 0,0 para remoção completa de ruído. | SIGMAS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Ideogram4Scheduler/pt-BR.md)

---
**Source fingerprint (SHA-256):** `408ea680158500690e28e300098a5c4fd13eb1a2c96c3d95db06244151116f22`
