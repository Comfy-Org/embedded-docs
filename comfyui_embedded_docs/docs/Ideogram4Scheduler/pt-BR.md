# Agendador Ideogram 4

O nó **Ideogram 4 Scheduler** gera uma sequência de valores sigma (níveis de ruído) para o processo de amostragem de difusão, com base no cronograma de referência do Ideogram 4. Ele cria um cronograma de ruído personalizado que se adapta às dimensões da imagem e permite ajuste fino por meio de parâmetros estatísticos.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `steps` | O número de etapas de amostragem para gerar o cronograma (padrão: 20) | INT | Sim | 1 a 200 |
| `width` | A largura da imagem em pixels (padrão: 1024) | INT | Sim | 256 a 8192 (passo: 16) |
| `height` | A altura da imagem em pixels (padrão: 1024) | INT | Sim | 256 a 8192 (passo: 16) |
| `mu` | O parâmetro de média para a distribuição logito-normal, controlando o nível de ruído central (padrão: 0.0) | FLOAT | Sim | -10.0 a 10.0 (passo: 0.05) |
| `std` | O parâmetro de desvio padrão para a distribuição logito-normal, controlando a dispersão dos níveis de ruído (padrão: 1.75) | FLOAT | Sim | 0.1 a 5.0 (passo: 0.05) |

Nota: O deslocamento central efetivo do cronograma é determinado por `mu` combinado com um termo de resolução baseado na área da imagem em relação a uma referência de 512×512. Áreas de imagem maiores, portanto, deslocam o cronograma de ruído em comparação com as menores.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `SIGMAS` | Um tensor de valores sigma representando o cronograma de ruído, com comprimento igual a `steps + 1`. Os valores decrescem de ruído alto para ruído baixo, com o valor final definido como 0.0 para remoção completa de ruído. | SIGMAS |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Ideogram4Scheduler/pt-BR.md)

---
**Source fingerprint (SHA-256):** `af0749713ce223d2246fc24b5100f18aa68d56746480990282899c223578b8f4`
