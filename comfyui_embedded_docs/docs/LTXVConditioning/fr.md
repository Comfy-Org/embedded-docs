> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConditioning/fr.md)

Le nœud LTXVConditioning ajoute des informations de fréquence d'images aux entrées de conditionnement positif et négatif pour les modèles de génération vidéo. Il prend des données de conditionnement existantes et applique la valeur de fréquence d'images spécifiée aux deux ensembles de conditionnement, les rendant ainsi adaptés au traitement par des modèles vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Oui | - | L'entrée de conditionnement positif qui recevra les informations de fréquence d'images |
| `negative` | CONDITIONING | Oui | - | L'entrée de conditionnement négatif qui recevra les informations de fréquence d'images |
| `frame_rate` | FLOAT | Non | 0.0 - 1000.0 | La valeur de fréquence d'images à appliquer aux deux ensembles de conditionnement (par défaut : 25.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `negative` | CONDITIONING | Le conditionnement positif avec les informations de fréquence d'images appliquées |
| `negative` | CONDITIONING | Le conditionnement négatif avec les informations de fréquence d'images appliquées |