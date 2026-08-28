# OptimalStepsScheduler

Le nœud OptimalStepsScheduler crée un plan de bruit (une séquence de valeurs sigma) à utiliser lors de l'échantillonnage de diffusion. Il choisit les niveaux de bruit de base selon le type de modèle sélectionné, ajuste le plan lorsque le débruitage est partiellement appliqué, et interpole les niveaux afin que les sigmas renvoyés correspondent au nombre d'étapes demandé.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model_type` | Le type de modèle de diffusion à utiliser pour le calcul du niveau de bruit. | COMBO | Oui | "FLUX"<br>"Wan"<br>"Chroma" |
| `étapes` | Le nombre total d'étapes d'échantillonnage à calculer (par défaut : 20). | INT | Oui | 3 à 1000 |
| `réduction du bruit` | Contrôle la force de débruitage, ce qui ajuste le nombre effectif d'étapes (par défaut : 1.0). | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |

**Remarque :** Lorsque `denoise` est inférieur à 1.0, le nœud utilise `round(steps * denoise)` comme nombre total d'étapes effectives. Si `denoise` vaut 0.0, le nœud renvoie un tenseur vide.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sigmas` | Une séquence de valeurs sigma représentant le plan de bruit pour l'échantillonnage de diffusion. | SIGMAS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OptimalStepsScheduler/fr.md)

---
**Source fingerprint (SHA-256):** `fd48c94ca16c8a3d8e6f0138018e7b13c15d100d6147807bcb23d838899045b7`
