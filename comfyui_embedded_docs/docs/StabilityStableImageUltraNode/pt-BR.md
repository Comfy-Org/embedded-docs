> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityStableImageUltraNode/pt-BR.md)

Gera imagens de forma síncrona com base em um prompt e resolução. Este nó cria imagens usando o modelo Stable Image Ultra da Stability AI, processando seu prompt de texto e gerando uma imagem correspondente com a proporção de aspecto e estilo especificados.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sim | - | O que você deseja ver na imagem de saída. Um prompt forte e descritivo que defina claramente elementos, cores e assuntos levará a melhores resultados. Para controlar o peso de uma determinada palavra, use o formato `(palavra:peso)`, onde `palavra` é a palavra cujo peso você deseja controlar e `peso` é um valor entre 0 e 1. Por exemplo: `O céu era um (azul:0.3) intenso e (verde:0.8)` descreveria um céu azul e verde, mas mais verde do que azul. |
| `aspect_ratio` | COMBO | Sim | Múltiplas opções disponíveis | Proporção de aspecto da imagem gerada. |
| `style_preset` | COMBO | Não | Múltiplas opções disponíveis | Estilo desejado opcional para a imagem gerada. |
| `seed` | INT | Sim | 0-4294967294 | A semente aleatória usada para criar o ruído. |
| `image` | IMAGE | Não | - | Imagem de entrada opcional. |
| `negative_prompt` | STRING | Não | - | Um trecho de texto descrevendo o que você *não* deseja ver na imagem de saída. Este é um recurso avançado. |
| `image_denoise` | FLOAT | Não | 0.0-1.0 | Desfoque da imagem de entrada; 0.0 resulta em uma imagem idêntica à entrada, 1.0 é como se nenhuma imagem tivesse sido fornecida. Padrão: 0.5 |

**Observação:** Quando uma imagem de entrada não é fornecida, o parâmetro `image_denoise` é automaticamente desativado.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | IMAGE | A imagem gerada com base nos parâmetros de entrada. |
