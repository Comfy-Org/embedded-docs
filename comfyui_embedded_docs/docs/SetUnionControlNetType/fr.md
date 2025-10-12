> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetUnionControlNetType/fr.md)

Le nœud SetUnionControlNetType vous permet de spécifier le type de réseau de contrôle à utiliser pour le conditionnement. Il prend un réseau de contrôle existant et définit son type de contrôle en fonction de votre sélection, créant ainsi une copie modifiée du réseau de contrôle avec la configuration de type spécifiée.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `réseau_de_contrôle` | CONTROL_NET | Oui | - | Le réseau de contrôle à modifier avec un nouveau paramètre de type |
| `type` | STRING | Oui | `"auto"`<br>Toutes les clés UNION_CONTROLNET_TYPES disponibles | Le type de réseau de contrôle à appliquer. Utilisez "auto" pour la détection automatique du type ou sélectionnez un type de réseau de contrôle spécifique parmi les options disponibles |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `réseau_de_contrôle` | CONTROL_NET | Le réseau de contrôle modifié avec le paramètre de type spécifié appliqué |
