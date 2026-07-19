# Beeble SwitchX Édition d’Image

Modifiez une seule image avec Beeble SwitchX. Ce nœud peut changer n'importe quel élément de la scène (arrière-plan, éclairage, costume) tout en préservant les pixels du sujet d'origine. Fournissez une image de référence et/ou une invite textuelle pour décrire le nouvel aspect. La résolution maximale est d'environ 2,77 mégapixels.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image source à modifier. | IMAGE | Oui | - |
| `invite` | Une description textuelle du nouvel aspect souhaité (par exemple, "un chevalier en armure étincelante"). | STRING | Oui | - |
| `mode alpha` | Comment gérer le mat alpha. "select" utilise une image clé pour sélectionner le sujet, "fill" remplace l'image entière sans mat séparé, "custom" utilise un masque fourni par l'utilisateur. | COMBO | Oui | `"select"`<br>`"fill"`<br>`"custom"` |
| `résolution maximale` | La résolution maximale de l'image de sortie. Une résolution plus élevée coûte plus de crédits. | COMBO | Oui | `"1080p"`<br>`"720p"` |
| `graine` | Une valeur de graine pour la reproductibilité. | INT | Oui | - |
| `image de référence` | Une image de référence optionnelle pour guider le style ou l'apparence des nouveaux éléments de la scène. | IMAGE | Non | - |

**Remarque sur `alpha_mode` :** Lorsque `alpha_mode` est défini sur `"select"`, vous devez également fournir une `alpha_keyframe` (une image clé utilisée pour sélectionner le sujet). Lorsqu'il est défini sur `"custom"`, vous devez fournir un `alpha_mask` (un masque créé par l'utilisateur). Lorsqu'il est défini sur `"fill"`, aucune entrée alpha n'est nécessaire.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L'image modifiée avec les éléments de la scène changés. | IMAGE |
| `alpha` | Le mat alpha utilisé par Beeble. Vide pour le mode "fill", qui n'a pas de mat séparé. | MASK |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BeebleSwitchXImageEdit/fr.md)

---
**Source fingerprint (SHA-256):** `41f23435686626e3ade28708fcb1da192ded347b210080ee9b17834ea8b727fb`
