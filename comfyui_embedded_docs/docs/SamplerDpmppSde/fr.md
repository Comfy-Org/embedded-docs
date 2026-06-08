Ce nœud est conçu pour générer un échantillonneur pour le modèle DPM++ SDE (Équation Différentielle Stochastique). Il s'adapte aux environnements d'exécution CPU et GPU, optimisant l'implémentation de l'échantillonneur en fonction du matériel disponible.

## Entrées

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `eta` | Spécifie la taille du pas pour le solveur SDE, influençant la granularité du processus d'échantillonnage. | FLOAT |
| `s_noise` | Détermine le niveau de bruit à appliquer lors du processus d'échantillonnage, affectant la diversité des échantillons générés. | FLOAT |
| `r` | Contrôle le rapport de réduction du bruit dans le processus d'échantillonnage, impactant la clarté et la qualité des échantillons générés. | FLOAT |
| `noise_device` | Sélectionne l'environnement d'exécution (CPU ou GPU) pour l'échantillonneur, optimisant les performances en fonction du matériel disponible. | COMBO[STRING] |

## Sorties

| Paramètre | Description | Type de données |
| --- | --- | --- |
| `sampler` | L'échantillonneur généré, configuré avec les paramètres spécifiés, prêt à être utilisé dans les opérations d'échantillonnage. | SAMPLER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDpmppSde/fr.md)
