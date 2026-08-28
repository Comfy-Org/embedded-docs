# Créer un Avatar HeyGen

Créez un avatar HeyGen réutilisable à partir d'une photo d'une personne ou d'une invite textuelle décrivant un personnage à générer. L'`avatar_id` résultant peut être utilisé avec le nœud HeyGen Avatar Video, et doit être enregistré pour réutiliser l'avatar dans de futurs workflows.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `source` | Génère un nouveau personnage à partir d'une invite textuelle, ou crée l'avatar à partir d'une photo connectée d'une personne. | DYNAMIC_COMBO | Oui | `"prompt"`<br>`"photo"` |

### Entrées du prompt

Disponible lorsque `source` est défini sur `"prompt"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Description de l'avatar à générer (jusqu'à 1000 caractères). Doit contenir au moins 1 caractère non blanc. Par défaut : chaîne vide. | STRING | Oui | 1 à 1000 caractères |

### Entrées de photo

Disponible lorsque `source` est défini sur `"photo"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `identity_photo` | Photo de la personne à transformer en avatar. Redimensionnée automatiquement si elle dépasse 2K. | IMAGE | Oui | Image unique |

### Entrées de référence

Disponible lorsque `source` est défini sur `"prompt"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `reference_images` | Emplacement extensible : connectez jusqu'à 3 images (`ref_image_1`...`ref_image_3`) pour guider l'apparence générée. Les images sont redimensionnées automatiquement si elles dépassent 2K. | IMAGE | Non | 0 à 3 images |

**Remarque :** Le paramètre `source` bascule entre deux modes mutuellement exclusifs. En mode `"prompt"`, `prompt` est requis et jusqu'à 3 images de référence peuvent être connectées en option. En mode `"photo"`, `identity_photo` est requis. Les photos et les images de référence sont redimensionnées automatiquement si elles dépassent 2K ; plus de 3 images de référence ne sont pas acceptées.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `avatar_id` | Identifiant de l'apparence de l'avatar. Transmettez-le à `custom_avatar_id` de HeyGen Avatar Video ; enregistrez-le pour réutiliser l'avatar ultérieurement. | STRING |
| `aperçu` | Image d'aperçu de l'avatar généré. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenCreateAvatarNode/fr.md)

---
**Source fingerprint (SHA-256):** `c60e9cdb0d91fb5ec6ea83b503b9aa10c978ce065a16c751a52e90c12e70a5e2`
