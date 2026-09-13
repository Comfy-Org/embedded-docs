# BriaEraseForeground

Este nó remove o primeiro plano de uma imagem com a Bria e gera um novo plano de fundo em seu lugar. Tudo o que a Bria identifica como primeiro plano é removido, não apenas pessoas, e os pixels não modificados são preservados. O resultado é renderizado novamente em um tamanho padrão próximo de 1 megapixel.

Este é um nó de API pago que é executado no serviço da Bria, portanto suas credenciais da API do Comfy são usadas a cada execução.

## Entradas

### Entradas comuns

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `image` | A imagem cujo primeiro plano é removido e substituído por um plano de fundo gerado. Apenas os canais de cor são enviados; qualquer canal alfa é descartado antes do envio. | IMAGE | Sim | - |
| `moderation` | Configurações de moderação. Selecione `"false"` para enviar a imagem sem sinalizadores de moderação, ou `"true"` para revelar os controles de moderação de conteúdo abaixo. Padrão: `"false"`. | DYNAMIC_COMBO | Sim | `"false"`<br>`"true"` |

### Entradas para `"false"`

Nenhuma entrada adicional. A solicitação é enviada sem sinalizadores de moderação de conteúdo.

### Entradas para `"true"`

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `visual_input_moderation` | Ativa a moderação de conteúdo na imagem de entrada. Padrão: false. | BOOLEAN | Sim | true<br>false |
| `visual_output_moderation` | Ativa a moderação de conteúdo na imagem de saída gerada. Padrão: false. | BOOLEAN | Sim | true<br>false |

### Observações

- A saída é renderizada novamente em um tamanho padrão próximo de 1 megapixel, portanto a imagem retornada pode diferir em dimensões da imagem de entrada.
- Este nó é um nó de API pago; cada execução custa aproximadamente US$ 0,0572.

## Saídas

| Nome da saída | Descrição | Tipo de dados |
|-------------|-------------|-----------|
| `IMAGE` | A imagem de entrada com seu primeiro plano apagado e um plano de fundo recém-gerado em seu lugar. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaEraseForeground/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4d8c3c5eed97c648b1191ec41931c97caa17e98a8edd1c054ed63e80cc671b05`
