Le nœud CLIPLoader est conçu pour charger les modèles CLIP, supportant différents types tels que stable diffusion et stable cascade. Il simplifie les complexités du chargement et de la configuration des modèles CLIP pour une utilisation dans diverses applications, offrant un moyen simplifié d'accéder à ces modèles avec des configurations spécifiques.

## Entrées

| Paramètre     | Data Type | Description |
|---------------|--------------|-------------|
| `clip_name`   | `COMBO[STRING]` | Spécifie le nom du modèle CLIP à charger. Ce nom est utilisé pour localiser le fichier du modèle dans une structure de répertoire prédéfinie. |
| `type`        | `COMBO[STRING]` | Détermine le type de modèle CLIP à charger, offrant des options entre 'stable_diffusion' et 'stable_cascade'. Cela affecte la manière dont le modèle est initialisé et configuré. |

## Sorties

| Paramètre | Data Type | Description |
|-----------|-------------|-------------|
| `clip`    | `CLIP`      | Le modèle CLIP chargé, prêt à être utilisé dans des tâches en aval ou pour un traitement ultérieur. |
