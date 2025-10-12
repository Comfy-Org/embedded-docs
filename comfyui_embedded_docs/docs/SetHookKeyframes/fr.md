> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetHookKeyframes/fr.md)

Le nœud Set Hook Keyframes permet d'appliquer une planification par images clés à des groupes de hooks existants. Il prend un groupe de hooks et applique optionnellement des informations de timing d'images clés pour contrôler quand les différents hooks sont exécutés pendant le processus de génération. Lorsque des images clés sont fournies, le nœud clone le groupe de hooks et définit le timing des images clés sur tous les hooks du groupe.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `hooks` | HOOKS | Oui | - | Le groupe de hooks auquel la planification par images clés sera appliquée |
| `hook_kf` | HOOK_KEYFRAMES | Non | - | Groupe d'images clés optionnel contenant les informations de timing pour l'exécution des hooks |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `hooks` | HOOKS | Le groupe de hooks modifié avec la planification par images clés appliquée (cloné si des images clés étaient fournies) |