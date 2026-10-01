# Ideogram 4.5 Precise Edit

Edite uma imagem com a orientação de um prompt de texto usando a edição precisa do Ideogram 4.5: apenas o que o prompt pede é alterado, os pixels não tocados permanecem idênticos, e a saída mantém o tamanho da imagem 1. A imagem 1 é a imagem a ser editada e até 4 imagens adicionais podem ser conectadas como referências.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `modelo` | Modelo a usar. (padrão: `"ideogram-4.5"`) | DYNAMIC_COMBO | Sim | `"ideogram-4.5"` |
| `images` | Slot expansível: a imagem 1 é a imagem a ser editada e as imagens 2 a 5 são referências opcionais (`image_1` ... `image_5`). Faça referência a elas no prompt como @Image1, @Image2, ...; uma entrada em lote conta uma vez por imagem. Cada imagem deve ter uma proporção de aspecto entre 1:6 e 6:1. | IMAGE | Sim | 1 a 5 imagens |
| `prompt` | Instruções de edição. Suporta referências no estilo @Image1 para as imagens conectadas. (padrão: string vazia) | STRING | Sim | 1 a 10000 caracteres |
| `quality` | Nível de qualidade. Níveis mais altos custam mais e demoram mais. (padrão: `"medium"`) | COMBO | Sim | `"very_low"`<br>`"low"`<br>`"medium"`<br>`"high"` |
| `seed` | Semente para geração. As mesmas imagens, prompt, configurações e semente produzem o mesmo resultado. (padrão: 42) | INT | Sim | 0 a 2147483647 |

### Restrições de parâmetros

- **Número de imagens:** pelo menos 1 e no máximo 5 imagens; uma entrada em lote conta uma vez por imagem. A imagem 1 é a imagem a ser editada e as imagens 2 a 5 são referências.
- **Tamanho da saída:** o resultado mantém o tamanho da imagem 1, portanto este nó não tem entradas de tamanho, largura ou altura.
- **Proporção de aspecto da imagem:** cada imagem não pode ser mais larga que 6x sua altura nem mais alta que 6x sua largura (entre 1:6 e 6:1).
- **Tags do prompt:** `@ImageN` é correspondido sem diferenciar maiúsculas de minúsculas e não deve exceder o número de imagens conectadas; o prompt não pode conter apenas espaços em branco e deve ter no máximo 10000 caracteres.
- **Escalonamento no upload:** imagens maiores que cerca de 4 MP, ou maiores que 4608 px no lado maior, são reduzidas antes de serem enviadas.
- **Segurança de conteúdo:** se o filtro de segurança de conteúdo do Ideogram bloquear o resultado, o nó gera um erro em vez de retornar uma imagem.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `IMAGE` | A imagem editada como um lote, no tamanho da imagem 1. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPreciseEditApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `74ba429ac93e4528e44c864ccfd3928f6c42108cfcc83577c8963a099a66f527`
