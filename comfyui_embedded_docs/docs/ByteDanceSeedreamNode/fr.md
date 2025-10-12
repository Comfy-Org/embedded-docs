> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNode/fr.md)

Le nœud ByteDance Seedream 4 offre des capacités unifiées de génération d'images à partir de texte et d'édition précise par instructions textuelles jusqu'à une résolution de 4K. Il peut créer de nouvelles images à partir d'invitations textuelles ou modifier des images existantes en utilisant des instructions textuelles. Le nœud prend en charge à la fois la génération d'image unique et la génération séquentielle de plusieurs images liées.

## Entrées

| Paramètre | Type de données | Type d'entrée | Défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | COMBO | "seedream-4-0-250828" | ["seedream-4-0-250828"] | Nom du modèle |
| `prompt` | STRING | STRING | "" | - | Invitation textuelle pour créer ou modifier une image. |
| `image` | IMAGE | IMAGE | - | - | Image(s) d'entrée pour la génération image-à-image. Liste de 1 à 10 images pour une génération à référence unique ou multiple. |
| `size_preset` | STRING | COMBO | Premier préréglage de RECOMMENDED_PRESETS_SEEDREAM_4 | Tous les libellés de RECOMMENDED_PRESETS_SEEDREAM_4 | Choisir une taille recommandée. Sélectionner Custom pour utiliser la largeur et la hauteur ci-dessous. |
| `width` | INT | INT | 2048 | 1024-4096 (pas de 64) | Largeur personnalisée pour l'image. La valeur n'est utilisée que si `size_preset` est défini sur `Custom` |
| `height` | INT | INT | 2048 | 1024-4096 (pas de 64) | Hauteur personnalisée pour l'image. La valeur n'est utilisée que si `size_preset` est défini sur `Custom` |
| `sequential_image_generation` | STRING | COMBO | "disabled" | ["disabled", "auto"] | Mode de génération d'images groupées. 'disabled' génère une seule image. 'auto' laisse le modèle décider s'il faut générer plusieurs images liées (par exemple, scènes d'histoire, variations de personnage). |
| `max_images` | INT | INT | 1 | 1-15 | Nombre maximum d'images à générer lorsque sequential_image_generation='auto'. Le total des images (entrée + générées) ne peut pas dépasser 15. |
| `seed` | INT | INT | 0 | 0-2147483647 | Graine à utiliser pour la génération. |
| `watermark` | BOOLEAN | BOOLEAN | True | - | Indique s'il faut ajouter un filigrane "Généré par IA" à l'image. |
| `fail_on_partial` | BOOLEAN | BOOLEAN | True | - | Si activé, interrompt l'exécution si des images demandées sont manquantes ou renvoient une erreur. |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | Image(s) générée(s) basée(s) sur les paramètres d'entrée et l'invitation |
