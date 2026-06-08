Le nœud KSamplerAdvanced est conçu pour améliorer le processus d'échantillonnage en proposant des configurations et techniques avancées. Il vise à offrir des options plus sophistiquées pour générer des échantillons à partir d'un modèle, en améliorant les fonctionnalités de base du KSampler.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `model` | Spécifie le modèle à partir duquel les échantillons doivent être générés, jouant un rôle crucial dans le processus d'échantillonnage. | MODEL |
| `add_noise` | Détermine si du bruit doit être ajouté au processus d'échantillonnage, affectant la diversité et la qualité des échantillons générés. | COMBO[STRING] |
| `noise_seed` | Définit la graine pour la génération de bruit, garantissant la reproductibilité du processus d'échantillonnage. | INT |
| `steps` | Définit le nombre d'étapes à suivre dans le processus d'échantillonnage, influençant le niveau de détail et la qualité du résultat. | INT |
| `cfg` | Contrôle le facteur de conditionnement, influençant la direction et l'espace du processus d'échantillonnage. | FLOAT |
| `sampler_name` | Sélectionne l'échantillonneur spécifique à utiliser, permettant de personnaliser la technique d'échantillonnage. | COMBO[STRING] |
| `scheduler` | Choisit le planificateur pour contrôler le processus d'échantillonnage, affectant la progression et la qualité des échantillons. | COMBO[STRING] |
| `positive` | Spécifie le conditionnement positif pour guider l'échantillonnage vers les attributs souhaités. | CONDITIONING |
| `negative` | Spécifie le conditionnement négatif pour éloigner l'échantillonnage de certains attributs. | CONDITIONING |
| `latent_image` | Fournit l'image latente initiale à utiliser dans le processus d'échantillonnage, servant de point de départ. | LATENT |
| `start_at_step` | Détermine l'étape de départ du processus d'échantillonnage, permettant de contrôler la progression de l'échantillonnage. | INT |
| `end_at_step` | Définit l'étape de fin du processus d'échantillonnage, délimitant la portée de l'échantillonnage. | INT |
| `return_with_leftover_noise` | Indique s'il faut renvoyer l'échantillon avec du bruit résiduel, affectant l'apparence du résultat final. | COMBO[STRING] |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `latent` | La sortie représente l'image latente générée à partir du modèle, reflétant les configurations et techniques appliquées. | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSamplerAdvanced/fr.md)
