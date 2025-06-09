Ce nœud détecte les modèles situés dans le dossier `ComfyUI/models/gligen` et lit également les modèles des chemins supplémentaires que vous avez configurés dans le fichier extra_model_paths.yaml. Parfois, vous devrez **rafraîchir l'interface ComfyUI** pour qu'elle puisse lire les fichiers de modèle dans le dossier correspondant.

Le nœud `GLIGENLoader` est conçu pour charger des modèles GLIGEN, qui sont des modèles génératifs spécialisés. Il facilite le processus de récupération et d'initialisation de ces modèles à partir de chemins spécifiés, les rendant prêts pour des tâches génératives ultérieures.

## Entrées

| Champ       | Comfy dtype       | Description                                                                       |
|-------------|-------------------|-----------------------------------------------------------------------------------|
| `gligen_name`| `COMBO[STRING]`    | Le nom du modèle GLIGEN à charger, spécifiant quel fichier de modèle récupérer et charger, crucial pour l'initialisation du modèle GLIGEN. |

## Sorties

| Champ    | Data Type | Description                                                              |
|----------|-------------|--------------------------------------------------------------------------|
| `gligen` | `GLIGEN`    | Le modèle GLIGEN chargé, prêt à être utilisé dans des tâches génératives, représentant le modèle entièrement initialisé chargé à partir du chemin spécifié. |
