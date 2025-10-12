> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerLoader/fr.md)

Le nœud PhotoMakerLoader charge un modèle PhotoMaker à partir des fichiers de modèles disponibles. Il lit le fichier de modèle spécifié et prépare l'encodeur d'identité PhotoMaker pour une utilisation dans les tâches de génération d'images basées sur l'identité. Ce nœud est marqué comme expérimental et est destiné à des fins de test.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `nom_du_modèle_photomaker` | STRING | Oui | Plusieurs options disponibles | Le nom du fichier de modèle PhotoMaker à charger. Les options disponibles sont déterminées par les fichiers de modèle présents dans le dossier photomaker. |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `photomaker_model` | PHOTOMAKER | Le modèle PhotoMaker chargé contenant l'encodeur d'identité, prêt à être utilisé dans les opérations d'encodage d'identité. |