Ce nœud est conçu pour générer un échantillonneur pour le modèle DPMPP_2M_SDE, permettant la création d'échantillons basés sur des types de solveurs, des niveaux de bruit et des préférences de périphérique de calcul spécifiés. Il abstrait les complexités de la configuration de l'échantillonneur, offrant une interface simplifiée pour générer des échantillons avec des paramètres personnalisés.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `solver_type` | Spécifie le type de solveur à utiliser dans le processus d'échantillonnage, offrant des options entre 'midpoint' et 'heun'. Ce choix influence la méthode d'intégration numérique appliquée lors de l'échantillonnage. | COMBO[STRING] |
| `eta` | Détermine la taille du pas dans l'intégration numérique, affectant la granularité du processus d'échantillonnage. Une valeur plus élevée indique une taille de pas plus grande. | `FLOAT` |
| `s_noise` | Contrôle le niveau de bruit introduit pendant le processus d'échantillonnage, influençant la variabilité des échantillons générés. | `FLOAT` |
| `noise_device` | Indique le périphérique de calcul ('gpu' ou 'cpu') sur lequel le processus de génération de bruit est exécuté, affectant les performances et l'efficacité. | COMBO[STRING] |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `sampler` | La sortie est un échantillonneur configuré selon les paramètres spécifiés, prêt à générer des échantillons. | `SAMPLER` |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDpmpp2mSde/fr.md)
