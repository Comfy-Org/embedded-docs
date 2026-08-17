# Recraft Remplacer l’arrière-plan

Remplacez l'arrière-plan de l'image en fonction de l'invite fournie. Ce nœud utilise l'API Recraft pour générer de nouveaux arrière-plans pour vos images selon votre description textuelle, vous permettant de transformer complètement l'arrière-plan tout en conservant le sujet principal intact.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image d'entrée à traiter | IMAGE | Oui | - |
| `prompt` | Invite pour la génération de l'image (par défaut : vide) | STRING | Oui | - |
| `n` | Le nombre d'images à générer (par défaut : 1) | INT | Oui | 1-6 |
| `seed` | Graine pour déterminer si le nœud doit s'exécuter à nouveau ; les résultats réels sont non déterministes quelle que soit la graine (par défaut : 0) | INT | Oui | 0-18446744073709551615 |
| `recraft_style` | Sélection facultative du style pour l'arrière-plan généré. Si non fourni, le style par défaut est « realistic_image » | STYLEV3 | Non | - |
| `negative_prompt` | Une description textuelle facultative des éléments indésirables sur une image (par défaut : vide) | STRING | Non | - |

**Remarque :** Le paramètre `seed` contrôle le moment où le nœud s'exécute à nouveau mais ne garantit pas de résultats déterministes en raison de la nature de l'API externe.

**Remarque :** Chaque image du lot d'entrée est traitée individuellement ; le nœud renvoie `n` images avec arrière-plan remplacé pour chaque image d'entrée.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L'image ou les images générées avec l'arrière-plan remplacé | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftReplaceBackgroundNode/fr.md)

---
**Source fingerprint (SHA-256):** `45a2607ae73cc67caa98d33bf536feda83a2021d960dec7cca76cbe0b9fc47ef`
