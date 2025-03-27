
URLs typically use ASCII format, which includes letters, numbers, and symbols found on a standard keyboard. http://www.google.com.

- ==Purpose==: Represents Unicode characters in ASCII format for DNS compatibility.
- ==Format==: `xn—<\URL minus special characters>-<\codes for special characters>.<TLD… (.com .net .org )>.`
- ==Example==: fàcebook.com 
  becomes xn—fcebook-lta.com.

![2](/Course-Notes/.assets/Pasted_image_20241119222907.png)

The browser converts it to Punycode automatically, which is quite helpful.

- ==Spam Email==: Spam emails can include product/service offers, financial transaction requests, and phishing attempts.
- ==Phishing Email==: Might appear legitimate, claiming a Facebook account compromise and prompting password reset.
- ==Malicious Link==: Might use a character substitution (e.g., www.fàcebook.com) to deceive users and lead them to a malicious site.

Non-ASCII characters can be used in countless ways to fool people. Punycode itself can hide nefarious URLs.

![1](/Course-Notes/.assets/Pasted_image_20241119223044.png)

Replacing all “i” characters in a link with the Cyrillic version of “i”.

- ==URL Display==: The address in the browser appears as a manually typed URL, but with Cyrillic “i”s converted to Punycode.
- ==Browser==: The browser recognizes the URL as similar to a legitimate website and offers a suggestion.
- ==Behavior==: Users clicking on illegitimate links do not receive the same browser suggestion.