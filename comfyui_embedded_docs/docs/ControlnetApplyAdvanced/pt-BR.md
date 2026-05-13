> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApplyAdvanced/pt-BR.md)

Este nó aplica transformações avançadas de rede de controle aos dados de condicionamento com base em uma imagem e um modelo de rede de controle. Ele permite ajustes refinados da influência da rede de controle sobre o conteúdo gerado, possibilitando modificações mais precisas e variadas no condicionamento.

## Entradas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|-------------|-------------|
| `positive` | `CONDITIONING` | Os dados de condicionamento positivo aos quais as transformações da rede de controle serão aplicadas. Representa os atributos ou características desejadas a serem realçadas ou mantidas no conteúdo gerado. |
| `negative` | `CONDITIONING` | Os dados de condicionamento negativo, representando atributos ou características a serem diminuídos ou removidos do conteúdo gerado. As transformações da rede de controle também são aplicadas a esses dados, permitindo um ajuste equilibrado das características do conteúdo. |
| `control_net` | `CONTROL_NET` | O modelo de rede de controle é essencial para definir os ajustes e aprimoramentos específicos nos dados de condicionamento. Ele interpreta a imagem de referência e os parâmetros de intensidade para aplicar transformações, influenciando significativamente o resultado final ao modificar atributos tanto nos dados de condicionamento positivo quanto negativo. |
| `image` | `IMAGE` | A imagem que serve como referência para as transformações da rede de controle. Ela influencia os ajustes feitos pela rede de controle nos dados de condicionamento, orientando o realce ou a supressão de características específicas. |
| `strength` | `FLOAT` | Um valor escalar que determina a intensidade da influência da rede de controle sobre os dados de condicionamento. Valores mais altos resultam em ajustes mais pronunciados. |
| `start_percent` | `FLOAT` | A porcentagem inicial do efeito da rede de controle, permitindo a aplicação gradual das transformações ao longo de um intervalo especificado. |
| `end_percent` | `FLOAT` | A porcentagem final do efeito da rede de controle, definindo o intervalo no qual as transformações são aplicadas. Isso possibilita um controle mais sutil sobre o processo de ajuste. |

## Saídas

| Parâmetro | Tipo de Dado | Descrição |
|-----------|-------------|-------------|
| `positive` | `CONDITIONING` | Os dados de condicionamento positivo modificados após a aplicação das transformações da rede de controle, refletindo os aprimoramentos feitos com base nos parâmetros de entrada. |
| `negative` | `CONDITIONING` | Os dados de condicionamento negativo modificados após a aplicação das transformações da rede de controle, refletindo a supressão ou remoção de características específicas com base nos parâmetros de entrada. |