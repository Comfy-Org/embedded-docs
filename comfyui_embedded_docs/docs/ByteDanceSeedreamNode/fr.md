> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNode/fr.md)

Le nœud ByteDance Seedream 4.5 & 5.0 offre des capacités unifiées de génération texte-image et d'édition précise par phrase unique, avec une résolution allant jusqu'à 4K. Il peut créer de nouvelles images à partir de descriptions textuelles ou modifier des images existantes à l'aide d'instructions textuelles. Le nœud prend en charge à la fois la génération d'images uniques et la génération séquentielle de plusieurs images connexes.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | STRING | Oui | Voir Description | Le modèle Seedream à utiliser pour la génération. Les modèles disponibles incluent les variantes seedream-4-0, seedream-4-5 et seedream-5-0. |
| `prompt` | STRING | Oui | - | Description textuelle pour créer ou modifier une image. Doit comporter au moins 1 caractère. |
| `image` | IMAGE | Non | - | Image(s) d'entrée pour la génération image-à-image. Image(s) de référence pour la génération à référence unique ou multiple. Maximum de 10 images de référence pour la plupart des modèles, ou 14 pour seedream-5-0-260128. |
| `size_preset` | STRING | Non | Plusieurs options disponibles | Choisissez une taille recommandée. Sélectionnez Personnalisé pour utiliser la largeur et la hauteur ci-dessous. Par défaut : premier préréglage de RECOMMENDED_PRESETS_SEEDREAM_4. |
| `width` | INT | Non | 1024 à 6240 (pas de 2) | Largeur personnalisée de l'image. La valeur n'est prise en compte que si `size_preset` est défini sur `Personnalisé`. Par défaut : 2048. |
| `height` | INT | Non | 1024 à 4992 (pas de 2) | Hauteur personnalisée de l'image. La valeur n'est prise en compte que si `size_preset` est défini sur `Personnalisé`. Par défaut : 2048. |
| `sequential_image_generation` | STRING | Non | "désactivé"<br>"auto" | Mode de génération d'images groupées. "désactivé" génère une seule image. "auto" laisse le modèle décider s'il doit générer plusieurs images connexes (par exemple, scènes d'histoire, variations de personnages). Par défaut : "désactivé". |
| `max_images` | INT | Non | 1 à 15 (pas de 1) | Nombre maximal d'images à générer lorsque sequential_image_generation='auto'. Le nombre total d'images (entrée + générées) ne peut pas dépasser 15. Par défaut : 1. |
| `seed` | INT | Non | 0 à 2147483647 (pas de 1) | Graine à utiliser pour la génération. Par défaut : 0. |
| `watermark` | BOOLEAN | Non | - | Indique s'il faut ajouter un filigrane "Généré par IA" à l'image. Par défaut : Faux. |
| `fail_on_partial` | BOOLEAN | Non | - | Si activé, interrompt l'exécution si des images demandées sont manquantes ou renvoient une erreur. Par défaut : Vrai. |

**Remarques sur les contraintes des paramètres :**
- La résolution minimale de l'image dépend du modèle sélectionné : 3,68 MP pour les modèles seedream-4-5 et seedream-5-0, 0,92 MP pour les modèles seedream-4-0.
- La résolution maximale de l'image est de 10,4 MP pour les modèles seedream-5-0 et de 16,78 MP pour les autres modèles.
- Les images de référence doivent avoir un rapport hauteur/largeur compris entre 1:3 et 3:1.
- Lorsque `sequential_image_generation` est défini sur "auto", le nombre total d'images d'entrée plus `max_images` ne peut pas dépasser 15.
- Les paramètres `width` et `height` ne sont utilisés que lorsque `size_preset` est défini sur "Personnalisé".

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `IMAGE` | IMAGE | Image(s) générée(s) en fonction des paramètres d'entrée et de la description textuelle. Renvoie un tenseur d'image unique ou un lot de tenseurs d'images si plusieurs images sont générées. |

---
**Source fingerprint (SHA-256):** `ce130246026e0f5036e137bea4e193f51097e0812459586dcbeb87ef01975630`
