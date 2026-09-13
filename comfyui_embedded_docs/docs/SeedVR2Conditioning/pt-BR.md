# Aplicar Condicionamento SeedVR2

Constrói condicionamentos positivo e negativo a partir de um latente VAE para uso com o modelo SeedVR2. Valida o latente de entrada e a estrutura do modelo, adiciona um canal de máscara ao latente e retorna ambas as saídas de condicionamento.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo SeedVR2. | MODEL | Sim | - |
| `vae_conditioning` | O latente VAE do SeedVR2 a partir do qual construir o condicionamento (nome de exibição: latent). | LATENT | Sim | - |

Nota: O latente `vae_conditioning` deve ser um tensor 5-D no layout channel-first do Comfy (B, C, T, H, W), em que C é a contagem esperada de canais do VAE SeedVR2. O nó gera um erro se o latente não for 5-D, se a contagem de canais não corresponder ou se o tensor parecer estar no layout channel-last. A entrada `model` deve ter a estrutura esperada do SeedVR2; o nó resolve seu modelo de difusão interno e lê seus condicionamentos positivo e negativo. Internamente, o nó anexa um canal de máscara constante ao latente e associa o condicionamento resultante tanto às saídas de condicionamento `positive` quanto `negative`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `positive` | O condicionamento positivo para amostragem. | CONDITIONING |
| `negative` | O condicionamento negativo para amostragem. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2Conditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `28e508bdd776e2e3f5f2f93bfc29a1a1d1c34a11dbdc7f421d197ddbfa85f0f5`
