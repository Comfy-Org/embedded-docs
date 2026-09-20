# QwenImage21Cache

Le nœud QwenImage21Cache configure le cache de préfixe KV du modèle Qwen-Image 2.1 : où les clés et valeurs mises en cache sont stockées et à quelle précision. Les jetons de texte et de référence sont calculés une fois puis réutilisés à travers les étapes d'échantillonnage, ce qui constitue l'essentiel de l'accélération sur les workflows d'édition, et ce nœud vous permet d'échanger de la mémoire contre de la vitesse ou d'exclure totalement le cache. Ce nœud est marqué comme expérimental.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle Qwen-Image 2.1 dont le cache de préfixe est configuré. | MODEL | Oui | - |
| `device` | Où les clés et valeurs mises en cache sont stockées. `"auto"` (par défaut) utilise d'abord la VRAM libre, puis la RAM ; `"gpu"` stocke le cache dans la VRAM ; `"cpu"` le stocke dans la RAM et le précharge en arrière-plan du calcul, ce qui coûte peu en vitesse ; `"off"` recalcule le préfixe à chaque étape, ce qui est plus lent, mais c'est le seul moyen d'exclure totalement le cache. | COMBO | Oui | `"auto"`<br>`"gpu"`<br>`"cpu"`<br>`"off"` |
| `dtype` | Précision de stockage du cache. `"default"` est sans perte ; `"int8"` divise le cache par deux avec une précision d'environ bf16 ; `"int4"` le divise par quatre, mais double à peu près l'erreur par étape. | COMBO | Oui | `"default"`<br>`"int8"`<br>`"int4"` |

Lorsque le cache ne tient pas, le modèle recalcule le préfixe au lieu d'évincer l'emplacement de l'autre branche ; un réglage surdimensionné dégrade donc la vitesse plutôt que de faire échouer l'exécution.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `MODEL` | Le modèle avec le périphérique de cache et la précision appliqués, prêt à être échantillonné. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImage21Cache/fr.md)

---
**Source fingerprint (SHA-256):** `0c10cdb465d1ee4063273ffbb4913def3830f7e329694cd0a2e292d6f3c37ae4`
