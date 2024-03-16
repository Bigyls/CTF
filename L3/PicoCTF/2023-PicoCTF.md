---
categories:
- CTF
- 2023
- PicoCTF
status: done
tags: CTF, 2023, PicoCTF
---
# PicoCTF

**Website :** [PicoCTF](https://picoctf.org/)

![X date](https://img.shields.io/badge/date-14/03/2023-yellow.svg)
![X total points](https://img.shields.io/badge/total_points-2500-blue.svg)
![X rank](https://img.shields.io/badge/team_ranking-1475%2F6925-purple.svg)
![X solo](https://img.shields.io/badge/team-alone-orange.svg)

**Description :** PicoCTF gamifies learning hacking with capture-the-flag puzzles created by trusted computer security and privacy experts at [Carnegie Mellon University](https://cmu.edu/).

## **Table of Contents**

1. GeneralSkills
	- [Rules](#Rules)
	- [Repetitions](#Repetitions)
	- [MoneyWare](#MoneyWare)
	- [Permissions](#Permissions)
	- [Chrono](#Chrono)
	- [Useless](#Useless)

2. Cryptography
	- [Rotation](#Rotation)
	- [ReadMyCert](#ReadMyCert)
	- [HideToSee](#HideToSee)

3. Forensics
	- [HideMe](#HideMe) 
	- [PcapPoisoning](#PcapPoisoning)
	- [WhoIsIt](#WhoIsIt)

4. Web
	- [FindMe](#FindMe)
	- [JavaCodeAnalys!?!](#JavaCodeAnalysis!?!)
	- [SOAP](#SOAP)

6. Reverse
	- [SafeOpener2](#SafeOpener2)
	- [Reverse](#Reverse)
	- [Timer](#Timer)

8. Pwn
	- [TwoSum](#TwoSum)
	- [Hijacking](#Hijacking)
	- [TicTac](#TicTac)

## **Rules**

![X category](https://img.shields.io/badge/category-GeneralSkills-blue.svg)
![X points](https://img.shields.io/badge/points-100-green.svg)

**Challenge Description :** Read the rules of the competition and get a little bonus !

### Approach

Let's check rules link and get the flag.
![](Images/GENERALSKILLS_Rules.png)

**Flag :** `picoCTF{h34rd_und3r5700d_4ck_cba1c711}`

## **Repetitions**

![X category](https://img.shields.io/badge/category-GeneralSkills-blue.svg)
![X points](https://img.shields.io/badge/points-100-green.svg)

**Challenge Description :** Can you make sense of this file ?

### Approach

As you can see in the challenge tags it's `base64` in the `.txt` file I just downloaded and it repeats. `Cyberchef` is the perfect tool for this challenge.
![](Images/GENERALSKILLS_Repetition.png)

After several decryption in `base64` I find the flag.
![](Images/GENERALSKILLS_Repetitions_1.png)

**Flag :** `picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_fffe6738}`

## **MoneyWare**

![X category](https://img.shields.io/badge/category-GeneralSkills-blue.svg)
![X points](https://img.shields.io/badge/points-100-green.svg)

**Challenge Description :** Your friend just got hacked and has been asked to pay some bitcoins to `1Mz7153HMuxXTuR2R1t78mGSdzaAtNbBWX`. 
He doesn’t seem to understand what is going on and asks you for advice. Can you identify what malware he’s being a victim of ?

### Approach

After one research on google with : `1Mz7153HMuxXTuR2R1t78mGSdzaAtNbBWX`
![](Images/GENERALSKILLS_Money_Ware.png)

The wallet was used by Petya ransomware.

![](Images/GENERALSKILLS_Money_Ware_1.png)

**Flag :** `picoCTF{Petya}`

## **Permissions**

![X category](https://img.shields.io/badge/category-GeneralSkills-blue.svg)
![X points](https://img.shields.io/badge/points-100-green.svg)

**Challenge Description :** Can you read files in the root file ?

### Approach

As you can see in the challenge tags is about vim and permissions. I know this type of challenge. Let's check on [GTFOBins](https://gtfobins.github.io/) if I find a good payload.
![](Images/GENERALSKILLS_Permissions.png)

Vim let me spawn a shell with root permissions and now it's easy to check /root flag.

![](Images/GENERALSKILLS_Permissions_1.png)

**Flag :** `picoCTF{uS1ng_v1m_3dit0r_2fb487cc}`

## **Chrono**

![X category](https://img.shields.io/badge/category-GeneralSkills-blue.svg)
![X points](https://img.shields.io/badge/points-100-green.svg)

**Challenge Description :** How to automate tasks to run at intervals on linux servers ?

### Approach

The description of the challenge allows me to see that this challenge talks about crontabs. Let's list them.

![](Images/GENERALSKILLS_Chrono.png)
![](Images/GENERALSKILLS_Chrono_1.png)

**Flag :** `picoCTF{Sch3DUL7NG_T45K3_L1NUX_05e9ab5e}`

## **Useless**

![X category](https://img.shields.io/badge/category-GeneralSkills-blue.svg)
![X points](https://img.shields.io/badge/points-100-green.svg)

**Challenge Description :** There's an interesting script in the user's home directory

### Approach

An other time, a good reading of the description helps for the challenge. 
Let's try `man useless`.
![](Images/GENERALSKILLS_Useless.png)
![](Images/GENERALSKILLS_Useless_1.png)

**Flag :** `picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_4675}`

## **Rotation**

![X category](https://img.shields.io/badge/category-Cryptography-blue.svg)
![X points](https://img.shields.io/badge/points-100-green.svg)

**Challenge Description :** You will find the flag after decrypting this file.

### Approach

As the title talks about rotation, I immediately think of rotational encryption and I go to [dcode](https://www.dcode.fr/) for brute-force and see the result.
![](Images/CRYPTO_Rotation.png)
![](Images/CRYPTO_Rotation_1.png)

**Flag :** `picoCTF{r0tation_d3crypt3d_59b71977}`

## **ReadMyCert**

![X category](https://img.shields.io/badge/category-Cryptography-blue.svg)
![X points](https://img.shields.io/badge/points-100-green.svg)

**Challenge Description :** How about we take you on an adventure on exploring certificate signing requests.

### Approach

I see that I just downloaded a `.csr` file and so I decide to click on it. This open a window, I observe and see the flag directly.
![](Images/CRYPTO_ReadMyCert.png)
![](Images/CRYPTO_ReadMyCert_1.png)

**Flag :** `picoCTF{read_mycert_e075addc}`

## **HideToSee**

![X category](https://img.shields.io/badge/category-Cryptography-blue.svg)
![X points](https://img.shields.io/badge/points-100-green.svg)

**Challenge Description :** How about some hide and seek heh ?

### Approach

After many try on [Aperi'Solve](https://www.aperisolve.com/),  and others ... just https://futureboy.us/stegano/decinput.html allowed me to find the cipher hidden in the image.

`krxlXGU{zgyzhs_xizxp_v7uzz0v5}`

After tests on dcode and cyberchef I did not find any data in clear. Infact I had forgotten that it was around the atbash cipher...

Finally, by noting the alphabet on a sheet to find the character string that is found at each challenge (picoCTF). I realized that the letters were substituted with the same alphabet but reversed, I could then the rest of the characters.

**A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z**
**Z, Y, X, W, V, U, T, S, R, Q, P, O, N, M, L, K, J, I, H, G, F, E, D, C, B, A**

![](Images/CRYPTO_HideToSee.png)

**Flag :** `picoCTF{atbash_crack_e7faa0e5}`

## **HideMe**

![X category](https://img.shields.io/badge/category-Forensics-blue.svg)
![X points](https://img.shields.io/badge/points-100-green.svg)

**Challenge Description :** The SOC analyst saw one image been sent back and forth between two people. They decided to investigate and found out that there was more than what meets the eye.

### Approach

Every time, I put the image in first in Aperi'Solve and I see an intriguing thing like a ZIP archive in `.png`.
![](Images/FORENSIC_HideMe.png)

Let's try to unzip it !
![](Images/FORENSIC_HideMe_1.png)

I can see a folder and an image that is unzipped. I just have to open the picture and see the flag.
![](Images/FORENSIC_HideMe_2.png)

![](Images/FORENSIC_HideMe_3.png)

**Flag :** `picoCTF{Hiddinng_An_imag3_within_@n_ima9e_5fbf3ff9}`

## **PcapPoisoning**

![X category](https://img.shields.io/badge/category-Forensics-blue.svg)
![X points](https://img.shields.io/badge/points-100-green.svg)

**Challenge Description :** How about some hide and seek heh ?

### Approach

After checking the Statistics of the capture on Wireshark. The thing that I do always for understand where I put my foot. I see FTP conversation and I put my investigation on it.

![](Images/FORENSIC_PcapPoisonning.png)

When I try to follow tcp stream I can see a clue (end of the flag).
![](Images/FORENSIC_PcapPoisonning_1.png)

By instinct, I double click on the 2nd trame and see the flag.
![](Images/FORENSIC_PcapPoisonning_2.png)
![](Images/FORENSIC_PcapPoisonning_3.png)

**Flag :** `picoCTF{P64P_4N4L7S1S_SU55355FUL_14f62f23}`

## **WhoIsIt**

![X category](https://img.shields.io/badge/category-Forensics-blue.svg)
![X points](https://img.shields.io/badge/points-100-green.svg)

**Challenge Description :** Someone just sent you an email claiming to be Google's co-founder Larry Page but you suspect a scam.
Can you help us identify whose mail server the email actually originated from ?

### Approach

In first, I open the file, inspect it and see IP address, let's see if whois can give me name information that I need for flag.
![](Images/FORENSIC_WhoIsIt.png)

`whois` on websites gives not all information, try on shell.
![](Images/FORENSIC_WhoIsIt_1.png)

![](Images/FORENSIC_WhoIsIt_2.png)

**Flag :** `picoCTF{WilhelmZwalina}`

## **FindMe**

![X category](https://img.shields.io/badge/category-Web-blue.svg)
![X points](https://img.shields.io/badge/points-100-green.svg)

**Challenge Description :** Help us test the form by submiting the username as `test` and password as `test!`

### Approach

This challenge is about redirections so, I open burpsuite and intercept all traffic for analyze step by step.
![](Images/WEB_FindMe.png)
![](Images/WEB_FindMe_1.png)

Results are here but encoded in base64
![](Images/WEB_FindMe_2.png)

![](Images/WEB_FindMe_3.png)

**Flag :** `picoCTF{proxies_all_the_way_81d4d831}`

## **JavaCodeAnalysis!?!**

![X category](https://img.shields.io/badge/category-Web-blue.svg)
![X points](https://img.shields.io/badge/points-300-green.svg)

**Challenge Description :** BookShelf Pico, my premium online book-reading service.I believe that my website is super secure. I challenge you to prove me wrong by reading the 'Flag' book !

### Approach

I'm coming on website who have 3 books and 1 book requiring Admin access (for reading the flag).
![](Images/WEB_JavaCodeAnalysis.png)

Inspection tool according to me to see an auth-token with `JWT` .
![](Images/WEB_JavaCodeAnalysis_6.png)

JWT was encoded with a secret, so I had to crack it with `hashcat`.
![](Images/WEB_JavaCodeAnalysis_1.png)


After that, I modify it on https://jwt.io/ and I put it in website.
![](Images/WEB_JavaCodeAnalysis_2.png)

After refreshing, I have my new authorizations (Admin), I can enter in the Admin dashboard and modify `user` permissions in `Admin`.
![](Images/WEB_JavaCodeAnalysis_3.png)

After logout/logon, user have good permissions for read the flag in the book.
![](Images/WEB_JavaCodeAnalysis_4.png)
![](Images/WEB_JavaCodeAnalysis_5.png)

**Flag :** `picoCTF{w34k_jwt_n0t_g00d_42f5774a}`

## **SOAP**

![X category](https://img.shields.io/badge/category-Web-blue.svg)
![X points](https://img.shields.io/badge/points-100-green.svg)

**Challenge Description :** The web project was rushed and no security assessment was done. Can you read the /etc/passwd file ?

### Approach

After much research to find a way to attack, I returned to instructions and I see `XXE` in tags. I never do this so I go on google to find things and I fall on a really good page (https://portswigger.net/web-security/xxe) who according to me to done this challenge.

When I click on button, It send `XML` to server.
![](Images/WEB_SOAP.png)
![](Images/WEB_SOAP_1.png)

Modify this `XML` for `XXE`.
![](Images/WEB_SOAP_2.png)

Result not on pictures but I can see `/etc/passwd` dans flag was in.

![](Images/WEB_SOAP_3.png)

**Flag :** `picoCTF{XML_3xtern@l_3nt1t1ty_e79a75d4}`

### Reflection

This challenge was pretty cool because it's thing that I nerver see.

## **SafeOpener2**

![X category](https://img.shields.io/badge/category-Reverse-blue.svg)
![X points](https://img.shields.io/badge/points-100-green.svg)

**Challenge Description :** What can you do with this file?I forgot the key to my safe but this file is supposed to help me with retrieving the lost key. Can you help me unlock my safe ?

### Approach
  
Like all the java code I see, I try to decompile it.
![](Images/REVERSE_SafeOpener2.png)

The flag was here.
![](Images/REVERSE_SafeOpener2_1.png)

**Flag :** `picoCTF{SAf3_Op3n3rr_y0u_solv3d_it_6d84122a}`

## **Reverse**

![X category](https://img.shields.io/badge/category-Reverse-blue.svg)
![X points](https://img.shields.io/badge/points-100-green.svg)

**Challenge Description :** Try reversing this file ? Can ya ?

### Approach
  
In first when I have file to reverse it. I do the command `strings`
![](Images/REVERSE_Reverse.png)

The flag is here.

![](Images/REVERSE_Reverse_1.png)

**Flag :** `picoCTF{3lf_r3v3r5ing_succe55ful_70eeb}`

## **Timer**

![X category](https://img.shields.io/badge/category-Reverse-blue.svg)
![X points](https://img.shields.io/badge/points-100-green.svg)

**Challenge Description :** You will find the flag after analysing this apk.

### Approach
  
I was never working on apk, I found decompiler (MobSF)
![](Images/REVERSE_Timer.png)

The flag is in `Android Version Name`.

![](Images/REVERSE_Timer_1.png)

**Flag :** `picoCTF{t1m3r_r3v3rs3d_succ355fuly_17496}`

## **TwoSum**

![X category](https://img.shields.io/badge/category-Pwn-blue.svg)
![X points](https://img.shields.io/badge/points-100-green.svg)

**Challenge Description :** Can you solve this ?

### Approach
  
After analysis, the given code contains a buffer overflow vulnerability in the `fgets` function call.
![](Images/PWN_TwoSum.png)

![](Images/PWN_TwoSum_1.png)

**Flag :** `picoCTF{Tw0_Sum_Integer_Bu773R_0v3rfl0w_f6ed8057}`

## **Hijacking**

![X category](https://img.shields.io/badge/category-Pwn-blue.svg)
![X points](https://img.shields.io/badge/points-200-green.svg)

**Challenge Description :** Getting root access can allow you to read the flag. Luckily there is a python file that you might like to play with.

### Approach

The challenge talks about playing with the python script but I found a permissions flaw on the vi tool so I exploited it
![](Images/PWN_Hijacking.png)

![](Images/PWN_Hijacking_1.png)

**Flag :** `picoCTF{pYth0nn_libraryH!j@CK!n9_13cfd3cc}`

## **TicTac**

![X category](https://img.shields.io/badge/category-Pwn-blue.svg)
![X points](https://img.shields.io/badge/points-200-green.svg)

**Challenge Description :** Someone created a program to read text files; we think the program reads files with root privileges but apparently it only accepts to read files that are owned by the user running it.

### Approach

The tags talk about `toctou` so I went to google and it's a flaw in the linux system. I followed the instructions and the payload worked.

https://samsclass.info/127/proj/E10.htm

![](Images/PWN_TicTac.png)

![](Images/PWN_TicTac_1.png)

**Flag :** `picoCTF{ToctoU_is_3a5y_04909d70a}`