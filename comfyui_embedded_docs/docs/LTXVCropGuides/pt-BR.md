> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVCropGuides/pt-BR.md)

O nó LTXVCropGuides processa condicionamentos e entradas latentes para geração de vídeo, removendo informações de quadros-chave e ajustando as dimensões latentes. Ele recorta a imagem latente e a máscara de ruído para excluir seções de quadros-chave, enquanto limpa os índices de quadros-chave dos condicionamentos positivo e negativo. Isso prepara os dados para fluxos de trabalho de geração de vídeo que não requerem orientação por quadros-chave.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sim | - | O condicionamento positivo contendo informações de orientação para a geração |
| `negative` | CONDITIONING | Sim | - | O condicionamento negativo contendo informações de orientação sobre o que evitar na geração |
| `latent` | LATENT | Sim | - | A representação latente contendo amostras de imagem e dados da máscara de ruído |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | O condicionamento positivo processado, com índices de quadros-chave limpos |
| `negative` | CONDITIONING | O condicionamento negativo processado, com índices de quadros-chave limpos |
| `latent` | LATENT | A representação latente recortada, com amostras e máscara de ruído ajustadas |
