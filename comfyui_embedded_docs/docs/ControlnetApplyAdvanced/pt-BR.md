> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplyAdvanced/pt-BR.md)

Este nó aplica transformações avançadas de rede de controle aos dados de condicionamento com base em uma imagem e um modelo de rede de controle. Ele permite ajustes refinados da influência da rede de controle sobre o conteúdo gerado, possibilitando modificações mais precisas e variadas ao condicionamento.

## Entradas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `positive` | `CONDITIONING` | Os dados de condicionamento positivo aos quais as transformações da rede de controle serão aplicadas. Eles representam os atributos ou características desejadas a serem aprimoradas ou mantidas no conteúdo gerado. |
| `negative` | `CONDITIONING` | Os dados de condicionamento negativo, representando atributos ou características a serem diminuídos ou removidos do conteúdo gerado. As transformações da rede de controle também são aplicadas a esses dados, permitindo um ajuste equilibrado das características do conteúdo. |
| `control_net` | `CONTROL_NET` | O modelo de rede de controle é crucial para definir os ajustes e aprimoramentos específicos aos dados de condicionamento. Ele interpreta a imagem de referência e os parâmetros de força para aplicar transformações, influenciando significativamente o resultado final ao modificar atributos tanto nos dados de condicionamento positivo quanto negativo. |
| `image` | `IMAGE` | A imagem que serve como referência para as transformações da rede de controle. Ela influencia os ajustes feitos pela rede de controle aos dados de condicionamento, orientando o aprimoramento ou a supressão de características específicas. |
| `strength` | `FLOAT` | Um valor escalar que determina a intensidade da influência da rede de controle sobre os dados de condicionamento. Valores mais altos resultam em ajustes mais pronunciados. |
| `start_percent` | `FLOAT` | A porcentagem inicial do efeito da rede de controle, permitindo a aplicação gradual das transformações em um intervalo especificado. |
| `end_percent` | `FLOAT` | A porcentagem final do efeito da rede de controle, definindo o intervalo sobre o qual as transformações são aplicadas. Isso permite um controle mais sutil sobre o processo de ajuste. |

## Saídas

| Parâmetro | Tipo de Dados | Descrição |
|-----------|-------------|-------------|
| `positive` | `CONDITIONING` | Os dados de condicionamento positivo modificados após a aplicação das transformações da rede de controle, refletindo os aprimoramentos feitos com base nos parâmetros de entrada. |
| `negative` | `CONDITIONING` | Os dados de condicionamento negativo modificados após a aplicação das transformações da rede de controle, refletindo a supressão ou remoção de características específicas com base nos parâmetros de entrada. |
