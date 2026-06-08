Voici la traduction de la documentation du nœud SamplerCustom, conformément à vos règles :

Le nœud SamplerCustom est conçu pour offrir un mécanisme d'échantillonnage flexible et personnalisable pour diverses applications. Il permet aux utilisateurs de sélectionner et de configurer différentes stratégies d'échantillonnage adaptées à leurs besoins spécifiques, améliorant ainsi l'adaptabilité et l'efficacité du processus d'échantillonnage.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `modèle` | Le type d'entrée 'model' spécifie le modèle à utiliser pour l'échantillonnage, jouant un rôle crucial dans la détermination du comportement et du résultat de l'échantillonnage. | `MODEL` |
| `ajouter_bruit` | Le type d'entrée 'add_noise' permet aux utilisateurs de spécifier si du bruit doit être ajouté au processus d'échantillonnage, influençant la diversité et les caractéristiques des échantillons générés. | `BOOLEAN` |
| `graine_de_bruit` | Le type d'entrée 'noise_seed' fournit une graine pour la génération de bruit, garantissant la reproductibilité et la cohérence du processus d'échantillonnage lors de l'ajout de bruit. | `INT` |
| `cfg` | Le type d'entrée 'cfg' définit la configuration du processus d'échantillonnage, permettant un réglage fin des paramètres et du comportement de l'échantillonnage. | `FLOAT` |
| `positive` | Le type d'entrée 'positive' représente les informations de conditionnement positif, guidant le processus d'échantillonnage vers la génération d'échantillons correspondant aux attributs positifs spécifiés. | `CONDITIONING` |
| `négative` | Le type d'entrée 'negative' représente les informations de conditionnement négatif, éloignant le processus d'échantillonnage de la génération d'échantillons présentant les attributs négatifs spécifiés. | `CONDITIONING` |
| `échantillonneur` | Le type d'entrée 'sampler' sélectionne la stratégie d'échantillonnage spécifique à employer, impactant directement la nature et la qualité des échantillons générés. | `SAMPLER` |
| `sigmas` | Le type d'entrée 'sigmas' définit les niveaux de bruit à utiliser dans le processus d'échantillonnage, affectant l'exploration de l'espace d'échantillonnage et la diversité de la sortie. | `SIGMAS` |
| `image_latente` | Le type d'entrée 'latent_image' fournit une image latente initiale pour le processus d'échantillonnage, servant de point de départ pour la génération d'échantillons. | `LATENT` |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `sortie_débruitée` | La sortie 'output' représente le résultat principal du processus d'échantillonnage, contenant les échantillons générés. | `LATENT` |
| `denoised_output` | La sortie 'denoised_output' représente les échantillons après l'application d'un processus de débruitage, améliorant potentiellement la clarté et la qualité des échantillons générés. | `LATENT` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustom/fr.md)
