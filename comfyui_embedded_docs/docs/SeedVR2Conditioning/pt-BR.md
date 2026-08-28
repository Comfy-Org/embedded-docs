# Aplicar Condicionamento SeedVR2

Este nó constrói condicionamentos positivo e negativo a partir de um latent do VAE para uso com o modelo SeedVR2. Ele valida a forma do latent de entrada e a estrutura do modelo e, em seguida, produz condicionamentos positivo e negativo que orientam a amostragem de imagem ou vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|--------------|-----------|
| `model` | O modelo SeedVR2. | MODEL | Sim | - |
| `vae_conditioning` | O latent do VAE SeedVR2 usado para criar o condicionamento (nome de exibição: latent). | LATENT | Sim | - |

Observação: o latent `vae_conditioning` deve ser um tensor 5-D no layout canal-primeiro do Comfy (B, C, T, H, W), em que C é o número esperado de canais do VAE SeedVR2. O nó gera um erro se o latent não for 5-D, se o número de canais não corresponder ou se parecer estar no layout canal-último. A entrada `model` deve ser um modelo com a estrutura SeedVR2 esperada. Internamente, o nó anexa um canal de máscara constante ao latent e anexa a condição resultante aos conjuntos de condicionamento positivo e negativo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|---------------|
| `positive` | O condicionamento positivo para a amostragem. | CONDITIONING |
| `negative` | O condicionamento negativo para a amostragem. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Conditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `28e508bdd776e2e3f5f2f93bfc29a1a1d1c34a11dbdc7f421d197ddbfa85f0f5`
