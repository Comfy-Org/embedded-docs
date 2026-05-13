> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringTrim/fr.md)

Le nœud StringTrim supprime les caractères d'espacement (espaces, tabulations, sauts de ligne) du début, de la fin ou des deux côtés d'une chaîne de texte. Vous pouvez choisir de couper à gauche, à droite ou des deux côtés de la chaîne. Cela est utile pour nettoyer les entrées de texte en supprimant les espaces, tabulations ou retours à la ligne indésirables.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `string` | STRING | Oui | - | La chaîne de texte à traiter. Prend en charge les entrées multilignes. |
| `mode` | COMBO | Oui | "Both"<br>"Left"<br>"Right" | Spécifie le(s) côté(s) de la chaîne à couper. "Both" supprime les espaces des deux extrémités, "Left" supprime uniquement du début, "Right" supprime uniquement de la fin. |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `output` | STRING | La chaîne de texte coupée, dont les espaces ont été supprimés selon le mode sélectionné. |

---
**Source fingerprint (SHA-256):** `29b4da100373585af8a672ccfbd4c0b597705c1d8c176b2f88f3e878c1192460`
