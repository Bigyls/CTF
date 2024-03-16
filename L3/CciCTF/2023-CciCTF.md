---
categories:
- CTF
- 2023
- CciCTF
status: done
tags: CTF 
---
# CciCTF

**Website :** [CciCTF](https://campus.vaucluse.cci.fr/)

![X date](https://img.shields.io/badge/date-31/03/2023-yellow.svg)
![X total points](https://img.shields.io/badge/total_points-2500-blue.svg)
![X rank](https://img.shields.io/badge/team_ranking-16-purple.svg)
![X solo](https://img.shields.io/badge/team-alone-orange.svg)

**Description :** Nos apprentis de deuxième année en cyber-sécurité et leur enseignants sont ravis de vous inviter la nuit du 31 mars au 1er avril sur le Campus de la CCI de Vaucluse pour une capture de drapeau numérique !

## **Table of Contents**

1. Reverse
	- [Hello_World_!](#Hello_World_!)
	- [Reverse](#Reverse)
	- [Some_Base](#Some_Base)
	- [Security_Key](#Security_Key)
	- [HackMatrix](#HackMatrix)
	- [Mot_De_Passe_Perdu](#Mot_De_Passe_Perdu)
	- [Reverser_Don't_Like_Licencer](#Reverser_Don't_Like_Licencer)
	 - [N0pe](#N0pe)
	- [POV](#POV)

2. Web
	- [Get_Password](#Get_Password)
	- [BOT](#BOT)
	- [Jeu_Gratuit_!](#Jeu_Gratuit_!)
	- [Site_Interdit_Aux_Mineurs](#Site_Interdit_Aux_Mineurs)
	- [File_Upload](#File_Upload)

1. Forensics
	- [Pcap2](#Pcap2)
	- [Investiga_1](#Investiga_1)
	- [Gmail_Proof](#Gmail_Proof)

## Hello_World_!

![X category](https://img.shields.io/badge/category-Reverse-blue.svg)
![X points](https://img.shields.io/badge/points-100-green.svg)

**Challenge Description :** Hum... Voici un fichier binaire. Peut-être qu'en le décompilant vous pouvez en tirer quelque chose ?

### Approach

I know `strings` command, let's check if I can see something:
![](Images/HelloWorld_1.png)

Yes ! I have the flag !

![](Images/HelloWorld_2.png)

**Flag :** `NHM2I{simpl3_introduction_to_r3v3rs3}`

## Reverse

![X category](https://img.shields.io/badge/category-Reverse-blue.svg)
![X points](https://img.shields.io/badge/points-100-green.svg)

**Challenge Description :** Hum... Voici un fichier binaire. Peut-être qu'en le décompilant vous pouvez en tirer quelque chose ?

### Approach

`strings` command work well, so let's try it:
![](Images/Reverse_1.png)

I have a part of flag, but i also have the password of the challenge, I launch the binary and obtain the flag.

**Flag :** `flag{r3ver5er_0f_th3_ye4rs_Gg}`

## Some_Base

![X category](https://img.shields.io/badge/category-Reverse-blue.svg)
![X points](https://img.shields.io/badge/points-200-green.svg)

**Challenge Description :** Voici un nouveau fichier. A vous de jouer :p

A `strings` command don't help me for this challenge. I can launch my favorite `BinaryNinja` and analyse the code. 

![](Images/SomeBase_1.png)

I can see an `if` condition who goes for `print` the flag in the terminal but I never go in. With `BinaryNinja` I can change conditions with a `PATCH` :

![](Images/SomeBase_2.png)

Run binary and now I always go into he condition for `print` my flag :)

![](Images/SomeBase_3.png)

**Flag :** `NHM2I{this_is_a_gr3at_r3v3rs3!}`

## Security_Key

![X category](https://img.shields.io/badge/category-Reverse-blue.svg)
![X points](https://img.shields.io/badge/points-200-green.svg)

**Challenge Description :** Too long  :(

This is the same methodology for this challenge as the previous one. Open `BinaryNinja` analyse logic of the code and PATCH it.

![](Images/SecurityKey_1.png)

**Flag :** `NHM2i{AAAA-Z10N-42-OK-CodeByrZmFeatTrinity}`

## HackMatrix

![X category](https://img.shields.io/badge/category-Reverse-blue.svg)
![X points](https://img.shields.io/badge/points-200-green.svg)

**Challenge Description :** Also too long :(

After launch the binary and multiple tests, I found the same result and no flag. 

![](Images/HackMatrix_1.png)

So let's open `BinaryNinja` and analyse the code !

![](Images/HackMatrix_2.png)

I can see the `if` condition who give me the 0 flag. So I can invert it for always go in `else`: 

![](Images/HackMatrix_3.png)

And Magic operates !

![](Images/HackMatrix_4.png)

![](Images/HackMatrix_5.png)

**Flag :** `NHM2I{e03326d6_093736bb_2946b47f_b804e4b8}`

## Mot_De_Passe_Perdu

![X category](https://img.shields.io/badge/category-Reverse-blue.svg)
![X points](https://img.shields.io/badge/points-200-green.svg)

**Challenge Description :** Retrouver le mot de passe qui permet d’accéder à l'application.

I the same logic, open `BinaryNinja` and analyse the code.

In this challenge I do a PATCH but I don't have see the password in plain text over my eyes LoL
![](Images/MotDePassePerdu_1.png)

![](Images/MotDePassePerdu_2.png)

![](Images/MotDePassePerdu_3.png)

![](Images/MotDePassePerdu_4.png)

**Flag :** `NHM2I{ac78c15c-27e7-43af-b8b1-29df4e5831d8}`

## N0pe

![X category](https://img.shields.io/badge/category-Reverse-blue.svg)
![X points](https://img.shields.io/badge/points-200-green.svg)

**Challenge Description :** J'ai acheté un nouveau jeu mais j'ai perdu ma licence. Pouvez-vous m'aider ??

I love `BinaryNinja` and this challenge is proof for why. I have launch it and analyse code. I see `print_flag()` function. So, I just say to `BinaryNinja` to never go in `if` condition for always print flag !

![](Images/ReverseLicencer_1.png)

After PATCH:
![](Images/ReverseLicencer_2.png)

I can put any characters after modifications:
![](Images/ReverseLicencer_3.png)

![](Images/ReverseLicencer_4.png)

**Flag :** `NHM2I{Byp4s5_L1cenc3_1s_34sy}`

## N0pe

![X category](https://img.shields.io/badge/category-Reverse-blue.svg)
![X points](https://img.shields.io/badge/points-200-green.svg)

**Challenge Description :** Too lonnnng :(

An other challenge finished with `BinaryNinja` and the same methodology:

I can put any characters, the flags is printed.
![](Images/N0pe_1.png)

![](Images/N0pe_2.png)

**Flag :** `NHM2I{jkMOPawBRl-SjwMGEu1EJ-4Z4TNCtzxd}`

## POV

![X category](https://img.shields.io/badge/category-Reverse-blue.svg)
![X points](https://img.shields.io/badge/points-200-green.svg)

**Challenge Description :** Un élève à **encore** fait n'importe quoi avec son code, je suis M. Naviliat (aka the GOAT), je suis là pour l'aider. Voilà ce qu'il m'a rendu...

This challenge is an other time, break with `BinaryNinja`.

![](Images/POV_1.png)

**Flag :** `NHM2I{b035a154-defe-4250-8c6a-3fe3562d9c1c}`

## Get_Password

![X category](https://img.shields.io/badge/category-Web-blue.svg)
![X points](https://img.shields.io/badge/points-100-green.svg)

**Challenge Description :** Tooooo long :(

After a short visit of the web site, in source code, I see a bad variable `password`. This variable contain the password in cipher text:
![](Images/GetPassword_1.png)

`dcode` works very well:
![](Images/GetPassword_2.png)

I just to login me and have the flag:
![](Images/GetPassword_3.png)

![](Images/GetPassword_4.png)

**Flag :** `NHM2I{...}`

## BOT

![X category](https://img.shields.io/badge/category-Web-blue.svg)
![X points](https://img.shields.io/badge/points-100-green.svg)

**Challenge Description :** Too long :(

I launch a dirb for this challenge and fall on `sitemap.xml` page. The flag as here.

![](Images/BOT_1.png)

**Flag :** `NHM2I{ENUMERATION_IS_THE_KEY}`

## Jeu_Gratuit_!

![X category](https://img.shields.io/badge/category-Web-blue.svg)
![X points](https://img.shields.io/badge/points-100-green.svg)

**Challenge Description :** Un ami m'a recommandé ce jeu, mais je n'arrive pas à me connecter. Sais-tu comment faire ?

![](Images/JeuGratuit_1.png)

After checking all basics point, I see a text box and button disabled. I have to enabled it:
![](Images/JeuGratuit_2.png)

![](Images/JeuGratuit_3.png)

**Flag :** `NHM2I{!I3stNullC3Dev}`

## Site_Interdit_Aux_Mineurs

![X category](https://img.shields.io/badge/category-Web-blue.svg)
![X points](https://img.shields.io/badge/points-100-green.svg)

**Challenge Description :** Nous sommes tombés sur ce site par hasard et nous ne pouvons pas y accéder, car il détecte que nous sommes pas majeurs.

![](Images/Mineur_1.png)

I can test to change `span` code where it's mentioned he age for have the flag:
![](Images/Mineur_2.png)
![](Images/Mineur_4.png)
![](Images/Mineur_3.png)

**Flag :** `NHM2I{...}`

## File_Upload

![X category](https://img.shields.io/badge/category-Web-blue.svg)
![X points](https://img.shields.io/badge/points-200-green.svg)

**Challenge Description :** I don't have :(

![](Images/FileUpload_1.png)

This web site contain a file upload section who accept just `.php` files. Let's try basic file upload with php reverse shell:

I setup my reverse shell:
![](Images/FileUpload_3.png)

![](Images/FileUpload_2.png)

Ok, now I can launch `nc` listener and click on the click for have shell:

I just have to check where is flag for `cat` it:
![](Images/FileUpload_4.png)

**Flag :** `NHM2I{GG_Fileuploaded!!}`

## Pcap2

![X category](https://img.shields.io/badge/category-Forensics-blue.svg)
![X points](https://img.shields.io/badge/points-100-green.svg)

**Challenge Description :** Too long :(

this challenge is just a classic challenge with wireshark. Follow TCP stream:
![](Images/Pcap2_1.png)

![](Images/Pcap2_2.png)

**Flag :** `NHM2I{hjdhdh-JDJ8786D-jkfh0-87897-RTbd7}`

## Investiga_1

![X category](https://img.shields.io/badge/category-Forensics-blue.svg)
![X points](https://img.shields.io/badge/points-100-green.svg)

**Challenge Description :** Retrouver le flag dans la trace `PCAP`.

This challenge more difficult to see but ICMP does not contain "W3lld0neP1ng" in basic trame.
![](Images/Investiga1_1.png)

![](Images/Investiga1_2.png)

**Flag :** `NHM2I{W3lld0neP1ng}`

## Gmail_Proof

![X category](https://img.shields.io/badge/category-Forensics-blue.svg)
![X points](https://img.shields.io/badge/points-100-green.svg)

**Challenge Description :** Too Looong :(

An simple `Ctrl+F` on the file permit me to see the flag:
![](Images/Gmail_1.png)

![](Images/Gmail_2.png)

**Flag :** `NHM2I{Qu3Del4PubSur73mail!}`