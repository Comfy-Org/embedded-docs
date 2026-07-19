# Luma Image vers Image

Voici la traduction de la documentation du nœud ComfyUI `LumaImageModifyNode` :

Modifie les images de manière synchrone en fonction d’un prompt textuel et du rapport hauteur/largeur de l’image d’origine. Ce nœud prend une image en entrée et la transforme selon le prompt fourni, en utilisant un poids d’image configurable pour contrôler le degré de modification de l’image d’origine.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L’image d’entrée à modifier | IMAGE | Oui | - |
| `prompt` | Prompt pour la génération de l’image (par défaut : "") | STRING | Oui | - |
| `poids de l'image` | Poids de l’image ; plus la valeur est proche de 1.0, moins l’image sera modifiée (par défaut : 0.1). En interne, cette valeur est inversée (1.0 - image_weight) et limitée entre 0.0 et 0.98. | FLOAT | Non | 0.0-0.98 |
| `modèle` | Le modèle Luma à utiliser pour la modification de l’image. Différents modèles ont des coûts différents. | STRING | Oui | `"photon-flash-1"`<br>`"photon-1"`<br>`"photon"` |
| `graine` | Graine permettant de déterminer si le nœud doit être réexécuté ; les résultats réels sont non déterministes quelle que soit la graine (par défaut : 0) | INT | Non | 0-18446744073709551615 |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `image` | L’image modifiée générée par le modèle Luma | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageModifyNode/fr.md)

---
**Source fingerprint (SHA-256):** `078542bdba19945037c95fefa30d1b403ebf58e29270c8067dcb8ff21a99b7e0`
