# Wreck CTF

**Website :** [WreckCTF](https://wreckctf.com/)

![X date](https://img.shields.io/badge/date-30/09/2022-yellow.svg)
![X total points](https://img.shields.io/badge/total_points-888-blue.svg)
![X rank](https://img.shields.io/badge/team_ranking-274%2F524-purple.svg)
![X solo](https://img.shields.io/badge/team-alone-orange.svg)

**Description :** Every year, the GreyHat cybersecurity club hosts an educational capture-the-flag competition to help college students around the world build cybersecurity skills. The competition features a number of intentionally vulnerable websites, insecure cryptographic schemes, exploitable binaries, unsafe machine learning models, and more. The full competition runs online from Sept 30 to Oct 2 (2022) and is open to everyone (college students, high school students, and security enthusiasts). We’ll have problems that are interesting to both beginners and advanced students.

For this CTF, I participated (alone) from the opening on Friday, September 30 at 10 p.m and I stopped 2-3 hours later.

## **Table of Contents**

1. Miscellaneous
    - [Discord](#Discord)
    - [Smoke-check](#Smoke-check)
    - [Bash](#Bash)

2. Web
    - [Sources](#Sources)
    - [Password-1](#Password-1)
    - [Password-2](#Password-2)
    - [Notes-1](#Notes-1)

3. Crypto
    - [Spin](#Spin)

## Discord

![X category](https://img.shields.io/badge/category-Miscellaneous-blue.svg)
![X points](https://img.shields.io/badge/points-1-green.svg)

**Challenge Description :** This challenge is just for join the Discord and catch the flag on the "Annoucement" Channel.

### Approach

So I was join the WRECKCTF discord and I found the flag.

**![](https://lh5.googleusercontent.com/IyzwdctQmK2MI-Ou49OuqAqTZ9GMsYLijjKParaJg5vdrUk5AgUsMpKlZhiiOOKoCshP8GQjK-TmV92V38RVCTtY4i3_TOi0whEQ9jaCHYW-Yyr8vkhE7ZK5eKHp-hh71zCz19Rqn4egj55DveMpMIGAm1v8V8h9To9Zi3qznmT3mJow5kxEiuWS2A)**

**Flag :** `flag{this_is_the_discord_flag}`

## Smoke-check

![X category](https://img.shields.io/badge/category-Miscellaneous-blue.svg)
![X points](https://img.shields.io/badge/points-1-green.svg)

**Challenge Description:** What's in the `flag.txt` ?

### Approach

I read the file `flag.txt` and i found the flag (very difficult !).

**![](https://lh3.googleusercontent.com/6neOk4WevSmyyVmO3AEvbDUhyMlxhUnWsuzXoZEI_T5mZlvOTBnBr1bm_UCTRtLhUrPsytlAQJaFF8OUKa30It6T9AbL-UvMd-wvsSpXbXSb8Y5HyYc2-Ic0BkIyp_3Q4D5fFr7uboKX_4W7lcLEafn_J8NAEITiUo-NqXa2ieaJ4qpwOFhUAOsfbw)**

**Flag :** `flag{this_is_what_flags_look_like}`

## Bash

![X category](https://img.shields.io/badge/category-Miscellaneous-blue.svg)
![X points](https://img.shields.io/badge/points-112-green.svg)

**Challenge Description :** I guess it's probably dash, not bash. can you read the flag ?
`nc challs.wreckctf.com 31106`

### Approach

I was try the netcat connection and I type many commands like `ls`, after that I was sure of the bash shell because I was in possibility to list files and read `flag.txt`.

[![asciicast](https://asciinema.org/a/lg8Z8SHBiTwVfyjbQZEIaedVv.svg)](https://asciinema.org/a/lg8Z8SHBiTwVfyjbQZEIaedVv)

**Flag :** `flag{cat_the_flag}`

## Sources

![X category](https://img.shields.io/badge/category-Miscellaneous-blue.svg)
![X points](https://img.shields.io/badge/points-100-green.svg)

**Challenge Description :** Click to spin, search for the flag !
`sources.challs.wreckctf.com`

### Approach

I know this challenges and I have directely check they web sources, here we have different parts of the flag in differents files.

**![](https://lh6.googleusercontent.com/SZBQda3E0fBXwplp-vAXZCYPHcLVKq1_pC3KMNfnwmkWMM4m9pAay4GMiMTQlhuVT9IsZPEVEFczoLNzaB3Svae-MMckC-XJrBgbesUDfx3fjLvDpcrOi_L645jYlhDeZDvI9N5Cz4eW16GZrlfN-8l8YPvS0m_RoHvsWtbiY_jLNbCiLKuSi_2VOQ)**
**![](https://lh4.googleusercontent.com/5kCYh93q1Wxch2VpBAhISm_Z7LnQMp6A8vgYSJtdOMbDm5pGjgS1BTkODaH9hyPKKiPt--6_v-CSRmH1tPY2HYTNqPWiTJOXqclG_l4EHzSIA--UkcmXEt_h-cXt5Q8-Mr3sLUu1kmA46UgRcsVBI-Jh8QKiKyiEjkGVw5X3QKbfrCLW5yspygopNg)**
**![](https://lh3.googleusercontent.com/oN2n_GpUP0SHSm1o38aAZNeeUZiEyhJNb8hp03979OG8pRKo61eOUI1GQT3T9mOuVzi68sTIDNupD9TAaFypnQzIlxebmKtmvRBOQ_HBy-wNNVWxEfu4tMDpuK2gi5Allc8jadTMEnF-AhqyaAwRG2g45M0QzTirwiRallrYQad2kzf78tfMeTa47w)**

### Reflections

**Check always** page source and scripts sources with navigators inspect tools.

## Password-1

![X category](https://img.shields.io/badge/category-Web-blue.svg)
![X points](https://img.shields.io/badge/points-130-green.svg)

**Challenge Description :** Can you figure out how to log in ?
`https://password-1.challs.wreckctf.com`

### Approach

In this challenge, we have the code source of the site and I see somewhere in the code (picture) an link to `/api/output` and this link call function who lunck a request to `flag`. So I decide to check this link and I found the flag.

![Code_Web_Password-1.png](Images/Code_Web_Password-1.png)
**![](https://lh4.googleusercontent.com/s41kY_7K20Q80B-1M_grTPDzI1mzLrB8XIPFiG-rQGYmcPUY3Yx376A63cma67wxIgi5I63eS1wBfWDA4Ja9Ui7FdvmIOSYi73VY7slnTElsF-7NjvReYAkckdN_bGnd7ygtfehldEYjbZ4RG0HOYRmCrWjPUH08NJpqJsB01vacsZrVNEPCdUxFIg)**

**Falg :** `flag{why_is_hashing_in_browser_so_hard}`

## Password-2

![X category](https://img.shields.io/badge/category-Web-blue.svg)
![X points](https://img.shields.io/badge/points-183-green.svg)

**Challenge Description :** Okay, i fixed that. can you still log in?
`password-2.challs.wreckctf.com`

### Approach

This challenge is like the Web/Password-1, I have the source code of the website. I look it and I see an simple SQL command in the code, so i decide to launch an easy SQL injection with `' OR '1'='1` who work and let me see the flag.

![Code_Web_Password-2.png](Images/Code_Web_Password-2.png)
**![](https://lh5.googleusercontent.com/3d0NUjPDfAR1-XM8vpgvKiYdN3n92NEeLFeQWWCKcjqxfpiNAxhwgRQDq-Jf0a1-DPay9geIAAK8tpnr2z-fTelKtEi8BM6sOeQYljNT4eJ-djflke0oILvwhmQiXs5eY4epq5RjcXP3_ywCZ841X_nWT9otLxYXF2zYaVLtljzjqjIDQi1Rvgm13w)**

**Flag :** `flag{i_love_in_memery_sqlite}`

### Reflections

Adding `'OR'1'='1`, which is a true statement, all passwords are returned.

## Notes-1

![X category](https://img.shields.io/badge/category-Web-blue.svg)
![X points](https://img.shields.io/badge/points-245-green.svg)

**Challenge Description :** Can you read the admin's note ?
`https://notes-1.challs.wreckctf.com`

### Approach

I decide to test in first the functionnatilies. I create many notes and i see the url, It change. In second time, I look the code and I see the id of notes is encode in `sha256`. So I took an `sha256` and I was decoding it. In fact, the note id is just a number who incremental one to one. After that I encode 0 in `sha256` and i was putting it in the url and I had the flag !
Also I tried to `-1` but I had no results.

**![](https://lh3.googleusercontent.com/Yj-JGksjg9pMLqoJe-AlBHrCFl7_mqCkNvpSbxMm6o7LUFH5HZWIAKKyupRhj1zPWQ_1De2twzIx4LUSLWJvJJ31ua_8m-17NAb0nHfTGwtcvE44sdZzOHI8UedMbfucI4PWqQrYxFaZok2nbRnvfqBvKg225ibbR9Ad7LBV49GYtZRF2qYAyOSptg)**
**![](https://lh5.googleusercontent.com/idH3JzUsLlx8w7itl6DlSeMdaENTDpLibpdiWu4jLUCg_tgjOJMg7q22tfiOP-F7uXNM3OiF62q__zPnCggu8bJI7p0ug5IifI9wt536boH2Bepd7Mk4JW-iUz9Kszje_y-4FuC0E9IcFI7NA5bk6fcxXJjprblRvGcyCK6IZGwABW7bG3UsAfqFbQ)**
**![](https://lh4.googleusercontent.com/ZajDEgh2PO3h2tq78nwKIkrGpKVufEC69H6aEehkmh7rEIDetNToAtCtXe-Ce4Rmi73DCtrQFzApAxMbrSOuxC0Ao0V2P2HKq5jKLFdxlsPMZLQWZRw09bcJTUnCg6AwRjE5zcL40rIHSRpPLSdeJSGAtC505r-VJPwPpePDhW1lbkA91_-IbXNanQ)**

**Flag :** `flag{technically_a_vulnerability}`

## Spin

![X category](https://img.shields.io/badge/category-Crypto-blue.svg)
![X points](https://img.shields.io/badge/points-116-green.svg)

**Challenge Description :** The classics.
`oujp{xkurpjcxah_ljnbja_lryqna}`

### Approach

For this challenge, I have read the code who is given (picture) and directly I recognized the cesar method for cipher a text (view in classes !). Good, I can use the code creates in classes for bruteforce and decrypt the potentially Cesar cipher text.

![Code_Crypto_Spin.png](Images/Code_Crypto_Spin.png)

**Flag :** `flag{obligatory_caesar_cipher}`
