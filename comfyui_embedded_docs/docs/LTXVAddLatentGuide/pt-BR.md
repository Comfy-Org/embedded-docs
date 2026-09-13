# LTXV Adicionar Guia Latent

O nó LTXV Add Latent Guide fixa um latent já codificado como um guia, para quando o guia vem de um estágio anterior em vez de uma imagem. Tem o mesmo efeito que o LTXV Add Guide sem a ida e volta de decode/encode do VAE. Um guia que é espacialmente menor que o destino (uma referência IC-LoRA ou de detalhamento) é dilatado em uma grade esparsa, e suas posições finais de RoPE são expandidas pela mesma proporção para que cubra o canvas de destino em vez de endereçar apenas o canto superior esquerdo dele.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `positive` | Entrada de condicionamento positivo. | CONDITIONING | Sim | N/A |
| `negative` | Entrada de condicionamento negativo. | CONDITIONING | Sim | N/A |
| `vae` | O modelo VAE usado para ler a fórmula do índice de redução de escala para posicionamento de frames. | VAE | Sim | N/A |
| `latent` | Latent de vídeo de destino no qual o guia é fixado. | LATENT | Sim | N/A |
| `guiding_latent` | Latent do guia. Seu tamanho espacial deve dividir o do destino pelo mesmo número inteiro em ambos os eixos; tamanho igual o fixa como está, metade do tamanho é tratada como uma referência IC-LoRA x2. | LATENT | Sim | N/A |
| `latent_idx` | Índice do frame latente em que o guia começa, contado em frames latentes em vez de frames de pixel. Valores negativos posicionam o guia em frames antes do início do latent, não contados de trás para frente a partir do seu fim. Padrão: 0. | INT | Sim | -9999 a 9999 |
| `strength` | Limitado a 1.0. Um guia dilatado marca suas posições de padding com uma máscara de denoise negativa para que o modelo as descarte; acima de 1.0, as posições mantidas também ficariam negativas e todo o guia seria descartado. Em vez disso, amplifique além de 1.0 com attention_mask. Padrão: 1.0. | FLOAT | Sim | 0.0 a 1.0, passo 0.01 |
| `attention_mask` | Máscara espacial opcional no espaço de pixels. Controla a influência do condicionamento por região via auto-atenção, multiplicada por strength. | MASK | Não | N/A |

### Observações

- Tanto `latent` quanto `guiding_latent` devem ser latents de vídeo 5D com formato (batch, channels, frames, height, width).
- O guia deve caber dentro do latent de destino: o número de frames do guia somado a `latent_idx` não pode ultrapassar o fim do latent de destino. Valores negativos de `latent_idx` são permitidos e posicionam o guia antes do início do latent.
- O tamanho espacial do guia deve dividir o tamanho espacial do destino por um número inteiro tanto no eixo de altura quanto no de largura.
- A proporção de altura e a proporção de largura devem ter o mesmo valor (proporção quadrada). Uma proporção não quadrada gera um erro, porque a dilatação e o posicionamento RoPE usam um único fator de redução de escala para ambos os eixos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `positive` | Condicionamento positivo com o guia anexado. | CONDITIONING |
| `negative` | Condicionamento negativo com o guia anexado. | CONDITIONING |
| `latent` | Saída de latent com o guia aplicado, incluindo o `noise_mask` atualizado. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAddLatentGuide/pt-BR.md)

---
**Source fingerprint (SHA-256):** `19542500484dbc57fdbeeab8ba05bc2978246b3be5decc413825f616cab46f73`
