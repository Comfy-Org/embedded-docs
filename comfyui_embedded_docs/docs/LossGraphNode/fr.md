# Tracer le graphique de perte

Le nœud LossGraphNode crée un graphique en courbes des valeurs de perte d’entraînement en fonction des étapes d’entraînement et l’affiche sous forme d’image d’aperçu. Il lit les valeurs de perte depuis un nœud d’entraînement, les trace sur un graphique avec des axes étiquetés et les valeurs de perte min/max, puis renvoie le graphique comme aperçu d’image dans l’interface.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `perte` | Map de perte provenant du nœud d’entraînement. Elle doit contenir une clé `loss` avec une liste de valeurs de perte numériques. | LOSS_MAP | Oui | - |
| `préfixe_nom_fichier` | Préfixe pour l’image du graphique de perte enregistrée. (défaut : "loss_graph") | STRING | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `ui.images` | L’image du graphique de perte générée, affichée en tant qu’aperçu. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LossGraphNode/fr.md)

---
**Source fingerprint (SHA-256):** `b1f0b72a03d4ce2d9461fc6e312bd1e847455f7dd5227667876a945494ea8cdb`
