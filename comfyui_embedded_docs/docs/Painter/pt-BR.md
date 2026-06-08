O nó Painter fornece uma tela interativa para criar ou editar imagens e máscaras diretamente no ComfyUI. Ele permite que você comece com uma tela em branco ou uma imagem existente, pinte sobre ela usando uma ferramenta de pincel e gere tanto a imagem resultante quanto uma máscara alfa correspondente. A máscara define as áreas pintadas, que são então compostas sobre a imagem base ou a cor de fundo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `imagem` | Imagem base opcional para pintar por cima. Se não for fornecida, uma tela em branco é criada usando a cor de fundo, largura e altura especificadas. | IMAGE | Não | - |
| `mask` | Os dados da pintura, normalmente gerados pelo widget interativo integrado do nó. Este parâmetro é gerenciado pela ferramenta de pintura da interface e não deve ser conectado a um soquete padrão. | STRING | Sim | - |
| `largura` | A largura da tela em pixels, usada quando nenhuma `imagem` base é fornecida. O valor deve ser um múltiplo de 64. O padrão é 512. | INT | Sim | 64 a 4096 |
| `altura` | A altura da tela em pixels, usada quando nenhuma `imagem` base é fornecida. O valor deve ser um múltiplo de 64. O padrão é 512. | INT | Sim | 64 a 4096 |
| `cor_de_fundo` | A cor de fundo da tela, especificada como um código hexadecimal (ex.: #000000). Isso é usado apenas quando nenhuma `imagem` base é fornecida. O padrão é preto (#000000). | COLOR | Sim | - |

**Observação:** A entrada `mask` foi projetada para funcionar com o widget de interface especializado do nó. Quando você pinta na tela, o widget preenche automaticamente esse valor. As entradas `width` e `height` ficam ocultas na interface padrão, mas definem as dimensões da tela ao criar uma nova imagem.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `IMAGE` | A imagem final composta. Este é o resultado da mesclagem das áreas pintadas (da `mask`) sobre a `imagem` base fornecida ou o fundo colorido. | IMAGE |
| `MASK` | A máscara de canal alfa (transparência) extraída da pintura. As áreas brancas representam as regiões pintadas, e as áreas pretas representam o fundo não modificado. | MASK |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Painter/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ae926b6d30aab65737bd99a58cb7de5a71fa36e61a677dbc97fc30b8ef8d2418`
