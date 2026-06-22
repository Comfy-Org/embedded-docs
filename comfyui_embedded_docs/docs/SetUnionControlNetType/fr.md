# Définir le Type de Réseau de Contrôle d'Union

Le nœud SetUnionControlNetType vous permet de spécifier le type de réseau de contrôle à utiliser pour le conditionnement. Il prend un réseau de contrôle existant et définit son type de contrôle en fonction de votre sélection, créant ainsi une copie modifiée du réseau de contrôle avec la configuration de type spécifiée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `réseau_de_contrôle` | Le réseau de contrôle à modifier avec un nouveau paramètre de type | CONTROL_NET | Oui | - |
| `type` | Le type de réseau de contrôle à appliquer. Utilisez "auto" pour la détection automatique du type ou sélectionnez un type de réseau de contrôle spécifique parmi les options disponibles | STRING | Oui | `"auto"`<br>Toutes les clés UNION_CONTROLNET_TYPES disponibles |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `réseau_de_contrôle` | Le réseau de contrôle modifié avec le paramètre de type spécifié appliqué | CONTROL_NET |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetUnionControlNetType/fr.md)

---
**Source fingerprint (SHA-256):** `a64308aec96784f08b6f3f8e96e85f532bd1c536301739e7252b2c7978921b5a`
