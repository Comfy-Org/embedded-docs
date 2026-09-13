# Recraft Remplacer l’arrière-plan

Remplace l'arrière-plan d'une image en fonction du prompt fourni. Ce nœud utilise l'API Recraft pour générer de nouveaux arrière-plans pour vos images selon votre description textuelle, ce qui vous permet de transformer complètement l'arrière-plan tout en conservant intact le sujet principal. Chaque image du lot d'entrée est traitée séparément, et les résultats sont combinés en un seul lot de sortie.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `image` | L'image d'entrée à traiter | IMAGE | Oui | - |
| `prompt` | Prompt pour la génération d'image (par défaut : vide) | STRING | Oui | - |
| `n` | Le nombre d'images à générer (par défaut : 1) | INT | Oui | 1-6 |
| `seed` | Graine permettant de déterminer si le nœud doit être réexécuté ; les résultats réels sont non déterministes quelle que soit la graine (par défaut : 0) | INT | Oui | 0-18446744073709551615 |
| `recraft_style` | Sélection de style facultative pour l'arrière-plan généré. Si non fournie, utilise par défaut le style "realistic_image" | STYLEV3 | Non | - |
| `negative_prompt` | Description textuelle facultative des éléments indésirables dans une image (par défaut : vide) | STRING | Non | - |

**Remarques :**
- Le paramètre `seed` contrôle le moment où le nœud se réexécute, mais ne garantit pas des résultats déterministes en raison de la nature de l'API externe.
- Lorsque `recraft_style` n'est pas connecté ou est laissé vide, le nœud revient au style `realistic_image`.
- Lorsque `negative_prompt` est laissé vide, il n'est pas envoyé avec la requête.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L'image ou les images générées avec l'arrière-plan remplacé. Pour chaque image d'entrée, le nombre de résultats générés est déterminé par `n`. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftReplaceBackgroundNode/fr.md)

---
**Source fingerprint (SHA-256):** `45a2607ae73cc67caa98d33bf536feda83a2021d960dec7cca76cbe0b9fc47ef`
