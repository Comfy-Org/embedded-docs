Le nœud BasicScheduler est conçu pour calculer une séquence de valeurs sigma pour les modèles de diffusion en fonction du planificateur, du modèle et des paramètres de débruitage fournis. Il ajuste dynamiquement le nombre total d'étapes en fonction du facteur de débruitage pour affiner le processus de diffusion.

## Types d'entrée

| Paramètre | Comfy dtype | Description |
|-----------|-------------|-------------|
| `model`   | `MODEL`     | Le paramètre model spécifie le modèle de diffusion pour lequel les valeurs sigma doivent être calculées. Il joue un rôle crucial dans la détermination des valeurs sigma appropriées pour le processus de diffusion. |
| `scheduler` | `COMBO[STRING]` | Le paramètre scheduler détermine l'algorithme de planification à utiliser pour calculer les valeurs sigma. Il influence directement la progression et les caractéristiques du processus de diffusion. |
| `steps`    | `INT`       | Le paramètre steps indique le nombre total d'étapes dans le processus de diffusion. Il affecte la granularité et la durée du processus. |
| `denoise`  | `FLOAT`     | Le paramètre denoise permet d'ajuster le nombre effectif d'étapes en échelonnant le total des étapes, permettant un contrôle plus fin du processus de diffusion. |

## Types de sortie

| Paramètre | Comfy dtype | Description |
|-----------|-------------|-------------|
| `sigmas`  | `SIGMAS`    | La sortie sigmas représente la séquence calculée de valeurs sigma pour le processus de diffusion, essentielle pour contrôler le niveau de bruit à chaque étape. |