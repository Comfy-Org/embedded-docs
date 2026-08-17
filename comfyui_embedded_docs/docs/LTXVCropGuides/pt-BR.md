# LTXVCropGuides

O nó LTXVCropGuides processa entradas de condicionamento e latentes para geração de vídeo, removendo informações de quadros-chave e ajustando as dimensões latentes. Ele recorta a imagem latente e a máscara de ruído para excluir seções de quadros-chave, enquanto limpa os índices de quadros-chave tanto nas entradas de condicionamento positivo quanto negativo. Isso prepara os dados para fluxos de trabalho de geração de vídeo que não exigem orientação por quadros-chave.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positive` | A entrada de condicionamento positivo contendo informações de orientação para a geração | CONDITIONING | Sim | - |
| `negative` | A entrada de condicionamento negativo contendo informações de orientação sobre o que evitar na geração | CONDITIONING | Sim | - |
| `latent` | A representação latente contendo amostras de imagem e dados de máscara de ruído | LATENT | Sim | - |

Nota: Se o condicionamento positivo não contiver índices de quadros-chave, o nó retorna as entradas positiva, negativa e latente inalteradas.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | O condicionamento positivo processado, com índices de quadros-chave e entradas de atenção de guia limpos | CONDITIONING |
| `negative` | O condicionamento negativo processado, com índices de quadros-chave e entradas de atenção de guia limpos | CONDITIONING |
| `latent` | A representação latente recortada, com amostras e máscara de ruído ajustadas, onde as seções de quadros-chave foram removidas | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVCropGuides/pt-BR.md)

---
**Source fingerprint (SHA-256):** `83e08bad281902e765ec18e06144b6a5fa730be2533932daa1d4076e6390b1e1`
