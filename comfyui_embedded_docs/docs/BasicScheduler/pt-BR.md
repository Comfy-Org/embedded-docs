O nó `BasicScheduler` é projetado para calcular uma sequência de valores de sigma para modelos de difusão com base no agendador, modelo e parâmetros de remoção de ruído fornecidos. Ele ajusta dinamicamente o número total de etapas com base no fator de remoção de ruído para refinar o processo de difusão, fornecendo "receitas" precisas para diferentes estágios em processos de amostragem avançados que exigem controle refinado (como amostragem em múltiplos estágios).

## Entradas

| Parâmetro | Descrição Metafórica | Tipo de Dado | Tipo de Entrada | Padrão | Intervalo | Propósito Técnico |
| --- | --- | --- | --- | --- | --- | --- |
| `modelo` | **Tipo de Tela**: Diferentes materiais de tela precisam de diferentes fórmulas de tinta | MODEL | Entrada | - | - | Objeto do modelo de difusão, determina a base do cálculo de sigma |
| `agendador` | **Técnica de Mistura**: Escolha como a concentração de tinta muda | COMBO[STRING] | Widget | - | 9 opções | Algoritmo de agendamento, controla o modo de decaimento do ruído |
| `etapas` | **Quantidade de Misturas**: Diferença de precisão entre 20 e 50 misturas | INT | Widget | 20 | 1-10000 | Etapas de amostragem, afeta a qualidade e velocidade de geração |
| `reduzir_ruído` | **Intensidade de Criação**: Controle o nível do ajuste fino à repintura | FLOAT | Widget | 1.0 | 0.0-1.0 | Força de remoção de ruído, suporta cenários de repintura parcial |

### Tipos de Agendador

Com base no código-fonte `comfy.samplers.SCHEDULER_NAMES`, suporta os seguintes 9 agendadores:

| Nome do Agendador   | Características      | Casos de Uso                    | Padrão de Decaimento de Ruído          |
| ------------------- | -------------------- | ------------------------------- | -------------------------------------- |
| **normal**          | Linear padrão        | Cenários gerais, equilibrado    | Decaimento uniforme                    |
| **karras**          | Transição suave      | Alta qualidade, rico em detalhes| Decaimento não linear suave            |
| **exponential**     | Decaimento exponencial| Geração rápida, eficiência      | Decaimento exponencial rápido          |
| **sgm_uniform**     | SGM uniforme         | Otimização de modelo específico | Decaimento otimizado SGM               |
| **simple**          | Agendamento simples  | Testes rápidos, uso básico      | Decaimento simplificado                |
| **ddim_uniform**    | DDIM uniforme        | Otimização de amostragem DDIM   | Decaimento específico DDIM             |
| **beta**            | Distribuição beta    | Necessidades de distribuição especial | Decaimento da função beta         |
| **linear_quadratic**| Linear quadrático    | Otimização de cenários complexos| Decaimento da função quadrática        |
| **kl_optimal**      | KL ótimo             | Otimização teórica              | Decaimento otimizado por divergência KL|

## Saídas

| Parâmetro | Descrição Metafórica | Tipo de Dado | Tipo de Saída | Significado Técnico |
| --- | --- | --- | --- | --- |
| `sigmas` | **Gráfico de Receita de Tinta**: Lista detalhada de concentração de tinta para uso passo a passo | SIGMAS | Saída | Sequência de níveis de ruído, guia o processo de remoção de ruído do modelo de difusão |

## Função do Nó: Assistente de Mistura de Cores do Artista

Imagine que você é um artista criando uma imagem nítida a partir de uma mistura caótica de tinta (ruído). O `BasicScheduler` atua como seu **assistente profissional de mistura de cores**, cujo trabalho é preparar uma série de receitas precisas de concentração de tinta:

### Fluxo de Trabalho

- **Passo 1**: Use tinta com 90% de concentração (alto nível de ruído)
- **Passo 2**: Use tinta com 80% de concentração
- **Passo 3**: Use tinta com 70% de concentração
- **...**
- **Passo Final**: Use tinta com 0% de concentração (tela limpa, sem ruído)

### Habilidades Especiais do Assistente de Cores

**Diferentes métodos de mistura (agendador)**:

- **Método de mistura "karras"**: A concentração de tinta muda de forma muito suave, como a técnica de gradiente de um artista profissional
- **Método de mistura "exponential"**: A concentração de tinta diminui rapidamente, adequado para criação rápida
- **Método de mistura "linear"**: A concentração de tinta diminui uniformemente, estável e controlável

**Controle refinado (etapas)**:

- **20 misturas**: Pintura rápida, prioridade à eficiência
- **50 misturas**: Pintura refinada, prioridade à qualidade

**Intensidade de criação (remoção de ruído)**:

- **1.0 = Criação nova completa**: Comece completamente de uma tela em branco
- **0.5 = Meia transformação**: Mantenha metade da pintura original, transforme a outra metade
- **0.2 = Ajuste fino**: Faça apenas ajustes sutis na pintura original

### Colaboração com Outros Nós

`BasicScheduler` (Assistente de Cores) → Preparar Receita → `SamplerCustom` (Artista) → Pintura Real → Trabalho Concluído

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BasicScheduler/pt-BR.md)
