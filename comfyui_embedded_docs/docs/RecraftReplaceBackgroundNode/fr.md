# Recraft Remplacer l’arrière-plan

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image d'entrée à traiter | IMAGE | Oui | - |
| `invite` | Invite pour la génération d'image (par défaut : vide) | STRING | Oui | - |
| `n` | Le nombre d'images à générer (par défaut : 1) | INT | Oui | 1-6 |
| `graine` | Graine pour déterminer si le nœud doit s'exécuter à nouveau ; les résultats réels sont non déterministes quelle que soit la graine (par défaut : 0) | INT | Oui | 0-18446744073709551615 |
| `recraft_style` | Sélection de style facultative pour l'arrière-plan généré. Si elle n'est pas fournie, le style par défaut est « realistic_image » | STYLEV3 | Non | - |
| `invite négative` | Une description textuelle facultative des éléments indésirables sur une image (par défaut : vide) | STRING | Non | - |

**Remarque :** Le paramètre `seed` contrôle le moment où le nœud s'exécute à nouveau mais ne garantit pas des résultats déterministes en raison de la nature de l'API externe.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | Les images générées avec l'arrière-plan remplacé. Pour chaque image d'entrée, le nombre de résultats générés est déterminé par `n`. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftReplaceBackgroundNode/fr.md)

---
**Source fingerprint (SHA-256):** `45a2607ae73cc67caa98d33bf536feda83a2021d960dec7cca76cbe0b9fc47ef`
