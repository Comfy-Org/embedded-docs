# Agendador Ideogram 4

O nó Ideogram 4 Scheduler gera uma sequência de valores sigma (níveis de ruído) para o processo de amostragem de difusão, com base no cronograma de referência do Ideogram 4. Ele cria um cronograma de ruído personalizado que se adapta às dimensões da imagem e permite ajuste fino por meio de parâmetros estatísticos.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|----------------|--------------|-----------|
| `passos` | O número de etapas de amostragem para gerar o cronograma (padrão: 20). A saída contém `steps + 1` valores sigma. | INT | Sim | 1 a 200 |
| `largura` | A largura da imagem em pixels (padrão: 1024). A resolução em relação a uma referência de 512×512 desloca o cronograma de ruído. | INT | Sim | 256 a 8192 (passo: 16) |
| `altura` | A altura da imagem em pixels (padrão: 1024). A resolução em relação a uma referência de 512×512 desloca o cronograma de ruído. | INT | Sim | 256 a 8192 (passo: 16) |
| `mu` | O parâmetro de média para a distribuição logit-normal, controlando o nível central de ruído. Combinado com o termo de resolução para formar o deslocamento de logSNR (padrão: 0.0). | FLOAT | Sim | -10.0 a 10.0 (passo: 0.05) |
| `std` | O parâmetro de desvio padrão para a distribuição logit-normal, controlando a dispersão dos níveis de ruído (padrão: 1.75). | FLOAT | Sim | 0.1 a 5.0 (passo: 0.05) |

Nota: O cronograma é derivado de uma distribuição logit-normal sobre o tempo de referência. Um termo de resolução igual a `0.5 * log((width × height) / (512 × 512))` é adicionado a `mu`, portanto imagens maiores ou menores deslocam o cronograma em relação a uma referência de 512×512 para o mesmo valor de `mu`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-----------|-------------|--------------|
| `SIGMAS` | Um tensor de valores sigma representando o cronograma de ruído, com comprimento igual a `steps + 1`. Os valores descem de ruído alto para ruído baixo, com o valor final definido como 0.0 para remoção completa de ruído. | SIGMAS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Ideogram4Scheduler/pt-BR.md)

---
**Source fingerprint (SHA-256):** `af0749713ce223d2246fc24b5100f18aa68d56746480990282899c223578b8f4`
