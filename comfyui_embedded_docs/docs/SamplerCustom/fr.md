
Le nœud SamplerCustom est conçu pour fournir un mécanisme d'échantillonnage flexible et personnalisable pour diverses applications. Il permet aux utilisateurs de sélectionner et de configurer différentes stratégies d'échantillonnage adaptées à leurs besoins spécifiques, améliorant ainsi l'adaptabilité et l'efficacité du processus d'échantillonnage.

## Entrées

| Paramètre | Type de Donnée | Description |
|-----------|--------------|-------------|
| `model`   | `MODEL`      | Le type d'entrée 'model' spécifie le modèle à utiliser pour l'échantillonnage, jouant un rôle crucial dans la détermination du comportement et du résultat de l'échantillonnage. |
| `add_noise` | `BOOLEAN`    | Le type d'entrée 'add_noise' permet aux utilisateurs de spécifier si du bruit doit être ajouté au processus d'échantillonnage, influençant la diversité et les caractéristiques des échantillons générés. |
| `noise_seed` | `INT`        | Le type d'entrée 'noise_seed' fournit une graine pour la génération de bruit, assurant la reproductibilité et la cohérence du processus d'échantillonnage lors de l'ajout de bruit. |
| `cfg`     | `FLOAT`      | Le type d'entrée 'cfg' définit la configuration du processus d'échantillonnage, permettant un réglage fin des paramètres et du comportement de l'échantillonnage. |
| `positive` | `CONDITIONING` | Le type d'entrée 'positive' représente des informations de conditionnement positif, guidant le processus d'échantillonnage vers la génération d'échantillons qui s'alignent sur des attributs positifs spécifiés. |
| `negative` | `CONDITIONING` | Le type d'entrée 'negative' représente des informations de conditionnement négatif, orientant le processus d'échantillonnage pour éviter de générer des échantillons présentant des attributs négatifs spécifiés. |
| `sampler` | `SAMPLER`    | Le type d'entrée 'sampler' sélectionne la stratégie d'échantillonnage spécifique à employer, impactant directement la nature et la qualité des échantillons générés. |
| `sigmas`  | `SIGMAS`     | Le type d'entrée 'sigmas' définit les niveaux de bruit à utiliser dans le processus d'échantillonnage, affectant l'exploration de l'espace d'échantillons et la diversité du résultat. |
| `latent_image` | `LATENT` | Le type d'entrée 'latent_image' fournit une image latente initiale pour le processus d'échantillonnage, servant de point de départ pour la génération d'échantillons. |

## Sorties

| Paramètre | Type de Donnée | Description |
|-----------|--------------|-------------|
| `output`  | `LATENT`     | Le 'output' représente le résultat principal du processus d'échantillonnage, contenant les échantillons générés. |
| `denoised_output` | `LATENT` | Le 'denoised_output' représente les échantillons après qu'un processus de débruitage a été appliqué, améliorant potentiellement la clarté et la qualité des échantillons générés. |
