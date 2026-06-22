# Tracer le graphique de perte

Voici la traduction de la documentation du nœud LossGraphNode :

Le LossGraphNode crée un graphique visuel des valeurs de perte d'entraînement au fil du temps et l'affiche sous forme d'image de prévisualisation. Il prend les données de perte issues des processus d'entraînement et génère un graphique en courbes montrant l'évolution de la perte à travers les étapes d'entraînement. Le graphique obtenu inclut des étiquettes d'axes et les valeurs de perte minimale et maximale.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `perte` | Carte de perte provenant du nœud d'entraînement. | LOSS_MAP | Oui | - |
| `préfixe_nom_fichier` | Préfixe pour l'image du graphique de perte sauvegardée. (par défaut : "loss_graph") | STRING | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `ui.images` | L'image du graphique de perte généré affichée sous forme de prévisualisation. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LossGraphNode/fr.md)

---
**Source fingerprint (SHA-256):** `9b1c844cb4babafc61102ee7bfd1039c325c6665abff1721d92a6da7d18029f9`
