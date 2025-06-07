
Ce nœud est conçu pour générer un échantillonneur pour le modèle DPMPP_2M_SDE, permettant la création d'échantillons basés sur des types de solveurs spécifiés, des niveaux de bruit et des préférences de dispositif de calcul. Il simplifie les complexités de la configuration de l'échantillonneur, offrant une interface simplifiée pour générer des échantillons avec des paramètres personnalisés.

## Entrées

| Paramètre       | Data Type | Description                                                                 |
|-----------------|-------------|-----------------------------------------------------------------------------|
| `solver_type`   | COMBO[STRING] | Spécifie le type de solveur à utiliser dans le processus d'échantillonnage, offrant des options entre 'midpoint' et 'heun'. Ce choix influence la méthode d'intégration numérique appliquée lors de l'échantillonnage. |
| `eta`           | `FLOAT`     | Détermine la taille des pas dans l'intégration numérique, affectant la granularité du processus d'échantillonnage. Une valeur plus élevée indique une taille de pas plus grande. |
| `s_noise`       | `FLOAT`     | Contrôle le niveau de bruit introduit pendant le processus d'échantillonnage, influençant la variabilité des échantillons générés. |
| `noise_device`  | COMBO[STRING] | Indique le dispositif de calcul ('gpu' ou 'cpu') sur lequel le processus de génération de bruit est exécuté, affectant la performance et l'efficacité. |

## Sorties

| Paramètre       | Data Type | Description                                                                 |
|-----------------|-------------|-----------------------------------------------------------------------------|
| `sampler`       | `SAMPLER`   | La sortie est un échantillonneur configuré selon les paramètres spécifiés, prêt à générer des échantillons. |
