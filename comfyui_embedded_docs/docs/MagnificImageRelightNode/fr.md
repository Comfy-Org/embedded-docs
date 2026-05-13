> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageRelightNode/fr.md)

Le nœud Magnific Image Relight ajuste l'éclairage d'une image d'entrée. Il peut appliquer un éclairage stylisé basé sur une invite textuelle ou transférer les caractéristiques d'éclairage d'une image de référence facultative. Le nœud offre divers contrôles pour affiner la luminosité, le contraste et l'ambiance générale du résultat final.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `image` | IMAGE | Oui | N/D | L'image à rééclairer. Exactement une image est requise. Dimensions minimales : 160x160 pixels. Le rapport hauteur/largeur doit être compris entre 1:3 et 3:1. |
| `prompt` | STRING | Non | N/D | Indication descriptive pour l'éclairage. Prend en charge la notation d'accentuation (1-1.4). Par défaut : chaîne vide. |
| `light_transfer_strength` | INT | Oui | 0 à 100 | Intensité d'application du transfert de lumière. Par défaut : 100. |
| `style` | COMBO | Oui | `"standard"`<br>`"darker_but_realistic"`<br>`"clean"`<br>`"smooth"`<br>`"brighter"`<br>`"contrasted_n_hdr"`<br>`"just_composition"` | Préférence de rendu stylistique. |
| `interpolate_from_original` | BOOLEAN | Oui | N/D | Limite la liberté de génération pour correspondre davantage à l'original. Par défaut : Faux. |
| `change_background` | BOOLEAN | Oui | N/D | Modifie l'arrière-plan en fonction de l'invite/de la référence. Par défaut : Vrai. |
| `preserve_details` | BOOLEAN | Oui | N/D | Préserve la texture et les détails fins de l'original. Par défaut : Vrai. |
| `advanced_settings` | DYNAMICCOMBO | Oui | `"disabled"`<br>`"enabled"` | Options de réglage fin pour un contrôle avancé de l'éclairage. Lorsqu'il est réglé sur `"enabled"`, des paramètres supplémentaires deviennent disponibles. |
| `reference_image` | IMAGE | Non | N/D | Image de référence facultative pour transférer l'éclairage. Si fournie, exactement une image est requise. Dimensions minimales : 160x160 pixels. Le rapport hauteur/largeur doit être compris entre 1:3 et 3:1. |

**Remarque sur les paramètres avancés :** Lorsque `advanced_settings` est réglé sur `"enabled"`, les paramètres imbriqués suivants deviennent actifs :

* `whites` : Ajuste les tons les plus clairs de l'image. Plage : 0 à 100. Par défaut : 50.
* `blacks` : Ajuste les tons les plus foncés de l'image. Plage : 0 à 100. Par défaut : 50.
* `brightness` : Réglage global de la luminosité. Plage : 0 à 100. Par défaut : 50.
* `contrast` : Réglage du contraste. Plage : 0 à 100. Par défaut : 50.
* `saturation` : Réglage de la saturation des couleurs. Plage : 0 à 100. Par défaut : 50.
* `engine` : Sélection du moteur de traitement. Options : `"automatic"`, `"balanced"`, `"cool"`, `"real"`, `"illusio"`, `"fairy"`, `"colorful_anime"`, `"hard_transform"`, `"softy"`.
* `transfer_light_a` : L'intensité du transfert de lumière. Options : `"automatic"`, `"low"`, `"medium"`, `"normal"`, `"high"`, `"high_on_faces"`.
* `transfer_light_b` : Modifie également l'intensité du transfert de lumière. Peut être combiné avec le contrôle précédent pour des effets variés. Options : `"automatic"`, `"composition"`, `"straight"`, `"smooth_in"`, `"smooth_out"`, `"smooth_both"`, `"reverse_both"`, `"soft_in"`, `"soft_out"`, `"soft_mid"`, `"style_shift"`, `"strong_shift"`.
* `fixed_generation` : Garantit une sortie cohérente avec les mêmes réglages. Par défaut : Vrai.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `image` | IMAGE | L'image rééclairée. |

---
**Source fingerprint (SHA-256):** `c260b7c88a267a20fdea7f436404fe96ede782bc522ab29da36e94c20f7330cd`
