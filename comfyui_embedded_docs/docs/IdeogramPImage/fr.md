# Ideogram P-Image

---

Ideogram & Pruna P-Image génère des images à partir d’un prompt texte grâce au modèle texte-image rapide d’Ideogram, réputé pour sa typographie soignée et son photoréalisme. Il prend également en charge les légendes JSON structurées d’Ideogram 4.0 pour un contrôle précis des chaînes de texte, des couleurs et de la mise en page. Le nœud renvoie l’image ou les images générées ainsi que le prompt final à partir duquel l’image a réellement été générée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt texte. Accepte également une légende JSON structurée Ideogram 4.0 (couleurs exactes en hexadécimal #RRGGBB, chaînes de texte exactes, disposition en boîtes englobantes) — réglez `prompt_upsampling` sur OFF pour l’utiliser tel quel. Ne doit pas être vide. (par défaut : "") | STRING | Oui | Tout texte non vide |
| `quality` | Niveau de vitesse/prix/qualité. MEDIUM est le défaut quotidien ; HIGH pour les prompts complexes, les détails fins et les textes difficiles ; VERY_LOW/LOW pour les brouillons à grande échelle. Les textes difficiles sont rendus médiocrement en dessous de MEDIUM. (par défaut : "MEDIUM") | COMBO | Oui | "VERY_LOW"<br>"LOW"<br>"MEDIUM"<br>"HIGH" |
| `resolution` | Classe de taille de sortie (les pixels exacts suivent le ratio d’aspect, p. ex. 16:9 donne 1280x720 en 1K et 2560x1440 en 2K). Préférez HIGH + 2K pour une typographie nette. (par défaut : "1K") | COMBO | Oui | "1K"<br>"2K" |
| `aspect_ratio` | Le ratio d’aspect pour la génération d’images. (par défaut : "1:1") | COMBO | Oui | "1:3"<br>"3:1"<br>"1:2"<br>"2:1"<br>"9:16"<br>"16:9"<br>"10:16"<br>"16:10"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"4:5"<br>"5:4"<br>"1:1" |
| `prompt_upsampling` | Développe les prompts courts en une légende structurée détaillée avant la génération (le prompt réécrit est renvoyé sous la forme de `final_prompt`). Réglez sur OFF lorsque vous fournissez votre propre légende JSON ou un texte exact. (par défaut : "AUTO") | COMBO | Oui | "AUTO"<br>"ON"<br>"OFF" |
| `seed` | Seed pour une génération reproductible. Avec `prompt_upsampling` sur OFF, la même seed et les mêmes paramètres renvoient la même image ; avec ON/AUTO, la réécriture du prompt varie à chaque exécution — reproduisez un résultat en réutilisant sa sortie `final_prompt` avec `prompt_upsampling` sur OFF et la même seed. (par défaut : 42) | INT | Non | 0 à 2147483647 |

**Remarque sur les contraintes :** Le prompt doit contenir au moins un caractère non blanc, sinon le nœud échoue. Réglez `prompt_upsampling` sur OFF lorsque vous fournissez votre propre légende JSON structurée ou un texte exact. Lorsque `prompt_upsampling` est sur ON ou AUTO, le prompt est réécrit avant la génération, donc la même seed peut ne pas reproduire la même image ; pour reproduire une image, réutilisez sa sortie `final_prompt` avec `prompt_upsampling` sur OFF et la même seed.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L’image ou les images générées, renvoyées sous forme de lot d’images. Si le filtre de sécurité du contenu d’Ideogram bloque la génération, une erreur est levée à la place. | IMAGE |
| `final_prompt` | Le prompt à partir duquel l’image a réellement été générée (la légende structurée réécrite lorsque `prompt_upsampling` a fonctionné, sinon votre prompt). Réinjectez-le avec `prompt_upsampling` sur OFF et la même seed pour reproduire cette image. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPImage/fr.md)

---
**Source fingerprint (SHA-256):** `6b014c2f097c49b5930f38869a4e2da0ebb19863763ae5817d6e566a36d2b8e8`
