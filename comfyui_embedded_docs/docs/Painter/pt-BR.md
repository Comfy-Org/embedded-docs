> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Painter/pt-BR.md)

O nó Painter fornece uma tela interativa para criar ou editar imagens e máscaras diretamente no ComfyUI. Ele permite que você comece com uma tela em branco ou uma imagem existente, pinte sobre ela usando uma ferramenta de pincel e gere tanto a imagem resultante quanto uma máscara alfa correspondente. A máscara define as áreas pintadas, que são então compostas sobre a imagem base ou a cor de fundo.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|---------------|-------------|-----------|-----------|
| `image` | IMAGE | Não | - | Imagem base opcional para pintar por cima. Se não for fornecida, uma tela em branco é criada usando a cor de fundo, largura e altura especificadas. |
| `mask` | STRING | Sim | - | Os dados de pintura, normalmente gerados pelo widget interativo integrado do nó. Este parâmetro é gerenciado pela ferramenta de pintura da interface e não deve ser conectado a um soquete padrão. |
| `width` | INT | Sim | 64 a 4096 | A largura da tela em pixels, usada quando nenhuma `image` base é fornecida. O valor deve ser múltiplo de 64. O padrão é 512. |
| `height` | INT | Sim | 64 a 4096 | A altura da tela em pixels, usada quando nenhuma `image` base é fornecida. O valor deve ser múltiplo de 64. O padrão é 512. |
| `bg_color` | COLOR | Sim | - | A cor de fundo da tela, especificada como um código hexadecimal (ex.: #000000). Isso é usado apenas quando nenhuma `image` base é fornecida. O padrão é preto (#000000). |

**Observação:** A entrada `mask` foi projetada para funcionar com o widget de interface especializado do nó. Quando você pinta na tela, o widget preenche automaticamente esse valor. As entradas `width` e `height` ficam ocultas na interface padrão, mas definem as dimensões da tela ao criar uma nova imagem.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `IMAGE` | IMAGE | A imagem final composta. Este é o resultado da mesclagem das áreas pintadas (da `mask`) sobre a `image` base fornecida ou o fundo colorido. |
| `MASK` | MASK | A máscara de canal alfa (transparência) extraída da pintura. As áreas brancas representam as regiões pintadas, e as áreas pretas representam o fundo não modificado. |