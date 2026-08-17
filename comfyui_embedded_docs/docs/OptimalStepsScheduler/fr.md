# OptimalStepsScheduler

Le nœud OptimalStepsScheduler calcule les sigmas du calendrier de bruit pour les modèles de diffusion en fonction du type de modèle sélectionné et de la configuration des étapes. Il ajuste le nombre total d'étapes selon le paramètre `denoise` et interpole les niveaux de bruit pour correspondre au nombre d'étapes demandé. Le nœud renvoie une séquence de valeurs sigma qui déterminent les niveaux de bruit utilisés pendant le processus d'échantillonnage par diffusion.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model_type` | Le type de modèle de diffusion à utiliser pour le calcul des niveaux de bruit | COMBO | Oui | "FLUX"<br>"Wan"<br>"Chroma" |
| `steps` | Le nombre total d'étapes d'échantillonnage à calculer (par défaut : 20) | INT | Oui | 3-1000 |
| `denoise` | Contrôle la force de débruitage, qui ajuste le nombre effectif d'étapes (par défaut : 1,0) | FLOAT | Oui | 0,0-1,0 |

**Remarque :** Lorsque `denoise` est défini sur une valeur inférieure à 1,0, le nœud calcule les étapes effectives comme `steps * denoise`. Si `denoise` est défini sur 0,0, le nœud renvoie un tenseur vide.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `sigmas` | Une séquence de valeurs sigma représentant le calendrier de bruit pour l'échantillonnage par diffusion | SIGMAS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OptimalStepsScheduler/fr.md)

---
**Source fingerprint (SHA-256):** `fd48c94ca16c8a3d8e6f0138018e7b13c15d100d6147807bcb23d838899045b7`
