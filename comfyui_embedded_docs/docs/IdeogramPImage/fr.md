# IdeogramPImage

Ideogram P-Image génère des images à partir d’un prompt texte en utilisant le modèle texte-image rapide d’Ideogram, connu pour sa typographie soignée et son photoréalisme. Il prend également en charge les légendes JSON structurées Ideogram 4.0 pour un contrôle précis des chaînes de texte, des couleurs et de la mise en page. Le nœud renvoie la ou les images générées ainsi que le prompt final à partir duquel l’image a réellement été générée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt texte. Accepte également une légende JSON structurée Ideogram 4.0 (couleurs exactes en hexadécimal #RRGGBB, chaînes de texte exactes, mise en page par boîtes englobantes) — définissez `prompt_upsampling` sur OFF pour l’utiliser telle quelle. Ne doit pas être vide. (défaut : "") | STRING | Oui | Tout texte |
| `quality` | Niveau de rapidité/prix/qualité. MEDIUM est le réglage quotidien par défaut ; HIGH pour les prompts complexes, les détails fins et les textes difficiles ; VERY_LOW/LOW pour les brouillons à grande échelle. Les textes difficiles sont mal rendus en dessous de MEDIUM. (défaut : "MEDIUM") | STRING | Oui | "VERY_LOW"<br>"LOW"<br>"MEDIUM"<br>"HIGH" |
| `resolution` | Classe de taille de sortie (les pixels exacts suivent le ratio d’aspect, par ex. 16:9 donne 1280x720 à 1K et 2560x1440 à 2K). Privilégiez HIGH + 2K pour une typographie nette. (défaut : "1K") | STRING | Oui | "1K"<br>"2K" |
| `aspect_ratio` | Le ratio d’aspect pour la génération d’image. (défaut : "1:1") | STRING | Oui | "1:3"<br>"3:1"<br>"1:2"<br>"2:1"<br>"9:16"<br>"16:9"<br>"10:16"<br>"16:10"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"4:5"<br>"5:4"<br>"1:1" |
| `prompt_upsampling` | Développe les prompts courts en une légende structurée détaillée avant la génération (le prompt réécrit est renvoyé comme `final_prompt`). Réglez sur OFF lorsque vous fournissez votre propre légende JSON ou un texte exact. (défaut : "AUTO") | STRING | Oui | "AUTO"<br>"ON"<br>"OFF" |
| `seed` | Graine pour une génération reproductible. Avec `prompt_upsampling` sur OFF, la même graine et les mêmes paramètres renvoient la même image ; avec ON/AUTO, la réécriture du prompt varie à chaque exécution — pour reproduire un résultat, réutilisez la sortie `final_prompt` avec `prompt_upsampling` sur OFF et la même graine. (défaut : 42) | INT | Non | 0 à 2147483647 |

**Remarque sur les contraintes :** Le prompt doit contenir au moins un caractère non-blanc, sinon le nœud échoue. Définissez `prompt_upsampling` sur OFF lorsque vous fournissez votre propre légende JSON structurée ou un texte exact. Lorsque `prompt_upsampling` est sur ON ou AUTO, le prompt est réécrit avant la génération, donc la même graine peut ne pas reproduire la même image ; pour reproduire une image, réutilisez sa sortie `final_prompt` avec `prompt_upsampling` sur OFF et la même graine.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | La ou les images générées renvoyées sous forme d’un lot d’images. Si le filtre de sécurité de contenu d’Ideogram bloque la génération, une erreur est levée à la place. | IMAGE |
| `final_prompt` | Le prompt à partir duquel l’image a réellement été générée (la légende structurée réécrite lorsque `prompt_upsampling` a fonctionné, sinon votre prompt). Réinjectez-le avec `prompt_upsampling` sur OFF et la même graine pour reproduire cette image. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPImage/fr.md)

---
**Source fingerprint (SHA-256):** `7bd20aae508fee111ded32e87119ed6fc01c5ad5ba7d595e24391830a0f20bb7`
