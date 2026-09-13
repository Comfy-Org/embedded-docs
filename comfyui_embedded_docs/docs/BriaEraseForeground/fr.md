# BriaEraseForeground

Ce nœud supprime le premier plan d'une image avec Bria et génère un nouvel arrière-plan à sa place. Tout ce que Bria identifie comme premier plan est supprimé, pas seulement les personnes, et les pixels non modifiés sont préservés. Le résultat est ré-rendu à une taille standard proche de 1 mégapixel.

Il s'agit d'un nœud API payant qui s'exécute sur le service de Bria, donc vos identifiants de l'API Comfy sont utilisés à chaque exécution.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image dont le premier plan est supprimé et remplacé par un arrière-plan généré. Seuls les canaux de couleur sont envoyés ; tout canal alpha est ignoré avant l'envoi. | IMAGE | Oui | - |
| `modération` | Paramètres de modération. Sélectionnez `"false"` pour envoyer l'image sans indicateurs de modération, ou `"true"` pour révéler les options de modération de contenu ci-dessous. Par défaut : `"false"`. | DYNAMIC_COMBO | Oui | `"false"`<br>`"true"` |

### Entrées `"false"`

Aucune entrée supplémentaire. La requête est envoyée sans indicateurs de modération de contenu.

### Entrées `"true"`

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `visual_input_moderation` | Active la modération de contenu sur l'image d'entrée. Par défaut : false. | BOOLEAN | Oui | true<br>false |
| `visual_output_moderation` | Active la modération de contenu sur l'image de sortie générée. Par défaut : false. | BOOLEAN | Oui | true<br>false |

### Remarques

- La sortie est ré-rendue à une taille standard proche de 1 mégapixel, donc l'image renvoyée peut différer en dimensions de l'entrée.
- Ce nœud est un nœud API payant ; chaque exécution coûte environ 0,0572 USD.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L'image d'entrée avec son premier plan effacé et un arrière-plan nouvellement généré à sa place. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaEraseForeground/fr.md)

---
**Source fingerprint (SHA-256):** `4d8c3c5eed97c648b1191ec41931c97caa17e98a8edd1c054ed63e80cc671b05`
