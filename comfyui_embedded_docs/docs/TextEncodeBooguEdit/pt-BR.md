# TextEncodeBooguEdit

Este nó prepara o condicionamento para edição de imagens com Boogu. Ele processa imagens de referência para criar saídas de condicionamento positivo e negativo. A imagem de referência é usada duas vezes: os tokens de visão da imagem são adicionados apenas ao condicionamento positivo para amplificar a instrução de edição, enquanto um latente de referência do VAE é adicionado tanto ao condicionamento positivo quanto ao negativo para que se cancelem sob CFG, preservando a identidade da imagem original; o tokenizador seleciona automaticamente o prompt de sistema apropriado com base na presença de imagens e prompts negativos vazios.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-------------|--------------|-------------|-------|
| `clip` | O modelo CLIP usado para codificação de texto | CLIP | Sim | |
| `prompt` | O prompt de texto descrevendo a edição desejada. Suporta texto multilinha e prompts dinâmicos. | STRING | Sim | |
| `negative_prompt` | O prompt de texto descrevendo o que evitar na edição. Pode ser deixado vazio para descartar o condicionamento negativo. Parâmetro avançado. | STRING | Sim | |
| `vae` | O modelo VAE usado para codificar imagens de referência no espaço latente. Necessário para adicionar latentes de referência às saídas de condicionamento. | VAE | Não | |
| `imagens` | Imagem(ns) de referência para editar. Boogu foca em uma referência por amostra; mais são permitidas. | IMAGE | Não | Até 16 imagens |
Os latentes de referência são adicionados a ambas as saídas de condicionamento apenas quando `vae` é fornecido junto com pelo menos uma `image` de referência. Se `vae` for omitido, a saída positiva ainda recebe os tokens de visão das imagens de referência, mas nenhuma saída inclui latentes de referência.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `positive` | Condicionamento contendo tanto o prompt de texto com tokens visuais quanto os latents de referência | CONDITIONING |
| `negative` | Condicionamento contendo o prompt de texto negativo e os latents de referência | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeBooguEdit/pt-BR.md)

---
**Source fingerprint (SHA-256):** `170979acf5b2e9f25f96231a4b23a4376cfddcd4bda2fdd6e03528417e6931b0`
