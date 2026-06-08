Voici la traduction en français de la documentation du nœud ComfyUI, conformément à vos règles :

---

Remplace l'arrière-plan d'une image en fonction d'une invite textuelle. Ce nœud utilise l'API Recraft pour générer de nouveaux arrière-plans pour vos images selon votre description textuelle, vous permettant de transformer complètement l'arrière-plan tout en conservant le sujet principal intact.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `image` | L'image d'entrée à traiter | IMAGE | Oui | - |
| `invite` | Invite pour la génération de l'image (par défaut : vide) | STRING | Oui | - |
| `n` | Le nombre d'images à générer (par défaut : 1) | INT | Oui | 1-6 |
| `graine` | Graine déterminant si le nœud doit se réexécuter ; les résultats réels sont non déterministes quelle que soit la graine (par défaut : 0) | INT | Oui | 0-18446744073709551615 |
| `recraft_style` | Sélection facultative du style pour l'arrière-plan généré. Si non fourni, utilise par défaut le style "realistic_image" | STYLEV3 | Non | - |
| `invite négative` | Description textuelle facultative des éléments indésirables sur une image (par défaut : vide) | STRING | Non | - |

**Remarque :** Le paramètre `seed` contrôle le moment où le nœud se réexécute mais ne garantit pas des résultats déterministes en raison de la nature de l'API externe.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `IMAGE` | La ou les images générées avec l'arrière-plan remplacé | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftReplaceBackgroundNode/fr.md)

---
**Source fingerprint (SHA-256):** `305cb8c542159a089b1fa03971205b23d50c8a328af006e284fb27011070f6bd`
