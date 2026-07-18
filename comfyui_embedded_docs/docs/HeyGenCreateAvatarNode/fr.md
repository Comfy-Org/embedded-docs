# HeyGenCreateAvatarNode

Créez un avatar HeyGen réutilisable à partir d'une photo d'une personne ou d'une invite textuelle décrivant un personnage à générer. L'identifiant de l'avatar obtenu peut être utilisé avec le nœud Vidéo d'avatar HeyGen pour créer des vidéos mettant en scène cet avatar.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `source` | Générer un nouveau personnage à partir d'une invite textuelle, ou créer l'avatar à partir d'une photo connectée d'une personne. | COMBO | Oui | `"prompt"`<br>`"photo"` |

Lorsque `source` est défini sur `"prompt"`, les paramètres supplémentaires suivants deviennent disponibles :

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Description de l'avatar à générer (jusqu'à 1000 caractères). | STRING | Oui | 1 à 1000 caractères |
| `reference_images` | Jusqu'à 3 images de référence guidant l'apparence générée. | IMAGE | Non | 0 à 3 images |

Lorsque `source` est défini sur `"photo"`, le paramètre supplémentaire suivant devient disponible :

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `identity_photo` | Photo de la personne à transformer en avatar. Réduite automatiquement si elle dépasse 2K. | IMAGE | Oui | Image unique |

**Remarque :** Le paramètre `source` bascule entre deux modes. En mode `"prompt"`, vous fournissez une description textuelle et éventuellement jusqu'à 3 images de référence. En mode `"photo"`, vous fournissez une seule photo d'une personne. Ces modes sont mutuellement exclusifs.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `avatar_id` | Identifiant de l'apparence de l'avatar. Transmettez-le au paramètre `custom_avatar_id` du nœud Vidéo d'avatar HeyGen ; sauvegardez-le pour réutiliser l'avatar ultérieurement. | STRING |
| `preview` | Image d'aperçu de l'avatar généré. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenCreateAvatarNode/fr.md)

---
**Source fingerprint (SHA-256):** `c60e9cdb0d91fb5ec6ea83b503b9aa10c978ce065a16c751a52e90c12e70a5e2`
