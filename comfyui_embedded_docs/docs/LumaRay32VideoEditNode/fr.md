# LumaRay32VideoEditNode

Ce nœud re-rend une vidéo existante sous une nouvelle instruction en utilisant Luma Ray 3.2, vous permettant de restyler, rééclairer, ajouter ou supprimer des éléments tout en conservant le mouvement d'origine. La vidéo source peut durer jusqu'à 18 secondes, et la vidéo éditée conserve la durée originale de la source.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `video` | Vidéo source à éditer. Jusqu'à 18 secondes. | VIDEO | Oui | - |
| `prompt` | Décrit la modification souhaitée. | STRING | Oui | - |
| `resolution` | La résolution de sortie pour la vidéo éditée. | COMBO | Oui | `"360p"`<br>`"540p"`<br>`"720p"`<br>`"1080p"` |
| `strength` | Dans quelle mesure préserver ou réimaginer la source. "auto" laisse Ray 3.2 choisir ; adhere_* préserve le plus, flex_* est équilibré, reimagine_* change le plus. (par défaut : "auto") | COMBO | Oui | `"auto"`<br>`"adhere_1"`<br>`"adhere_2"`<br>`"adhere_3"`<br>`"flex_1"`<br>`"flex_2"`<br>`"flex_3"`<br>`"reimagine_1"`<br>`"reimagine_2"`<br>`"reimagine_3"` |
| `seed` | Graine pour la reproductibilité. | INT | Oui | - |

**Remarque :** Le `prompt` doit contenir entre 1 et 6000 caractères. La vidéo source ne doit pas dépasser 18 secondes de durée.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `VIDEO` | La vidéo éditée en sortie. | VIDEO |
| `generation_id` | L'identifiant unique pour la requête de génération. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32VideoEditNode/fr.md)

---
**Source fingerprint (SHA-256):** `936d9d7da3fdee9b0b468781fd470751db01f772f3c5c20582da7fb1ff85e6e6`
