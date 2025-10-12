> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OptimalStepsScheduler/fr.md)

Le nœud OptimalStepsScheduler calcule les sigmas du plan de bruit pour les modèles de diffusion en fonction du type de modèle sélectionné et de la configuration des étapes. Il ajuste le nombre total d'étapes en fonction du paramètre de débruitage et interpole les niveaux de bruit pour correspondre au nombre d'étapes demandé. Le nœud retourne une séquence de valeurs sigma qui déterminent les niveaux de bruit utilisés pendant le processus d'échantillonnage par diffusion.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model_type` | COMBO | Oui | "FLUX"<br>"Wan"<br>"Chroma" | Le type de modèle de diffusion à utiliser pour le calcul des niveaux de bruit |
| `steps` | INT | Oui | 3-1000 | Le nombre total d'étapes d'échantillonnage à calculer (par défaut : 20) |
| `denoise` | FLOAT | Non | 0.0-1.0 | Contrôle la force du débruitage, ce qui ajuste le nombre effectif d'étapes (par défaut : 1.0) |

**Note :** Lorsque `denoise` est défini sur une valeur inférieure à 1.0, le nœud calcule les étapes effectives comme `steps * denoise`. Si `denoise` est défini sur 0.0, le nœud retourne un tenseur vide.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | Une séquence de valeurs sigma représentant le plan de bruit pour l'échantillonnage par diffusion |