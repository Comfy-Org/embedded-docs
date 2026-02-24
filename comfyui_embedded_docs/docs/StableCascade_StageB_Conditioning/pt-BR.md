> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageB_Conditioning/pt-BR.md)

O nó StableCascade_StageB_Conditioning prepara os dados de condicionamento para a geração do Estágio B do Stable Cascade, combinando as informações de condicionamento existentes com as representações latentes anteriores do Estágio C. Ele modifica os dados de condicionamento para incluir as amostras latentes do Estágio C, permitindo que o processo de geração aproveite as informações anteriores para produzir resultados mais coerentes.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `conditioning` | CONDITIONING | Sim | - | Os dados de condicionamento a serem modificados com as informações anteriores do Estágio C |
| `stage_c` | LATENT | Sim | - | A representação latente do Estágio C contendo as amostras anteriores para o condicionamento |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | Os dados de condicionamento modificados com as informações anteriores do Estágio C integradas |
