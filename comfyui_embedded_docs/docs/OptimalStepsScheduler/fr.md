# OptimalStepsScheduler

Le nœud OptimalStepsScheduler crée un programme de bruit (une séquence de valeurs sigma) à utiliser pendant l'échantillonnage de diffusion. Il choisit les niveaux de bruit de base à partir du type de modèle sélectionné, ajuste le programme lorsque le débruitage n'est appliqué que partiellement, et interpole les niveaux afin que les sigmas renvoyés correspondent au nombre d'étapes demandé.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model_type` | Type de modèle de diffusion à utiliser pour le calcul des niveaux de bruit. Chaque option utilise sa propre table prédéfinie de niveaux de bruit. | COMBO | Oui | "FLUX"<br>"Wan"<br>"Chroma" |
| `steps` | Nombre total d'étapes d'échantillonnage à calculer (par défaut : 20). | INT | Oui | 3 à 1000 |
| `denoise` | Contrôle la force du débruitage, ce qui ajuste le nombre effectif d'étapes (par défaut : 1.0). | FLOAT | Oui | 0.0 à 1.0 (pas : 0.01) |

**Remarque :** La table des niveaux de bruit de base pour le `model_type` sélectionné est rééchantillonnée avec une interpolation log-linéaire lorsque sa longueur n'est pas égale à `steps + 1`, de sorte que la sortie corresponde toujours au nombre d'étapes demandé.

**Remarque :** Lorsque `denoise` est inférieur à 1.0, le nœud utilise `round(steps * denoise)` comme nombre total d'étapes effectives et ne conserve que la queue correspondante du programme. Si `denoise` est égal à 0.0 ou inférieur, le nœud renvoie un tenseur vide.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sigmas` | Une séquence de valeurs sigma représentant le programme de bruit pour l'échantillonnage de diffusion. La valeur finale de la séquence est toujours définie à 0. | SIGMAS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OptimalStepsScheduler/fr.md)

---
**Source fingerprint (SHA-256):** `fd48c94ca16c8a3d8e6f0138018e7b13c15d100d6147807bcb23d838899045b7`
