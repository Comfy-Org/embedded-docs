# LTXVConditioning

Le nœud LTXVConditioning ajoute des informations de fréquence d'images aux entrées de conditionnement positives et négatives pour les modèles de génération vidéo. Il prend les données de conditionnement existantes et applique la valeur de fréquence d'images spécifiée aux deux ensembles de conditionnement, les rendant adaptés au traitement par les modèles vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | L'entrée de conditionnement positive qui recevra les informations de fréquence d'images | CONDITIONING | Oui | - |
| `negative` | L'entrée de conditionnement négative qui recevra les informations de fréquence d'images | CONDITIONING | Oui | - |
| `frame_rate` | La valeur de fréquence d'images à appliquer aux deux ensembles de conditionnement (défaut : 25.0) | FLOAT | Oui | 0.0 - 1000.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Le conditionnement positif avec les informations de fréquence d'images appliquées | CONDITIONING |
| `negative` | Le conditionnement négatif avec les informations de fréquence d'images appliquées | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConditioning/fr.md)

---
**Source fingerprint (SHA-256):** `c8546b691329f2934995f97a6db2e1393d2928bf1a7438fd079d52f87bee1c35`
