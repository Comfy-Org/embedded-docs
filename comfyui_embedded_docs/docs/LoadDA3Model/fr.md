# Charger Depth Anything 3

Ce nœud charge un modèle Depth Anything 3 à partir d'un fichier, en le préparant pour une utilisation dans des tâches d'estimation de profondeur. Il vous permet de sélectionner le fichier du modèle et, éventuellement, de spécifier la précision numérique (type de données) pour les poids du modèle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_name` | Le nom du fichier du modèle Depth Anything 3 à charger. | STRING | Oui | Liste des fichiers de modèle disponibles dans le dossier `geometry_estimation` |
| `weight_dtype` | La précision numérique (type de données) pour les poids du modèle. L'option "default" utilise la précision d'origine du modèle. (par défaut : "default") | STRING | Non | `"default"`<br>`"fp16"`<br>`"bf16"`<br>`"fp32"` |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `DA3_MODEL` | Le modèle Depth Anything 3 chargé, prêt à être utilisé dans des workflows d'estimation de profondeur. | DA3_MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadDA3Model/fr.md)

---
**Source fingerprint (SHA-256):** `b1b3f4075cd9172bc1f274848b9300bca20d3cbd53b23d3c4a9f0986b36e409e`
