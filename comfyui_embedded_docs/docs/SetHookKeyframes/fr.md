# Définir les Images Clés de Crochet

Le nœud Set Hook Keyframes vous permet d'appliquer une planification d'images clés à des groupes de hooks existants. Il prend un groupe de hooks et applique éventuellement des informations de temporisation d'images clés pour contrôler le moment d'exécution des différents hooks pendant le processus de génération. Lorsque des images clés sont fournies, le nœud clone le groupe de hooks et définit la temporisation des images clés sur tous les hooks du groupe.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `crochets` | Le groupe de hooks auquel la planification d'images clés sera appliquée | HOOKS | Oui | - |
| `crochet_kf` | Groupe d'images clés optionnel contenant les informations de temporisation pour l'exécution des hooks | HOOK_KEYFRAMES | Non | - |


| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `hooks` | Le groupe de hooks modifié avec la planification d'images clés appliquée (cloné si des images clés ont été fournies) | HOOKS |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetHookKeyframes/fr.md)

---
**Source fingerprint (SHA-256):** `48908e5247b18e5b7b1d894c2f1adcf6403e499125b0c3eb05978584b3d5759b`
