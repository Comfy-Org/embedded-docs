# Créer un Avatar HeyGen

```markdown
Créez un avatar HeyGen réutilisable à partir d'une photo d'une personne ou d'un prompt textuel décrivant un personnage à générer. L'`avatar_id` résultant peut être utilisé avec le nœud HeyGen Avatar Video, et doit être enregistré pour réutiliser l'avatar dans de futurs workflows.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `source` | Génère un nouveau personnage à partir d'un prompt textuel, ou crée l'avatar à partir d'une photo connectée d'une personne. | DYNAMIC_COMBO | Oui | `"prompt"`<br>`"photo"` |

### Entrées Prompt

Disponibles lorsque `source` est défini sur `"prompt"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Description de l'avatar à générer (jusqu'à 1000 caractères). Doit contenir au moins 1 caractère non blanc. Par défaut : chaîne vide. | STRING | Oui | 1 à 1000 caractères |

### Entrées Photo

Disponibles lorsque `source` est défini sur `"photo"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `identity_photo` | Photo de la personne à transformer en avatar. Réduite automatiquement si elle dépasse 2K. | IMAGE | Oui | Image unique |

### Entrées de référence

Disponibles lorsque `source` est défini sur `"prompt"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `reference_images` | Emplacement extensible : connectez jusqu'à 3 images (`ref_image_1`...`ref_image_3`) pour guider l'apparence générée. Les images sont réduites automatiquement si elles dépassent 2K. | IMAGE | Non | 0 à 3 images |

**Remarque :** Le paramètre `source` bascule entre deux modes mutuellement exclusifs. En mode `"prompt"`, `prompt` est requis et jusqu'à 3 images de référence peuvent être connectées en option. En mode `"photo"`, `identity_photo` est requis. Les photos et les images de référence sont réduites automatiquement lorsqu'elles dépassent 2K ; plus de 3 images de référence ne sont pas acceptées.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `avatar_id` | ID d'apparence de l'avatar. Transmettez-le à `custom_avatar_id` de HeyGen Avatar Video ; enregistrez-le pour réutiliser l'avatar plus tard. | STRING |
| `aperçu` | Image d'aperçu de l'avatar généré. | IMAGE |
```

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenCreateAvatarNode/fr.md)

---
**Source fingerprint (SHA-256):** `3669686fc6d089909bd5d2d75292ceef05702ed3cc7b14e561bcb444c30a4e63`
