Voici la traduction en français de la documentation du nœud PhotoMakerLoader :

Le nœud PhotoMakerLoader charge un modèle PhotoMaker à partir des fichiers de modèle disponibles. Il lit le fichier de modèle spécifié et prépare l'encodeur d'identité PhotoMaker pour une utilisation dans des tâches de génération d'images basées sur l'identité. Ce nœud est marqué comme expérimental et est destiné à des fins de test.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `nom_du_modèle_photomaker` | Le nom du fichier de modèle PhotoMaker à charger. Les options disponibles sont déterminées par les fichiers de modèle présents dans le dossier `photomaker`. | STRING | Oui | Plusieurs options disponibles |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `photomaker_model` | Le modèle PhotoMaker chargé contenant l'encodeur d'identité, prêt à être utilisé dans des opérations d'encodage d'identité. | PHOTOMAKER |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerLoader/fr.md)

---
**Source fingerprint (SHA-256):** `4c55abacf8462d8de3d1f2a728d4b09ab1d1c8c6476d25cc4af5089508a721da`
