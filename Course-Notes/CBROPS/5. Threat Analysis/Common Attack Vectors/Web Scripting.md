
- ==Malware Delivery==: Cybercriminals often deliver malware via the web, using newly infected websites.
- ==Web Scripting Dangers==: Security analysts should be aware of the dangers of web scripting, particularly $malicious$ JavaScript, which can silently redirect browsers to load malware.

**HTML**
- Web page content can be static and dynamic.
- ==Static Web Content==: Created using markup languages like HTML and XML, often with a .html extension.
- ==Document Rendering==: Read by a web browser and displayed on the client’s screen in a human-readable format.
- ==Source Code Access==: Viewable in web browsers like Internet Explorer by navigating to View > Source.

```
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>My First Heading</h1>
<p>My first paragraph.</p>

</body>
</html>
```

![3](/Course-Notes/.assets/Pasted_image_20241119092136.png)

**CSS** 
- ==Definition==: A style sheet language used to describe the style of an HTML document.
- ==Function==: Specifies how HTML elements should be displayed, such as background color.
- ==Example Usage==: `background-color: lightblue;` displays a light blue background color on a web page.

```
<!DOCTYPE html>
<html>
<head>
==<style>
body {
    background-color: lightblue;
}
</style>==
</head>
<body>

<h1>Hello Cisco!</h1>

<p>This page has a light blue background color!</p>

</body>
</html>
```

CSS can also be used to indicate the text alignment, font size, and so on.

## Server-Side and Client-Side Scripting

- ==Web Scripting==: Creates dynamic content on web pages, enhancing user experience beyond static content.
- ==Server-side== Scripting: Implemented on web servers to generate customized responses for each user request, using languages like PERL, Python, PHP, etc.
- ==Client-side== Scripting: Executed by the user’s web browser using languages like JavaScript, Visual Basic Script, etc., to enhance interactivity.

**JavaScript** 
- ==Implementation==: Define JavaScript in a separate file and link to it using the src attribute of the script tag.
- ==Embedding==: Embed JavaScript in a web page using the `<script type=“text/javascript”>` and `</script>` tags.
- ==File Example==: scriptname.js file contains the JavaScript.

```
<!DOCTYPE html>
<html>
<body>
==<script type="text/javascript" src="scriptname.js"></script>==
</body>
</html>
```

Instead of specifying the JavaScript file with the `src` attribute, the actual JavaScript can be written between the `<script type="text/javascript">` and `</script">` tags, as shown below:

```
<script type="text/javascript">
==document.write('Hello Cisco')==
</script>
```

The above JavaScript will render the "Hello Cisco" output on the client's web browser.

The `<script>` tag can also be used to tag the JavaScript instead of `<script type="text/javascript">` as shown below. The `<script type="text/javascript">` tag is required in HTML 4, but optional in HTML 5. In HTML 5, the script type defaults to text/javascript.

```
==<script>==
document.write('Hello HTML 5')
==</script>==
```

# Obfuscated JavaScript

- ==Purpose==: To disguise the appearance of source code and reduce its size.
- ==Goal==: To protect intellectual property by making JavaScript source code difficult to analyze or steal.
- ==Technique==: Encoding JavaScript into difficult-to-read statements.

For attackers:
- ==Purpose==: Disguise malicious code to avoid detection and execute it on a workstation.
- ==Goal==: Execute malicious code undetected to achieve their objectives.
- ==Intent==: Compromise a system.

For analysts: 
- ==Obfuscated JavaScript==: Should not be automatically considered malicious, but analysts should recognize the challenges in identifying them.
- ==Obfuscation Attack Popularity==: Increasingly popular and difficult to detect.

## Obfuscation techniques:
1. Automatically renaming variables to random names to reduce readability.
2. JavaScript ignores whitespace. White-space randomization involves inserting whitespace characters and line breaks without altering code functionality.
3. Self-modifying source code that rewrites itself during execution.
4. Character code and string manipulation combined with misusing ‘eval()’.

The example here represents a benign script that simply outputs the phrase “Hello World!”:

```
<script>
Alert("Hello World!")
</script>
```

This example appears as normal script code and can be deciphered to determine what will occur when the script is executed. Review the simple browser pop-up window:

![2](/Course-Notes/.assets/Pasted_image_20241119100624.png)

Next, examine the same code after it has been run through a script-encoding tool:

```
eval (function (p,a,c,k,e, d) {e=function (c) {return c};if (!''.replace (/^/,String)) {while (c--) {d[c]=k[c]|c}k=[function (e) {return d[el]}];e=function() {return'\\w +'}; c=1};while (c--) {if (k[c]) {p=p.replace(new RegExp ('\\b'+e(c)+'\\b', 'g'), k[c])}}return p}('<0><1("32! ") <0>,4,4, 'script|alert|World Hello'.split ('|'),0,1}))
```

![1](/Course-Notes/.assets/Pasted_image_20241119100627.png)

- ==Obfuscation Goal==: Prevent analysts from determining the intended functionality of the script.
- ==Obfuscation Method==: Encoding the script makes it difficult to recognize the original code.
- ==Obfuscation Effect==: Decrypting the encoded script is a complex process.

JavaScript is commonly embedded within HTML code and is executed on the client-side system. Encoding JavaScript can allow a threat actor to hide malicious code that will be executed on a target machine.

- ==JavaScript Obfuscation==: An effective method for disguising code functionality, but not indecipherable to experienced analysts.
- ==JavaScript Analysis Tools==: Tools like BurpSuite, JSDetox use de-obfuscation techniques and HTML DOM emulation for analyzing JavaScript malware.
- ==Manual De-obfuscation==: Not typically performed by Tier 1 SOC analysts, but they should recognize obfuscated JavaScript and decide whether to proceed or escalate.

In the following example, the variable was set as a two-character $a key. This key value was created during the encoding process using the encoder tool, JJEncode.

```
$a=~[];$a={___:++$a,$$$$:(![]+"")[$a],__$:++$a,$_$_:(![]+"")[$a],_$_:++$a,$_$$:({}+"")[$a],$$_$:($a[$a]+"")[$a],_$$:++$a,$$$_:(!""+"")[$a],$__:++$a,$_$:++$a,$$__:({}+"")[$a],$$_:++$a,$$$:++$a,$___:++$a,$__$:++$a};$a.$_=($a.$_=$a+"")[$a.$_$]+($a._$=$a.$_[$a.__$])+($a.$$=($a.$+"")[$a.__$])+((!$a)+"")[$a._$$]+($a.__=$a.$_[$a.$$_])+($a.$=(!""+"")[$a.__$])+($a._=(!""+"")[$a._$_])+$a.$_[$a.$_$]+$a.__+$a._$+$a.$;$a.$$=$a.$+(!""+"")[$a._$$]+$a.__+$a._+$a.$+$a.$$;$a.$=($a.___)[$a.$_][$a.$_];$a.$($a.$($a.$$+"\""+"\\"+$a.__$+$a._$_+"\"")())();
```

In this example, the variable was set as a two-character $a key and was parsed with the phrase "This SOC rocks!" encoded within the script:

```
$a=~[];$a={___:++$a,$$$$:(![]+"")[$a],__$:++$a,$_$_:(![]+"")[$a],_$_:++$a,$_$$:({}+"")[$a],$$_$:($a[$a]+"")[$a],_$$:++$a,$$$_:(!""+"")[$a],$__:++$a,$_$:++$a,$$__:({}+"")[$a],$$_:++$a,$$$:++$a,$___:++$a,$__$:++$a};$a.$_=($a.$_=$a+"")[$a.$_$]+($a._$=$a.$_[$a.__$])+($a.$$=($a.$+"")[$a.__$])+((!$a)+"")[$a._$$]+($a.__=$a.$_[$a.$$_])+($a.$=(!""+"")[$a.__$])+($a._=(!""+"")[$a._$_])+$a.$_[$a.$_$]+$a.__+$a._$+$a.$;$a.$$=$a.$+(!""+"")[$a._$$]+$a.__+$a._+$a.$+$a.$$;$a.$=($a.___)[$a.$_][$a.$_];$a.$($a.$($a.$$+"\""+"\\"+$a.__$+$a._$_+$a.$$$+$a.$$$_+"\\"+$a.$__+$a.___+"\\"+$a.__$+$a.$$_+$a._$_+$a._$+$a.$$__+"\\"+$a.__$+$a.$_$+$a._$$+"\\"+$a.$__+$a.___+$a.$_$_+"\\"+$a.__$+$a.$$_+$a._$$+"\\"+$a.$__+$a.___+$a.$_$_+"\\"+$a.$__+$a.___+"\\"+$a.__$+$a._$_+$a._$$+"\\"+$a.__$+$a.__$+$a.$$$+"\\"+$a.__$+$a.___+$a._$$+"."+"\"")())();
```

In this final example, the variable "$" is used as the encoding key:

```
$=~[];$={___:++$,$$$$:(![]+"")[$],__$:++$,$_$_:(![]+"")[$],_$_:++$,$_$$:({}+"")[$],$$_$:($[$]+"")[$],_$$:++$,$$$_:(!""+"")[$],$__:++$,$_$:++$,$$__:({}+"")[$],$$_:++$,$$$:++$,$___:++$,$__$:++$};$.$_=($.$_=$+"")[$.$_$]+($._$=$.$_[$.__$])+($.$$=($.$+"")[$.__$])+((!$)+"")[$._$$]+($.__=$.$_[$.$$_])+($.$=(!""+"")[$.__$])+($._=(!""+"")[$._$_])+$.$_[$.$_$]+$.__+$._$+$.$;$.$$=$.$+(!""+"")[$._$$]+$.__+$._+$.$+$.$$;$.$=($.___)[$.$_][$.$_];$.$($.$($.$$+"\""+"\\"+$.__$+$._$_+$.$$$+$.$$$_+"\\"+$.$__+$.___+"\\"+$.__$+$.$$_+$._$_+$._$+$.$$__+"\\"+$.__$+$.$_$+$._$$+"\\"+$.$__+$.___+$.$_$_+"\\"+$.__$+$.$$_+$._$$+"\\"+$.$__+$.___+$.$_$_+"\\"+$.$__+$.___+"\\"+$.__$+$._$_+$._$$+"\\"+$.__$+$.__$+$.$$$+"\\"+$.__$+$.___+$._$$+"."+"\"")())();
```

