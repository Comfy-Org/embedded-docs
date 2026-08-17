# Tracer le graphique de perte

Le nœud LossGraphNode crée un graphique visuel des valeurs de perte d'entraînement au fil du temps et l'affiche comme image d'aperçu. Il prend les données de perte des processus d'entraînement et génère un graphique en courbes montrant comment la perte évolue au fil des étapes d'entraînement. Le graphique obtenu comprend des étiquettes d'axes et les valeurs de perte min/max.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `loss` | Map de perte provenant du nœud d'entraînement. Doit contenir une clé `loss` avec une liste de valeurs de perte utilisées pour tracer le graphique. | LOSS_MAP | Oui | - |
| `filename_prefix` | Préfixe pour l'image du graphique de perte enregistrée. (par défaut : "loss_graph") | STRING | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `ui.images` | L'image du graphique de perte générée affichée en aperçu. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LossGraphNode/fr.md)

---
**Source fingerprint (SHA-256):** `b1f0b72a03d4ce2d9461fc6e312bd1e847455f7dd5227667876a945494ea8cdb`
