> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDpmppSde/fr.md)

Ce nœud est conçu pour générer un échantillonneur pour le modèle DPM++ SDE (Équation Différentielle Stochastique). Il s'adapte aux environnements d'exécution CPU et GPU, optimisant l'implémentation de l'échantillonneur en fonction du matériel disponible.

## Entrées

| Paramètre       | Type de données | Description |
|----------------|-----------------|-------------|
| `eta`          | FLOAT           | Spécifie la taille du pas pour le solveur SDE, influençant la granularité du processus d'échantillonnage.|
| `s_noise`      | FLOAT           | Détermine le niveau de bruit à appliquer lors du processus d'échantillonnage, affectant la diversité des échantillons générés.|
| `r`            | FLOAT           | Contrôle le rapport de réduction du bruit dans le processus d'échantillonnage, impactant la clarté et la qualité des échantillons générés.|
| `noise_device` | COMBO[STRING]   | Sélectionne l'environnement d'exécution (CPU ou GPU) pour l'échantillonneur, optimisant les performances en fonction du matériel disponible.|

## Sorties

| Paramètre    | Type de données | Description |
|----------------|-----------------|-------------|
| `sampler`    | SAMPLER         | L'échantillonneur généré, configuré avec les paramètres spécifiés, prêt à être utilisé dans les opérations d'échantillonnage.|